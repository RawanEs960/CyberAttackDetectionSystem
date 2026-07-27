# ==========================================
# Cyber Attack Detection System
# Flask Web Application
# ==========================================

from flask import (
    Flask,
    render_template,
    request,
    send_file
)

import os
import joblib
import pandas as pd

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

# ==========================================
# Create Flask App
# ==========================================

app = Flask(__name__)

# ==========================================
# Directories
# ==========================================

BASE_DIR = os.path.dirname(__file__)

MODEL_DIR = os.path.join(BASE_DIR, "models")

UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

CHART_DIR = os.path.join(
    BASE_DIR,
    "static",
    "charts"
)

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(CHART_DIR, exist_ok=True)

# ==========================================
# Load Saved Files
# ==========================================

model = joblib.load(
    os.path.join(
        MODEL_DIR,
        "optimized_xgboost.pkl"
    )
)

feature_names = joblib.load(
    os.path.join(
        MODEL_DIR,
        "feature_names.pkl"
    )
)

label_encoder = joblib.load(
    os.path.join(
        MODEL_DIR,
        "label_encoder.pkl"
    )
)

print("="*50)
print("Model Loaded Successfully")
print("="*50)

# ==========================================
# Home Page
# ==========================================

@app.route("/")

def home():

    return render_template(
        "index.html"
    )

# ==========================================
# Prediction
# ==========================================

@app.route(
    "/predict",
    methods=["POST"]
)

def predict():

    # -----------------------------
    # Check Uploaded File
    # -----------------------------

    if "file" not in request.files:

        return render_template(
            "error.html",
            missing=["No file uploaded"]
        )

    uploaded_file = request.files["file"]

    if uploaded_file.filename == "":

        return render_template(
            "error.html",
            missing=["No selected file"]
        )

    # -----------------------------
    # Save File
    # -----------------------------

    file_path = os.path.join(
        UPLOAD_DIR,
        uploaded_file.filename
    )

    uploaded_file.save(file_path)

    # -----------------------------
    # Read CSV
    # -----------------------------

    try:

        data = pd.read_csv(file_path)

    except Exception:

        return render_template(
            "error.html",
            missing=["Invalid CSV file"]
        )

    # -----------------------------
    # Validate Columns
    # -----------------------------

    missing_columns = [

        col

        for col in feature_names

        if col not in data.columns

    ]

    if len(missing_columns) > 0:

        return render_template(

            "error.html",

            missing=missing_columns

        )

    # -----------------------------
    # Select Features
    # -----------------------------

    X = data[feature_names]

    # -----------------------------
    # Prediction
    # -----------------------------

    predictions = model.predict(X)

    labels = label_encoder.inverse_transform(
        predictions
    )

    data["Prediction"] = labels

    # -----------------------------
    # Save Predictions
    # -----------------------------

    output_file = os.path.join(
        OUTPUT_DIR,
        "predictions.csv"
    )

    data.to_csv(
        output_file,
        index=False
    )

    # -----------------------------
    # Statistics
    # -----------------------------

    prediction_counts = (

        data["Prediction"]

        .value_counts()

        .sort_values(ascending=False)

        .to_dict()

    )

    # -----------------------------
    # Pie Chart
    # -----------------------------

    plt.figure(figsize=(7,7))

    plt.pie(

        prediction_counts.values(),

        labels=prediction_counts.keys(),

        autopct="%1.1f%%",

        startangle=90

    )

    plt.title(
        "Prediction Distribution"
    )

    plt.tight_layout()

    plt.savefig(

        os.path.join(

            CHART_DIR,

            "prediction_pie.png"

        )

    )

    plt.close()

    # -----------------------------
    # Bar Chart
    # -----------------------------

    plt.figure(figsize=(8,5))

    plt.bar(

        prediction_counts.keys(),

        prediction_counts.values()

    )

    plt.title(
        "Prediction Counts"
    )

    plt.ylabel(
        "Samples"
    )

    plt.xticks(rotation=25)

    plt.tight_layout()

    plt.savefig(

        os.path.join(

            CHART_DIR,

            "prediction_bar.png"

        )

    )

    plt.close()

    # -----------------------------
    # Display Results
    # -----------------------------

    return render_template(

        "results.html",

        table=data.to_html(

            classes="table table-striped table-hover",

            index=False

        ),

        stats=prediction_counts,

        total_rows=len(data),

        pie_chart="charts/prediction_pie.png",

        bar_chart="charts/prediction_bar.png"

    )

# ==========================================
# Download Results
# ==========================================

@app.route("/download")

def download():

    return send_file(

        os.path.join(

            OUTPUT_DIR,

            "predictions.csv"

        ),

        as_attachment=True

    )

# ==========================================
# Run Flask
# ==========================================

if __name__ == "__main__":

    app.run(

        debug=True

    )
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import numpy as np

# إنشاء تطبيق Flask
app = Flask(__name__)

# تحميل النموذج المحفوظ
model = joblib.load("../models/xgboost_cicids2017.pkl")


# الصفحة الرئيسية (اختيارية)
@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/")
# def home():
#     return jsonify({
#         "message": "🚀 Cyber Attack Detection API is running successfully!"
#     })

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # استقبال البيانات بصيغة JSON
        data = request.get_json()

        # تحويلها إلى DataFrame (صف واحد فقط)
        df = pd.DataFrame([data])

        # تمرير البيانات للنموذج
        prediction = model.predict(df)[0]

        # بناء النتيجة النصية
        result = "⚠️ Attack Detected" if prediction == 1 else "✅ Normal Traffic"

        return jsonify({
            "prediction": int(prediction),
            "result": result
        })

    except Exception as e:
        return jsonify({"error": str(e)})

      

if __name__ == "__main__":
    app.run(debug=True)

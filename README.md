# Intelligent Web-Based System for Network Traffic Analysis and Cyber-Attack Detection Using Machine Learning Techniques

## Project Overview

This project presents an intelligent web-based Intrusion Detection System (IDS) that analyzes network traffic and detects cyber-attacks using Machine Learning techniques.

The system was developed as part of a Master's research project and combines data preprocessing, feature selection, hyperparameter optimization, explainable artificial intelligence (XAI), and a Flask web application for real-time prediction.

---

## Dataset

- CICIDS2017 Network Intrusion Detection Dataset
- Balanced Sampling Strategy
- More than 2.5 million original network traffic records

---

## Project Structure

```
CyberAttackDetectionSystem/

│

├── data/

├── experiments/

│      E01_ModelComparison

│      E02_FeatureSelection

│      E03_HyperparameterOptimization

│      E04_ModelExplainability

│      E05_WebApplication

│

├── flask_app/

├── notebooks/

├── test_files/

├── docs/

└── README.md
```

---

## Experiments

### E01 — Model Comparison

Compared multiple machine learning models:

- Decision Tree
- Random Forest
- LightGBM
- XGBoost

---

### E02 — Feature Selection

Feature importance was computed using Random Forest.

Different feature subsets were evaluated:

- All Features
- Top 30
- Top 25
- Top 20
- Top 15

Top-30 features achieved the best balance between accuracy and computational cost.

---

### E03 — Hyperparameter Optimization

RandomizedSearchCV was applied to optimize the XGBoost classifier.

Evaluation included:

- Accuracy
- Precision
- Recall
- F1-score
- Training Time
- Prediction Time

---

### E04 — Model Explainability

Explainable Artificial Intelligence (XAI) was implemented using SHAP.

Generated visualizations include:

- SHAP Summary Plot
- SHAP Feature Importance
- SHAP Waterfall Plot

---

### E05 — Flask Web Application

The optimized XGBoost model was deployed using Flask.

Application features:

- Upload CSV files
- Predict cyber attacks
- Display prediction statistics
- Pie Chart visualization
- Bar Chart visualization
- SHAP Explainability visualizations
- Download prediction results

---

## Machine Learning Model

Final Model:

- Optimized XGBoost

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1-score

---

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- SHAP
- Flask
- Bootstrap
- Matplotlib
- Joblib

---

## Installation

Clone the repository

```bash
git clone https://github.com/RawanEs960/CyberAttackDetectionSystem.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
cd flask_app
python app.py
```

---

## Project Outcome

The proposed intelligent intrusion detection system successfully integrates:

- Machine Learning
- Feature Selection
- Hyperparameter Optimization
- Explainable AI (SHAP)
- Interactive Flask Deployment

into a complete cyber-attack detection framework suitable for practical network traffic analysis.

---

## Author

Rawan Esmandar

Master of Web Sciences

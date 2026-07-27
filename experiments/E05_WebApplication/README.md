# E05 - Flask Web Application

## Objective

The objective of this experiment is to deploy the optimized XGBoost intrusion detection model as a web application using Flask. The application enables users to upload network traffic data, perform cyber attack prediction, visualize prediction statistics, and inspect Explainable AI (SHAP) visualizations generated in Experiment E04.

---

## Workflow

1. Load the optimized XGBoost model.
2. Load the Label Encoder.
3. Load the selected Top-30 feature names.
4. Upload a CSV file containing network traffic.
5. Validate the required input features.
6. Predict attack classes.
7. Display prediction statistics.
8. Generate prediction charts.
9. Display SHAP explainability visualizations.
10. Download prediction results.

---

## Inputs

- CSV Network Traffic File

---

## Outputs

- Attack Predictions
- Prediction Statistics
- Prediction Distribution Pie Chart
- Prediction Count Bar Chart
- Prediction Table
- SHAP Summary Plot
- SHAP Feature Importance
- SHAP Waterfall Plot
- Downloadable Prediction CSV

---

## Technologies

- Flask
- Python
- XGBoost
- SHAP
- Bootstrap
- Pandas
- Matplotlib
- Joblib

---

## Result

The optimized XGBoost model was successfully deployed as an interactive web application capable of detecting cyber attacks and providing interpretable prediction results using SHAP visualizations.
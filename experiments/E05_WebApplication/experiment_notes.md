# Experiment Notes

## Experiment

E05 - Flask Web Application

---

## Notes

The optimized XGBoost model produced in Experiment E03 was deployed without retraining.

The selected Top-30 features generated in Experiment E02 were reused to validate uploaded datasets.

The SHAP visualizations generated during Experiment E04 were integrated into the web application to provide global model explainability.

The application validates uploaded CSV files before prediction by checking the required feature names.

Prediction results are displayed through multiple visualization components including:

- Prediction statistics
- Pie chart
- Bar chart
- Prediction table
- SHAP Summary Plot
- SHAP Feature Importance
- SHAP Waterfall Plot

The application also allows users to download prediction results as a CSV file.

---

## Conclusion

The Flask deployment demonstrates how machine learning and explainable artificial intelligence can be integrated into a practical cyber security application for real-time network traffic analysis.
# Experiment Notes

## Experiment Information

**Experiment ID:** E04_ModelExplainability

**Date:** 23 July 2026

**Status:** Completed

---

## Objective

Interpret the predictions of the optimized XGBoost model using SHAP in order to improve model transparency and explain the contribution of each selected feature.

---

## Methodology

* The optimized XGBoost model produced in Experiment E03 was loaded.
* No additional model training was performed.
* The Top 30 selected features generated in Experiment E02 were reused.
* SHAP TreeExplainer was employed to compute feature contributions.
* A subset of the dataset was sampled to reduce computational cost during SHAP analysis.
* Multiple SHAP visualizations were generated to provide both global and local model explanations.

---

## Generated Figures

* SHAP Summary Plot
* SHAP Feature Importance Plot
* SHAP Waterfall Plot
* SHAP Dependence Plot

---

## Observations

* SHAP successfully identified the most influential network traffic features.
* The explanations confirmed that only a small subset of features contributes significantly to model decisions.
* Global explanations revealed overall feature importance across the dataset.
* Local explanations illustrated how individual feature values influenced specific predictions.

---

## Conclusion

The optimized XGBoost model demonstrates not only excellent predictive performance but also a high degree of interpretability through SHAP, making it more suitable for practical cybersecurity applications where explainability is essential.

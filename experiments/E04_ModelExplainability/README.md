# Experiment E04: Model Explainability Using SHAP

## Experiment Information

**Experiment ID:** E04_ModelExplainability

**Objective:**

Provide an interpretable explanation of the optimized XGBoost model using SHAP (SHapley Additive exPlanations). This experiment aims to identify the contribution of each selected feature to the model predictions and improve the transparency of the proposed intrusion detection system.

---

## Input Files

This experiment directly uses the outputs generated in previous experiments.

From **Experiment E03**

* optimized_xgboost.pkl
* label_encoder.pkl
* feature_names.pkl

From **Experiment E02**

* selected_features.csv (Top 30 Features)

Dataset

* CICIDS2017 (Cleaned)

---

## Explainability Method

SHAP (TreeExplainer)

The optimized XGBoost model is interpreted without retraining. SHAP values are computed only for the selected Top 30 features.

---

## Generated Visualizations

* SHAP Summary Plot
* SHAP Feature Importance
* SHAP Waterfall Plot
* SHAP Dependence Plot

---

## Output Files

```
figures/
│
├── shap_summary.png
├── shap_feature_importance.png
├── shap_waterfall.png
└── shap_dependence.png
```

```
trained_models/
│
└── optimized_xgboost.pkl
```

---

## Outcome

The experiment provides a transparent interpretation of the optimized XGBoost model and identifies the most influential network traffic features responsible for cyber-attack detection.

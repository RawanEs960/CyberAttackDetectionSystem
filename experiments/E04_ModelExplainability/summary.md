# Experiment E04 Summary

## Experiment Title

Model Explainability Using SHAP

---

## Objective

Explain the decision-making process of the optimized XGBoost model using SHAP and identify the contribution of the selected Top 30 features to cyber-attack classification.

---

## Explainability Technique

SHAP (SHapley Additive exPlanations)

---

## Input Model

Optimized XGBoost Model (Experiment E03)

---

## Selected Features

Top 30 Features (Experiment E02)

---

## Generated Outputs

| Output                  | Description                                               |
| ----------------------- | --------------------------------------------------------- |
| SHAP Summary Plot       | Global feature impact across the dataset                  |
| SHAP Feature Importance | Ranking of feature importance                             |
| SHAP Waterfall Plot     | Local explanation for an individual prediction            |
| SHAP Dependence Plot    | Relationship between feature values and SHAP contribution |

---

## Key Findings

* SHAP successfully explained the behavior of the optimized XGBoost model.
* The generated explanations identified the most influential traffic features used for cyber-attack detection.
* Both global and local explanations were produced, increasing model transparency.
* The explainability results support the reliability of the proposed intelligent intrusion detection system.

---

## Final Decision

The optimized XGBoost model, together with SHAP explanations, was selected as the final machine learning model for integration into the web-based cyber-attack detection system developed in this research.

---

## Status

✅ Experiment Completed Successfully

**Date:** 23 July 2026

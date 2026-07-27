# Experiment E01 Summary

## Experiment Title

Machine Learning Model Comparison for Cyber-Attack Detection

---

## Objective

The objective of this experiment was to compare the performance of several supervised machine learning algorithms for multi-class cyber-attack detection using the complete feature set (52 features) from the CICIDS2017 dataset.

No feature selection techniques were applied during this experiment to ensure a fair and unbiased comparison among all evaluated algorithms.

---

## Compared Algorithms

- Decision Tree
- Random Forest
- XGBoost
- LightGBM

---

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Training Time
- Prediction Time

---

## Results

| Algorithm | Accuracy | F1-score | Training Time (s) |
|-----------|----------|----------|-------------------|
| Decision Tree | 99.22% | 99.22% | 1.147 |
| Random Forest | 99.51% | 99.51% | 11.761 |
| XGBoost | **99.71%** | **99.71%** | **3.319** |
| LightGBM | **99.71%** | **99.71%** | 7.774 |

---

## Key Findings

- All evaluated algorithms achieved excellent classification performance using the complete feature set.
- XGBoost and LightGBM achieved the highest predictive performance with identical Accuracy and F1-score.
- XGBoost required significantly less training time than LightGBM while maintaining the same classification performance.
- Random Forest achieved strong predictive performance but required the longest training time.
- Decision Tree provided the fastest and simplest model but produced the lowest overall classification performance.

---

## Final Decision

Although XGBoost and LightGBM achieved identical predictive performance, XGBoost was selected as the baseline model for the remaining experiments because it provided equivalent classification accuracy with substantially lower training time.

The selected XGBoost model will be further investigated through feature selection, hyperparameter optimization, SHAP-based explainability, and integration into the proposed Flask web application.

---

## Output Files

- comparison_results.csv
- metrics_table.xlsx
- trained_models/
- figures/
- confusion_matrices/
- label_encoder.pkl
- feature_names.pkl

---

## Status

✅ Experiment Completed Successfully

**Date:** 16/07/2026
# Experiment E03 Summary

## Experiment Title

Hyperparameter Optimization of XGBoost

---

## Objective

Improve the predictive performance of the baseline XGBoost classifier through hyperparameter optimization using RandomizedSearchCV.

---

## Optimization Method

RandomizedSearchCV

Cross Validation:
5-fold

Iterations:
50

Evaluation Metric:
Weighted F1-score

---

## Best Hyperparameters

The optimal hyperparameters obtained from RandomizedSearchCV are stored in:

best_parameters.json

---

## Performance Comparison

| Metric | Baseline | Optimized | Improvement |
|---------|----------|-----------|-------------|
| Accuracy | 99.7555% | **99.8166%** | ↑ +0.0613% |
| Precision | 99.7556% | **99.8163%** | ↑ +0.0608% |
| Recall | 99.7555% | **99.8166%** | ↑ +0.0613% |
| F1-score | 99.7553% | **99.8161%** | ↑ +0.0610% |
| Training Time | 2.495 s | 2.542 s | ↑ +0.047 s |
| Prediction Time | 0.04966 s | **0.04904 s** | ↓ Faster |

---

## Key Findings

- Hyperparameter optimization produced consistent improvements across all classification metrics.
- The optimized model achieved the highest overall predictive performance.
- Training time increased only slightly due to the more complex optimized model.
- Prediction time remained almost identical to the baseline model.
- The experimental protocol avoided Data Leakage by performing feature selection only on the training set.

---

## Final Decision

The optimized XGBoost model is selected as the final classifier for integration into the proposed intelligent web-based cyber-attack detection system.

This optimized model will be deployed within the Flask web application and subsequently interpreted using SHAP explainability techniques.

---

## Output Files

baseline_results.csv

optimized_results.csv

comparison_results.csv

best_parameters.json

trained_models/

figures/

confusion_matrices/

---

## Status

Completed Successfully

Date:
22 July 2026
# Experiment E02 Summary

## Experiment Title

Feature Selection Using Random Forest Feature Importance

---

## Objective

Evaluate different feature subsets to determine whether dimensionality reduction can preserve the predictive performance of the selected XGBoost model while improving computational efficiency.

---

## Feature Selection Method

Random Forest Feature Importance

---

## Evaluated Feature Sets

- All Features (52)
- Top 30
- Top 25
- Top 20
- Top 15

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

| Feature Set | Accuracy | Training Time (s) |
|-------------|----------|-------------------:|
| All Features | **99.71%** | 2.913 |
| Top 30 | **99.71%** | **1.742** |
| Top 25 | 99.62% | 1.592 |
| Top 20 | 99.53% | 1.343 |
| Top 15 | 99.54% | 1.236 |

---

## Key Findings

- The Top 30 feature subset achieved identical predictive performance to the complete feature set.
- Reducing the number of features from 52 to 30 reduced the training time by approximately **40%** without affecting the classification accuracy.
- Further feature reduction (Top 25, Top 20 and Top 15) slightly decreased the predictive performance.
- Random Forest feature importance proved effective for identifying the most informative features while preserving model performance.

---

## Final Decision

The **Top 30 feature subset** was selected as the optimal feature set because it preserved the highest predictive performance while significantly reducing computational cost.

The selected feature subset will be used in **Experiment 03 (Hyperparameter Optimization)**.

---

## Output Files

- feature_importance.csv
- selected_features.csv
- feature_selection_results.csv
- metrics_table.xlsx
- trained_models/
- figures/
- confusion_matrices/

---

## Status

✅ Experiment Completed Successfully

Date: 16/07/2026
# Experiment Notes

## Experiment Information

Experiment ID:
E03_HyperparameterOptimization

Date:
16 July 2026

Status:
Completed

---

## Objective

Optimize the hyperparameters of the baseline XGBoost model in order to improve its classification performance while maintaining efficient computational cost.

---

## Dataset

Dataset:
CICIDS2017 (Cleaned)

Target:
Attack Type

Number of Features:
52

Selected Feature Subset:
Top 30

---

## Methodology

The experiment follows the same preprocessing pipeline used in previous experiments.

Important methodological decisions:

- Train/Test Split was performed before feature selection.
- Random Forest Feature Importance was calculated using only the training set.
- Top 30 features were selected according to their importance scores.
- The same training and testing partitions were used for both baseline and optimized models to ensure a fair comparison.
- Hyperparameter optimization was performed using RandomizedSearchCV with five-fold cross validation.

---

## Hyperparameter Optimization

Search Method:
RandomizedSearchCV

Cross Validation:
5-fold

Number of Iterations:
50

Evaluation Metric:
Weighted F1-score

---

## Observations

- Hyperparameter optimization slightly improved all classification metrics.
- The optimized model achieved higher Accuracy, Precision, Recall and F1-score.
- Prediction time remained almost unchanged.
- Training time increased slightly due to the optimized model complexity.
- No Data Leakage occurred during feature selection.

---

## Conclusion

The optimized XGBoost model will be adopted as the final classifier for the proposed intelligent cyber-attack detection system.
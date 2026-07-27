# Experiment E03

## Title

Hyperparameter Optimization of XGBoost for Cyber-Attack Detection

---

## Objective

The objective of this experiment is to improve the predictive performance of the baseline XGBoost classifier by optimizing its hyperparameters using Randomized Search Cross Validation.

---

## Methodology

The experiment follows the same preprocessing pipeline adopted in the previous experiments.

Pipeline:

Load Dataset

↓

Balanced Sampling

↓

Label Encoding

↓

Train/Test Split

↓

Random Forest Feature Importance

↓

Top 30 Feature Selection

↓

Baseline XGBoost

↓

RandomizedSearchCV

↓

Optimized XGBoost

↓

Performance Comparison

---

## Optimization Method

RandomizedSearchCV

Cross Validation: 5-fold

Iterations: 50

Evaluation Metric:

Weighted F1-score

---

## Outputs

trained_models/

confusion_matrices/

figures/

baseline_results.csv

optimized_results.csv

comparison_results.csv

best_parameters.json

feature_importance.csv

selected_features.csv

label_encoder.pkl

feature_names.pkl

---

## Status

Completed Successfully
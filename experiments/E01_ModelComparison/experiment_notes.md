# Experiment Notes

## Experiment Information

**Experiment ID:** E01_ModelComparison

**Experiment Title:** Machine Learning Model Comparison

**Date:** 16 July 2026

**Status:** Completed

---

## Objective

To compare the performance of four supervised machine learning algorithms for multi-class cyber-attack detection using the complete feature set extracted from the CICIDS2017 dataset.

This experiment aims to establish a reliable baseline model before performing feature selection and hyperparameter optimization.

---

## Experimental Setup

### Dataset

- Dataset: CICIDS2017 (Cleaned)
- Number of Features: 52
- Target Variable: Attack Type

### Compared Algorithms

- Decision Tree
- Random Forest
- XGBoost
- LightGBM

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Training Time
- Prediction Time

---

## Methodology

- All available features (52) were used.
- No feature selection technique was applied.
- The dataset was divided into training and testing sets before model training.
- All algorithms were trained and evaluated using the same train/test split to ensure a fair comparison.

---

## Observations

- XGBoost and LightGBM achieved the highest classification performance.
- XGBoost reached the same predictive performance as LightGBM while requiring considerably less training time.
- Random Forest produced competitive results but required the longest training time among the evaluated models.
- Decision Tree provided the simplest model and the fastest prediction time but achieved the lowest overall predictive performance.

---

## Conclusion

This experiment establishes the baseline performance of the evaluated machine learning algorithms.

Based on the obtained results, XGBoost was selected as the baseline model for the subsequent experiments due to its excellent balance between predictive performance and computational efficiency.

Feature selection will be investigated separately in Experiment 02 using the selected baseline model.
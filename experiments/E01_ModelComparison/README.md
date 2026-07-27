# Experiment 01 – Machine Learning Model Comparison

## Objective

The objective of this experiment is to compare several supervised machine learning algorithms for cyber attack detection using the CICIDS2017 dataset.

Unlike the previous exploratory experiments, this experiment uses all available features (52 features) to ensure a fair comparison between algorithms before applying any feature selection techniques.

## Dataset

- Dataset: CICIDS2017 (Cleaned Version)
- Number of Features: 52
- Target Variable: Attack Type

## Compared Algorithms

- Decision Tree
- Random Forest
- XGBoost
- LightGBM

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Training Time
- Prediction Time

## Output Files

comparison_results.csv

metrics_table.xlsx

trained_models/

figures/

confusion_matrices/

label_encoder.pkl

feature_names.pkl

## Conclusion

The purpose of this experiment is to identify the most suitable machine learning algorithm that will be used in the following experiments.
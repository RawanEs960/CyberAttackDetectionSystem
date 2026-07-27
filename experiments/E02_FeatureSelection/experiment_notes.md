# Experiment Notes

## Experiment Information

Experiment ID:
E02_FeatureSelection

Date:
16 July 2026

Status:
Completed

---

## Objective

Investigate the impact of feature selection on the predictive performance and computational efficiency of the selected XGBoost model.

---

## Methodology

- The dataset was loaded, sampled, and label encoded.
- The dataset was split into training and testing sets before feature selection to eliminate data leakage.
- Random Forest was trained exclusively on the training set to compute feature importance scores.
- Five feature subsets were generated:
  - All Features (52)
  - Top 30
  - Top 25
  - Top 20
  - Top 15
- XGBoost was trained independently on each feature subset.
- Each experiment was repeated five times using different random seeds.
- Mean evaluation metrics were calculated and reported.

---

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Training Time
- Prediction Time

---

## Observations

- The Top 30 feature subset achieved the same predictive performance as the complete feature set.
- Training time decreased substantially after reducing the feature space from 52 to 30 features.
- Further reducing the number of features below 30 resulted in a slight decrease in classification performance.
- The feature selection process successfully reduced computational cost while maintaining excellent predictive performance.

---

## Conclusion

The Top 30 feature subset was selected for the next experiment because it achieved identical classification performance to the full feature set while significantly reducing the training time. This subset will be used during the hyperparameter optimization stage.
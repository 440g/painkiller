# Summary of 43_CatBoost_SelectedFeatures

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.025
- **depth**: 8
- **rsm**: 0.9
- **loss_function**: Logloss
- **eval_metric**: Logloss
- **explain_level**: 2

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

43.2 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.614301 | nan         |
| auc       | 0.72019  | nan         |
| f1        | 0.698112 |   0.321224  |
| accuracy  | 0.658615 |   0.505224  |
| precision | 0.923729 |   0.884769  |
| recall    | 1        |   0.0542064 |
| mcc       | 0.317167 |   0.499391  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.614301 |  nan        |
| auc       | 0.72019  |  nan        |
| f1        | 0.653998 |    0.505224 |
| accuracy  | 0.658615 |    0.505224 |
| precision | 0.656207 |    0.505224 |
| recall    | 0.651803 |    0.505224 |
| mcc       | 0.317123 |    0.505224 |


## Confusion matrix (at threshold=0.505224)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |             5967 |             3002 |
| Labeled as 1 |             3061 |             5730 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



[<< Go back](../README.md)

import pandas as pd
import numpy as np
from src.features.pre_processing import pre_process
from src.data.load_bigquery import load_ee_data_from_db
from src.features.feature_engineering import apply_feature_engineering
from src.features.post_processing import remove_non_training_columns
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score, precision_score, f1_score
from sklearn import metrics


def prepare_data_set():
    loan_df = load_ee_data_from_db()
    loan_df = pre_process(loan_df)
    loan_df = apply_feature_engineering(loan_df)
    loan_df = remove_non_training_columns(loan_df)
    return loan_df


def train_test_sets(features_df, target, test_size):
    x_train, x_test, y_train, y_test = train_test_split(features_df, target,
                                                        test_size=test_size,
                                                        random_state=42)
    return x_train, x_test, y_train, y_test


def clf_metrics(features_df, target, clf):
    predictions = np.array(clf.predict(features_df))
    probabilities = clf.predict_proba(features_df)[:, 1]
    print("Confusion matrix on train: \n", pd.crosstab(
        target, predictions,
        rownames=["Actual "],
        colnames=["Predicted "],
    ))
    for metric in [precision_score, recall_score, f1_score]:
        print((metric.__name__ + ": {:.2f}.format(metric(target.values,"
                                 " predictions)"))
    print(" Accuracy: {:.2f}".format(metrics.accuracy_score(target,
                                                            predictions)))
    fpr, tpr, thresholds = metrics.roc_curve(target, probabilities,
                                             pos_label=1)
    print((" AUC:", metrics.auc(fpr, tpr)))
    print((" Gini:", 2 * metrics.auc(fpr, tpr)))
    print("End of Classifier Metrics Results")

import pandas as pd
from src.models import utils
from src.data_transform.data_transform import one_hot_encode_df
from src.config.model_constants import PARAMETERS
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


def random_forest_tuning(x_train, y_train):
    rfc = RandomForestClassifier(random_state=1)
    cv_rfc = GridSearchCV(estimator=rfc, param_grid=PARAMETERS, cv=10)
    cv_rfc.fit(x_train, y_train)
    return cv_rfc


def random_forest_model():
    rf = RandomForestClassifier(
        random_state=1,
        criterion="entropy",
        max_depth=12,
        max_features="auto",
        n_estimators=300,
        min_samples_leaf=30,
        class_weight="balanced",
        n_jobs=1
    )
    return rf


def feature_importance(rf, x_train):
    df = pd.DataFrame(
        rf.feature_importances_, index=x_train.columns,
        columns=["importance"]).sort_values("importance", ascending=False)
    return df


if __name__ == "main":
    loan_df = utils.prepare_data_set()
    loan_df = one_hot_encode_df(loan_df)
    print(loan_df.head(4))
    # x, y = utils.train_test_sets(loan_df, 0.25)
    # check = random_forest_tuning(x, y)
    # print(check.best_params_)
    # rfm = random_forest_model()
    # rfm.fit(x, y)


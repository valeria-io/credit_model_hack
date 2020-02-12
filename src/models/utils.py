from src.features.pre_processing import pre_process
from src.data.load_bigquery import load_ee_data_from_db
from src.features.feature_engineering import apply_feature_engineering
from src.features.post_processing import post_process
from sklearn.model_selection import train_test_split
import pandas as pd


def prepare_dataset():
    loan_df = load_ee_data_from_db()
    loan_df = pre_process(loan_df)
    loan_df = apply_feature_engineering(loan_df)
    loan_df = post_process(loan_df)
    return loan_df


def train_test_split(df, test_size):
    train, test = train_test_split(df, test_size)
    return train, test


def category_to_numerical(df):
    df = df.copy()
    columns = []
    for col_name in df.columns:
        if df[col_name].dtype == 'object' and len(df[col_name].value_counts()) > 2:
            df[col_name] = df[col_name].astype('category')
            columns.append(col_name)
    df.CreditScoreEsMicroL.replace({'M': True}, {'Non-M': False})
    df = pd.get_dummies(df, columns=columns)
    return df

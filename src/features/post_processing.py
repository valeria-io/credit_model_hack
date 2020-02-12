import pandas as pd
import numpy as np
from src.config.data_constants import EXCLUDE_COLUMNS
from src.data.load_bigquery import load_ee_data_from_db
from src.features.pre_processing import pre_process
from src.features.feature_engineering import apply_feature_engineering


def remove_non_training_columns(df: pd.DataFrame):
    df = df.copy()
    df = df.drop(columns=list(EXCLUDE_COLUMNS))
    return df


def fill_missing_values(df: pd.DataFrame):
    df = df.copy()

    numerical_columns = df.select_dtypes(include=['number']).columns
    categorical_columns = df.select_dtypes(include=['category', 'object', 'bool']).columns

    df[numerical_columns] = df[numerical_columns].fillna(df[numerical_columns].median())
    df[categorical_columns] = df[categorical_columns].replace({np.nan: 'NaN'})

    return df


def post_process(df: pd.DataFrame):
    df = df.copy()
    df = remove_non_training_columns(df)
    df = fill_missing_values(df)

    return df


if __name__ == "__main__":
    loan_df = load_ee_data_from_db()
    loan_df = pre_process(loan_df)
    loan_df = apply_feature_engineering(loan_df)
    loan_df = post_process(loan_df)


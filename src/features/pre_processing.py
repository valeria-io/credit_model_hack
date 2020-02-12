import numpy as np
import pandas as pd

from src.config.data_constants import (
    REPLACE_VALUES,
    OUTLIERS,
    COLUMNS,
    REPLACE_NAN,
    NEW_COLUMNS,
)
from src.data.load_bigquery import load_ee_data_from_db


def replace_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.replace(REPLACE_VALUES)
    return df


def remove_outliers(df: pd.DataFrame):
    df = df.copy()
    df = df.drop(list(OUTLIERS))
    return df


def format_column_types(df: pd.DataFrame):
    df = df.copy()
    df[COLUMNS.DATE_OF_BIRTH] = pd.to_datetime(
        df[COLUMNS.DATE_OF_BIRTH], format="%Y-%m-%d"
    )
    df[COLUMNS.CREDIT_SCORE_EE_MINI] = df[COLUMNS.CREDIT_SCORE_EE_MINI].astype(str)
    return df


def format_nan(df: pd.DataFrame):
    df = df.copy()
    df = df.replace(to_replace=["", None], value=np.nan)
    return df


def fill_early_loans(df: pd.DataFrame):
    df = df.copy()
    df.loc[
        (df[COLUMNS.PREVIOUS_REPAYMENTS_BEFORE_LOAN].isnull())
        & (df[COLUMNS.NO_OF_PREVIOUS_LOANS_BEFORE_LOAN] == 0),
        COLUMNS.PREVIOUS_REPAYMENTS_BEFORE_LOAN,
    ] = 0

    df.loc[
        (df[COLUMNS.PREVIOUS_EARLY_REPAYMENTS_BEFOLE_LOAN].isnull())
        & (df[COLUMNS.PREVIOUS_EARLY_REPAYMENTS_COUNT_BEFORE_LOAN] == 0),
        COLUMNS.PREVIOUS_EARLY_REPAYMENTS_BEFOLE_LOAN,
    ] = 0

    return df


def replace_nan_values_in_categories(df):
    df = df.copy()
    df = df.replace(REPLACE_NAN)
    return df


def add_perc_nan_per_row(df: pd.DataFrame):
    df = df.copy()
    df[NEW_COLUMNS.NAN_PERC_PER_ROW] = df.isnull().sum(axis=1) / df.shape[1]
    #@todo: move labels and bins to constants
    df[NEW_COLUMNS.NAN_LEVEL] = pd.cut(
        df[NEW_COLUMNS.NAN_PERC_PER_ROW],
        [-1, 0, 0.02, 0.05, 0.1, 0.2, 0.5, 1],
        labels=["None", "Minimal", "Low", "Low/Med", "Med", "Med/High", "High"],
        right=True,
    )
    return df


def pre_process(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = replace_values(df)
    df = format_nan(df)
    df = remove_outliers(df)
    df = format_column_types(df)
    df = fill_early_loans(df)
    df = add_perc_nan_per_row(df)
    df = replace_nan_values_in_categories(df)
    return df


if __name__ == "__main__":
    loan_df = load_ee_data_from_db()
    loan_df = pre_process(loan_df)

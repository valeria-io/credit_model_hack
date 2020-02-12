import pandas as pd
from src.config.data_constants import EXCLUDE_COLUMNS


def remove_non_training_columns(df: pd.DataFrame):
    df = df.copy()
    df = df.drop(columns=list(EXCLUDE_COLUMNS))
    return df

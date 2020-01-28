import pandas as pd
import numpy as np

from src.config.data_constants import REPLACE_VALUES
from src.data.load_data import load_raw_data

def replace_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.replace(REPLACE_VALUES)
    return df


if __name__ == '__main__':
    raw_df = load_raw_data()
    df = replace_values(raw_df)
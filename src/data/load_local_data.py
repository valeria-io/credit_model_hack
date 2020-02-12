import pandas as pd
from src.config.data_constants import COLUMNS
from src.config.paths_constants import RAW_DATA_PATH


def load_raw_data_from_csv():
    df = pd.read_csv(RAW_DATA_PATH, low_memory=False, usecols=COLUMNS)
    df = df.set_index([COLUMNS.LOAN_NUMBER], drop=True)
    return df


if __name__ == "__main__":
    loan_df = load_raw_data_from_csv()

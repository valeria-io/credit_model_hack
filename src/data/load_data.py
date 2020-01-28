import pandas as pd
from src.config.data_constants import COLUMNS
from src.config.paths_constants import RAW_DATA_PATH

def load_raw_data():

    df = pd.read_csv(RAW_DATA_PATH, low_memory=True)

    return df[list(COLUMNS)]


if __name__ == "__main__":
    df = load_raw_data()
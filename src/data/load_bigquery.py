import google.auth
from google.cloud import bigquery, bigquery_storage
from src.config.data_constants import COLUMNS
from src.config.table_names import (
    BONDORA_RAW_TABLE_NAME,
    BONDORA_EE_FILTERED_TABLE_NAME,
)
import pandas as pd


def read_from_db(query: str) -> pd.DataFrame:
    credentials, project_id = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    client = bigquery.Client(credentials=credentials, project=project_id)
    bqstorage_client = bigquery_storage.BigQueryStorageClient(credentials=credentials)
    df = client.query(query).to_dataframe(bqstorage_client=bqstorage_client)

    return df


# @todo: write test
def load_raw_data_from_db() -> pd.DataFrame:
    query = "SELECT * FROM {}".format(BONDORA_RAW_TABLE_NAME)
    df = read_from_db(query)
    return df


# @todo: write test
def load_ee_data_from_db() -> pd.DataFrame:
    features = ", ".join(COLUMNS)
    query = "SELECT {} FROM {}".format(features, BONDORA_EE_FILTERED_TABLE_NAME)
    df = read_from_db(query)
    return df


if __name__ == "__main__":
    loan_df = load_ee_data_from_db()

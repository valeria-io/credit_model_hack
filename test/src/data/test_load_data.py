from src.config.data_constants import COLUMNS
from src.data.load_local_data import load_raw_data_from_csv
import pytest


@pytest.fixture(scope="class")
def get_raw_dataset():
    raw_data = load_raw_data_from_csv()
    yield raw_data


class TestLoadRawData:
    def test_columns(self, get_raw_dataset):
        expected_columns = list(COLUMNS)
        actual_columns = list(get_raw_dataset.reset_index().columns)
        assert expected_columns == actual_columns

    def test_dataset_size(self, get_raw_dataset):
        expected_size = (134414, 46)
        actual_size = get_raw_dataset.shape
        assert expected_size == actual_size

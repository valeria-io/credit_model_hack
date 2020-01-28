from src.config.data_constants import COLUMNS
from src.data.load_data import load_raw_data
import pytest

@pytest.fixture(scope='class')
def get_raw_dataset():
    raw_data = load_raw_data()
    yield raw_data


class TestLoadRawData(object):
    def test_columns(self, get_raw_dataset):
        expected_columns = list(COLUMNS)
        actual_columns = list(get_raw_dataset.columns)
        assert expected_columns == actual_columns

    def test_dataset_size(self, get_raw_dataset):
        expected_size = (134414, 50)
        actual_size = get_raw_dataset.shape
        assert expected_size == actual_size
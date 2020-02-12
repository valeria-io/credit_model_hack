import pandas as pd
import pytest

from src.config.data_constants import EXCLUDE_COLUMNS, COLUMNS
from src.features.post_processing import remove_non_training_columns
from pandas.util.testing import assert_frame_equal


@pytest.fixture(scope="module")
def test_data():
    columns = list(EXCLUDE_COLUMNS) + [COLUMNS.INCOME_TOTAL]
    testing_data = pd.DataFrame(columns=columns, data=[[1] * len(columns)])
    yield testing_data


def test_remove_non_training_columns(test_data):
    actual = remove_non_training_columns(test_data)
    expected = pd.DataFrame({COLUMNS.INCOME_TOTAL: [1]})
    assert_frame_equal(actual, expected)

import pytest
import pandas as pd
from src.config.data_constants import COLUMNS, NEW_COLUMNS
from src.features.feature_engineering import create_percentage_from_income, add_birthday_details
from pandas.util.testing import assert_frame_equal


@pytest.fixture()
def get_raw_df():
    raw_df = pd.DataFrame(
        {
            COLUMNS.INCOME_TOTAL: [90.0, 150.0, 149.1313, 300.0, 105.5],
            COLUMNS.INCOME_FROM_PRINCIPAL_EMPLOYER: [45.0, 50.0, 0, 400, 105.5],
            COLUMNS.INCOME_FROM_PENSION: [45.0, 50.0, 0, 400, 105.5],
            COLUMNS.INCOME_FROM_SOCIAL_WELFARE: [45.0, 50.0, 0, 400, 105.5],
            COLUMNS.INCOME_FROM_LEAVE_PAY: [45.0, 50.0, 0, 400, 105.5],
            COLUMNS.INCOME_FROM_CHILD_SUPPORT: [45.0, 50.0, 0, 400, 105.5],
            COLUMNS.INCOME_OTHER: [45.0, 50.0, 0, 400, 105.5],
            COLUMNS.INCOME_FROM_FAMILY_ALLOWANCE: [45.0, 50.0, 0, 400, 105.5],
        }
    )
    yield raw_df


def test_create_percentage_from_income(get_raw_df):
    actual = create_percentage_from_income(get_raw_df)

    expected_values = [
        45.0 / 90.0,
        50.0 / 150.0,
        0 / 149.1313,
        400 / 300.0,
        105.5 / 105.5,
    ]

    expected = get_raw_df
    expected[NEW_COLUMNS.PERC_PRINCIPAL_EMPLOYER_FROM_TOTAL_INCOME] = expected_values
    expected[NEW_COLUMNS.PERC_PENSION_FROM_TOTAL_INCOME] = expected_values
    expected[NEW_COLUMNS.PERC_SOCIAL_WELFARE_FROM_TOTAL_INCOME] = expected_values
    expected[NEW_COLUMNS.PERC_LEAVE_PAY_FROM_TOTAL_INCOME] = expected_values
    expected[NEW_COLUMNS.PERC_CHILD_SUPPORT_FROM_TOTAL_INCOME] = expected_values
    expected[NEW_COLUMNS.PERC_OTHER_FROM_TOTAL_INCOME] = expected_values
    expected[NEW_COLUMNS.PERC_FAMILY_ALLOWANCE_FROM_TOTAL_INCOME] = expected_values

    assert_frame_equal(actual, expected)


@pytest.fixture()
def get_birthday_mix():
    birthdays = pd.DataFrame({
        COLUMNS.DATE_OF_BIRTH: pd.to_datetime(['2018-01-01', '1990-10-23', '1980-05-24', '2016-10-02'], format='%Y-%m-%d')
    })
    yield birthdays

@pytest.fixture()
def get_birthday_single():
    birthdays = pd.DataFrame({
        COLUMNS.DATE_OF_BIRTH: pd.to_datetime(['2018-01-01', '1990-10-09', '1980-05-02', '2016-10-02'], format='%Y-%m-%d')
    })
    yield birthdays


class TestAddBirthdayDetails:
    def test_add_birthday_mix(self, get_birthday_mix):
        actual = add_birthday_details(get_birthday_mix)
        expected = pd.DataFrame({
            COLUMNS.DATE_OF_BIRTH: pd.to_datetime(['2018-01-01', '1990-10-23', '1980-05-24', '2016-10-02'], format='%Y-%m-%d'),
            NEW_COLUMNS.YEAR_OF_BIRTH: [2018, 1990, 1980, 2016],
            NEW_COLUMNS.MONTH_OF_BIRTH: [1, 10, 5, 10]
        })
        assert_frame_equal(actual, expected)

    def test_add_birthday_single(self, get_birthday_single):
        actual = add_birthday_details(get_birthday_single)
        expected = pd.DataFrame({
            COLUMNS.DATE_OF_BIRTH: pd.to_datetime(['2018-01-01', '1990-10-09', '1980-05-02', '2016-10-02'], format='%Y-%m-%d'),
            NEW_COLUMNS.YEAR_OF_BIRTH: [2018, 1990, 1980, 2016],
            NEW_COLUMNS.MONTH_OF_BIRTH: [1, 10, 5, 10]
        })
        assert_frame_equal(actual, expected)

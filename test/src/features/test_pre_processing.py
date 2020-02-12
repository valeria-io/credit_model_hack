import pytest
import pandas as pd
import numpy as np
from src.config.data_constants import COLUMNS, NEW_COLUMNS
from src.features.pre_processing import (
    replace_values,
    remove_outliers,
    format_nan,
    fill_early_loans,
    format_column_types,
    add_perc_nan_per_row,
    replace_nan_values_in_categories,
)
from pandas.util.testing import assert_frame_equal


@pytest.fixture(name="test_data")
def get_raw_data_for_testing():
    testing_raw_data = pd.DataFrame(
        {
            COLUMNS.LOAN_NUMBER: [2383, 573, 979, 6231, 12741, 37948, 100, 200],
            COLUMNS.OCCUPATION_AREA: [1.0, 2.0, 12.0, 19.0, 0.0, -1.0, np.nan, 1],
            COLUMNS.EMPLOYMENT_STATUS: [1.0, 2.0, 3.0, 6.0, 0.0, -1.0, np.nan, 1],
            COLUMNS.MARITAL_STATUS: [1.0, 2.0, 3.0, 5.0, 0.0, -1.0, np.nan, 1],
            COLUMNS.EDUCATION: [1.0, 2.0, 3.0, 5.0, 0.0, -1.0, np.nan, 1],
            COLUMNS.USE_OF_LOAN: [1, 2, 3, 5, 0, -1, np.nan, 1],
            COLUMNS.GENDER: [1.0, 1.0, 1.0, 2.0, 0.0, -1.0, np.nan, 1],
            COLUMNS.VERIFICATION_TYPE: [1.0, 2.0, 3.0, 5.0, 0.0, -1.0, np.nan, 1],
            COLUMNS.LANGUAGE_CODE: [1, 2, 13, 15, 22, -1, np.nan, 3],
            COLUMNS.HOME_OWNERSHIP_TYPE: [1, 2, 3, 5, 0, -1, np.nan, 1],
            COLUMNS.AGE: [1, 2, 3, 4, 0, -1, np.nan, 1],
        }
    )
    testing_raw_data = testing_raw_data.set_index(COLUMNS.LOAN_NUMBER)

    yield testing_raw_data


@pytest.mark.parametrize(
    "colname, expected",
    [
        (
            COLUMNS.OCCUPATION_AREA,
            [
                "Other",
                "Mining",
                "Real-estate",
                "Agriculture, forestry and fishing",
                np.nan,
                np.nan,
                np.nan,
                "Other",
            ],
        ),
        (
            COLUMNS.EMPLOYMENT_STATUS,
            [
                "Unemployed",
                "Partially Employed",
                "Fully Employed",
                "Retiree",
                np.nan,
                np.nan,
                np.nan,
                "Unemployed",
            ],
        ),
        (
            COLUMNS.MARITAL_STATUS,
            [
                "Married",
                "Cohabitant",
                "Single",
                "Widow",
                np.nan,
                np.nan,
                np.nan,
                "Married",
            ],
        ),
        (
            COLUMNS.EDUCATION,
            [
                "Primary",
                "Basic",
                "Vocational",
                "Higher",
                np.nan,
                np.nan,
                np.nan,
                "Primary",
            ],
        ),
        (
            COLUMNS.USE_OF_LOAN,
            [
                "Real Estate",
                "Home Improvement",
                "Business",
                "Travel",
                "Loan Consolidation",
                np.nan,
                np.nan,
                "Real Estate",
            ],
        ),
        (
            COLUMNS.GENDER,
            ["Woman", "Woman", "Woman", np.nan, "Male", -1.0, np.nan, "Woman"],
        ),
        (
            COLUMNS.VERIFICATION_TYPE,
            [
                "Income Unverified",
                "Cross-Ref by Phone",
                "Income Verified",
                5.0,
                np.nan,
                -1.0,
                np.nan,
                "Income Unverified",
            ],
        ),
        (
            COLUMNS.LANGUAGE_CODE,
            ["Estonian", "Other", np.nan, np.nan, np.nan, -1, np.nan, "Russian"],
        ),
        (
            COLUMNS.HOME_OWNERSHIP_TYPE,
            [
                "Owner",
                "Living with parents",
                "Tenant, pre-furnished property",
                "Other",
                "Other",
                np.nan,
                np.nan,
                "Owner",
            ],
        ),
        (COLUMNS.AGE, [np.nan, np.nan, 3, 4, np.nan, -1, np.nan, np.nan]),
    ],
    ids=[
        COLUMNS.OCCUPATION_AREA,
        COLUMNS.EMPLOYMENT_STATUS,
        COLUMNS.MARITAL_STATUS,
        COLUMNS.EDUCATION,
        COLUMNS.USE_OF_LOAN,
        COLUMNS.GENDER,
        COLUMNS.VERIFICATION_TYPE,
        COLUMNS.LANGUAGE_CODE,
        COLUMNS.HOME_OWNERSHIP_TYPE,
        COLUMNS.AGE,
    ],
)
def test_replace_values(colname, expected, test_data):
    expected = pd.DataFrame(
        {
            colname: expected,
            COLUMNS.LOAN_NUMBER: [2383, 573, 979, 6231, 12741, 37948, 100, 200],
        }
    )
    expected = expected.set_index(COLUMNS.LOAN_NUMBER)
    actual = replace_values(test_data[[colname]])
    assert_frame_equal(actual, expected)


def test_remove_outliers(test_data):
    actual = remove_outliers(
        test_data[
            [COLUMNS.OCCUPATION_AREA, COLUMNS.EMPLOYMENT_STATUS, COLUMNS.MARITAL_STATUS]
        ]
    )
    #@todo - move it out
    expected = pd.DataFrame(
        {
            COLUMNS.LOAN_NUMBER: [100, 200],
            COLUMNS.OCCUPATION_AREA: [np.nan, 1],
            COLUMNS.EMPLOYMENT_STATUS: [np.nan, 1],
            COLUMNS.MARITAL_STATUS: [np.nan, 1],
        }
    )
    expected = expected.set_index(COLUMNS.LOAN_NUMBER)

    assert_frame_equal(actual, expected)


@pytest.fixture()
def get_nan_df():
    nan_df = pd.DataFrame(
        {"col1": [None, np.nan, "", 2], "col2": [np.nan, None, None, 5]}
    )
    yield nan_df


def test_format_nan(get_nan_df):
    expected = pd.DataFrame(
        {"col1": [np.nan, np.nan, np.nan, 2], "col2": [np.nan, np.nan, np.nan, 5]}
    )
    actual = format_nan(get_nan_df)
    assert_frame_equal(expected, actual)


@pytest.fixture()
def get_early_loans():
    early_loans = pd.DataFrame(
        {
            COLUMNS.PREVIOUS_REPAYMENTS_BEFORE_LOAN: [np.nan, np.nan, 10, 20],
            COLUMNS.NO_OF_PREVIOUS_LOANS_BEFORE_LOAN: [0, 10, 0, 1],
            COLUMNS.PREVIOUS_EARLY_REPAYMENTS_BEFOLE_LOAN: [np.nan, 10, 20, np.nan],
            COLUMNS.PREVIOUS_EARLY_REPAYMENTS_COUNT_BEFORE_LOAN: [0, 1, 0, 10],
        }
    )
    return early_loans


def test_fill_early_loans(get_early_loans):
    expected = pd.DataFrame(
        {
            COLUMNS.PREVIOUS_REPAYMENTS_BEFORE_LOAN: [0, np.nan, 10, 20],
            COLUMNS.NO_OF_PREVIOUS_LOANS_BEFORE_LOAN: [0, 10, 0, 1],
            COLUMNS.PREVIOUS_EARLY_REPAYMENTS_BEFOLE_LOAN: [0, 10, 20, np.nan],
            COLUMNS.PREVIOUS_EARLY_REPAYMENTS_COUNT_BEFORE_LOAN: [0, 1, 0, 10],
        }
    )
    actual = fill_early_loans(get_early_loans)
    assert_frame_equal(expected, actual)


@pytest.fixture()
def get_data_with_nulls():
    list_100 = np.arange(100)
    data_with_nulls = pd.DataFrame(
        columns=np.arange(100),
        data=[
            list_100,
            np.place(list_100, list_100 <= 2, np.nan),
            list(np.arange(96)) + [np.nan] * 4,
            list(np.arange(90)) + [np.nan] * 10,
            list(np.arange(85)) + [np.nan] * 15,
            list(np.arange(60)) + [np.nan] * 40,
            list(np.arange(20)) + [np.nan] * 80,
            [np.nan] * 100,
        ],
    )
    yield data_with_nulls


def test_add_perc_nan_per_row(get_data_with_nulls):
    expected = get_data_with_nulls.merge(
        pd.DataFrame(
            {
                NEW_COLUMNS.NAN_PERC_PER_ROW: [
                    0,
                    2 / 100,
                    4 / 100,
                    10 / 100,
                    15 / 100,
                    40 / 100,
                    80 / 100,
                    100 / 100,
                ],
                NEW_COLUMNS.NAN_LEVEL: [
                    "None",
                    "Minimal",
                    "Low",
                    "Low/Med",
                    "Med",
                    "Med/High",
                    "High",
                    "High",
                ],
            }
        ),
        how="inner",
        left_index=True,
        right_index=True,
    )
    expected[NEW_COLUMNS.NAN_LEVEL] = pd.Categorical(
        expected[NEW_COLUMNS.NAN_LEVEL],
        categories=["None", "Minimal", "Low", "Low/Med", "Med", "Med/High", "High"],
        ordered=True,
    )
    actual = add_perc_nan_per_row(get_data_with_nulls)

    assert_frame_equal(expected, actual)


@pytest.fixture()
def get_unformatted_data():
    unformatted_data = pd.DataFrame(
        {
            COLUMNS.DATE_OF_BIRTH: ["1990-10-23", "1980-05-24"],
            COLUMNS.CREDIT_SCORE_EE_MINI: [100, 200],
        }
    )
    yield unformatted_data


def test_format_column_types(get_unformatted_data):
    expected = pd.DataFrame(
        {
            COLUMNS.DATE_OF_BIRTH: [
                pd.to_datetime("1990-10-23"),
                pd.to_datetime("1980-05-24"),
            ],
            COLUMNS.CREDIT_SCORE_EE_MINI: ["100", "200"],
        }
    )
    actual = format_column_types(get_unformatted_data)

    assert_frame_equal(actual, expected)





def test_replace_nan_values_in_categories(get_nan_in_cat_columns):
    expected = pd.DataFrame(
        {
            COLUMNS.VERIFICATION_TYPE: [
                "Income Unverified",
                "Income Unverified",
                "Verified",
            ],
            COLUMNS.GENDER: ["Male", "Male", "Female"],
            COLUMNS.EDUCATION: ["Basic", "Other", "Basic"],
            COLUMNS.CREDIT_SCORE_EE_MINI: ["NaN", "NaN", "100"],
        }
    )
    actual = replace_nan_values_in_categories(get_nan_in_cat_columns)

    assert_frame_equal(expected, actual)

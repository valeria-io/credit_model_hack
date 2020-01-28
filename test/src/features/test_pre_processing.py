import pytest
import pandas as pd
import numpy as np
from src.config.data_constants import COLUMNS
from src.features.pre_processing import replace_values
from pandas.util.testing import assert_frame_equal

@pytest.fixture(scope='class', name='test_data')
def get_raw_data_for_testing():
    testing_raw_data = pd.DataFrame({
        COLUMNS.OCCUPATION_AREA: [1., 2., 12., 19., 0., -1., np.nan, 1],
        COLUMNS.EMPLOYMENT_STATUS: [1., 2., 3., 6., 0., -1., np.nan, 1],
        COLUMNS.MARITAL_STATUS: [1., 2., 3., 5., 0., -1., np.nan, 1],
        COLUMNS.EDUCATION: [1., 2., 3., 5., 0., -1., np.nan, 1],
        COLUMNS.USE_OF_LOAN: [1, 2, 3, 5, 0, -1, np.nan, 1],
        COLUMNS.GENDER: [1., 1., 1., 2., 0., -1., np.nan, 1],
        COLUMNS.VERIFICATION_TYPE: [1., 2., 3., 5., 0., -1., np.nan, 1],
        COLUMNS.LANGUAGE_CODE: [1, 2, 13, 15, 22, -1, np.nan, 9],
        COLUMNS.HOME_OWNERSHIP_TYPE: [1, 2, 3, 5, 0, -1, np.nan, 1],
        COLUMNS.AGE: [1, 2, 3, 4, 0, -1, np.nan, 1]


    })
    yield testing_raw_data

class TestReplaceValues(object):
    def test_occupation_area(self, test_data):
        expected = pd.DataFrame({COLUMNS.OCCUPATION_AREA: ['Other', 'Mining', 'Real-estate', 'Agriculture, forestry and fishing', np.nan, np.nan, np.nan, 'Other']})
        actual = replace_values(test_data[[COLUMNS.OCCUPATION_AREA]])
        assert_frame_equal(actual, expected)

    def test_employment_status(self, test_data):
        expected = pd.DataFrame({COLUMNS.EMPLOYMENT_STATUS: ['Unemployed', 'Partially Employed', 'Fully Employed', 'Retiree', np.nan, np.nan, np.nan, 'Unemployed']})
        actual = replace_values(test_data[[COLUMNS.EMPLOYMENT_STATUS]])
        assert_frame_equal(actual, expected)

    def test_marital_status(self, test_data):
        expected = pd.DataFrame({COLUMNS.MARITAL_STATUS: ['Married', 'Cohabitant', 'Single', 'Widow', np.nan, np.nan, np.nan, 'Married']})
        actual = replace_values(test_data[[COLUMNS.MARITAL_STATUS]])
        assert_frame_equal(actual, expected)

    def test_education(self, test_data):
        expected = pd.DataFrame({COLUMNS.EDUCATION: ['Primary', 'Basic', 'Vocational', 'Higher', np.nan, np.nan, np.nan, 'Primary']})
        actual = replace_values(test_data[[COLUMNS.EDUCATION]])
        assert_frame_equal(actual, expected)

    def test_use_of_loan(self, test_data):
        expected = pd.DataFrame({COLUMNS.USE_OF_LOAN: ['Real Estate', 'Home Improvement', 'Business', 'Travel', 'Loan Consolidation', np.nan, np.nan, 'Real Estate']})
        actual = replace_values(test_data[[COLUMNS.USE_OF_LOAN]])
        assert_frame_equal(actual, expected)

    def test_gender(self, test_data):
        expected = pd.DataFrame({COLUMNS.GENDER: ['Woman', 'Woman', 'Woman', np.nan, 'Male', -1., np.nan, 'Woman']})
        actual = replace_values(test_data[[COLUMNS.GENDER]])
        assert_frame_equal(actual, expected)

    def test_verification_type(self, test_data):
        expected = pd.DataFrame({COLUMNS.VERIFICATION_TYPE: ['Income Unverified', 'Cross-Ref by Phone', 'Income Verified', 5., np.nan, -1., np.nan, 'Income Unverified']})
        actual = replace_values(test_data[[COLUMNS.VERIFICATION_TYPE]])
        assert_frame_equal(actual, expected)

    def test_language(self, test_data):
        expected = pd.DataFrame({COLUMNS.LANGUAGE_CODE: ['Estonian', 'English', np.nan, np.nan, np.nan, -1, np.nan, 'Slovakian']})
        actual = replace_values(test_data[[COLUMNS.LANGUAGE_CODE]])
        assert_frame_equal(actual, expected)

    def test_home_ownership(self, test_data):
        expected = pd.DataFrame({COLUMNS.HOME_OWNERSHIP_TYPE: ['Owner', 'Living with parents', 'Tenant, pre-furnished property','Council house', 'Homeless', np.nan, np.nan, 'Owner']})
        actual = replace_values(test_data[[COLUMNS.HOME_OWNERSHIP_TYPE]])
        assert_frame_equal(actual, expected)

    def test_age(self, test_data):
        expected = pd.DataFrame({COLUMNS.AGE: [np.nan, np.nan, 3, 4, np.nan, -1, np.nan, np.nan]})
        actual = replace_values(test_data[[COLUMNS.AGE]])
        assert_frame_equal(actual, expected)
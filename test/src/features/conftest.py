from src.config.data_constants import COLUMNS
import numpy as np
import pandas as pd
import pytest


@pytest.fixture()
def get_nan_in_cat_columns():
    nan_in_cat_columns_df = pd.DataFrame(
        {
            COLUMNS.VERIFICATION_TYPE: ["Income Unverified", np.nan, "Verified"],
            COLUMNS.GENDER: [np.nan, "Male", "Female"],
            COLUMNS.EDUCATION: ["Basic", "Other", np.nan],
            COLUMNS.CREDIT_SCORE_EE_MINI: [np.nan, np.nan, "100"],
        }
    )
    yield nan_in_cat_columns_df
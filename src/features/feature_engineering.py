import pandas as pd
from src.config.data_constants import NEW_COLUMNS, COLUMNS
from src.features.pre_processing import pre_process
from src.data.load_bigquery import load_ee_data_from_db


def create_percentage_from_income(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df[NEW_COLUMNS.PERC_PRINCIPAL_EMPLOYER_FROM_TOTAL_INCOME] = (
        df[COLUMNS.INCOME_FROM_PRINCIPAL_EMPLOYER] / df[COLUMNS.INCOME_TOTAL]
    )
    df[NEW_COLUMNS.PERC_PENSION_FROM_TOTAL_INCOME] = (
        df[COLUMNS.INCOME_FROM_PENSION] / df[COLUMNS.INCOME_TOTAL]
    )
    df[NEW_COLUMNS.PERC_SOCIAL_WELFARE_FROM_TOTAL_INCOME] = (
        df[COLUMNS.INCOME_FROM_SOCIAL_WELFARE] / df[COLUMNS.INCOME_TOTAL]
    )
    df[NEW_COLUMNS.PERC_LEAVE_PAY_FROM_TOTAL_INCOME] = (
        df[COLUMNS.INCOME_FROM_LEAVE_PAY] / df[COLUMNS.INCOME_TOTAL]
    )
    df[NEW_COLUMNS.PERC_CHILD_SUPPORT_FROM_TOTAL_INCOME] = (
        df[COLUMNS.INCOME_FROM_CHILD_SUPPORT] / df[COLUMNS.INCOME_TOTAL]
    )
    df[NEW_COLUMNS.PERC_OTHER_FROM_TOTAL_INCOME] = (
        df[COLUMNS.INCOME_OTHER] / df[COLUMNS.INCOME_TOTAL]
    )
    df[NEW_COLUMNS.PERC_FAMILY_ALLOWANCE_FROM_TOTAL_INCOME] = (
        df[COLUMNS.INCOME_FROM_FAMILY_ALLOWANCE] / df[COLUMNS.INCOME_TOTAL]
    )
    return df


def add_birthday_details(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df[NEW_COLUMNS.YEAR_OF_BIRTH] = df[COLUMNS.DATE_OF_BIRTH].dt.year
    df[NEW_COLUMNS.MONTH_OF_BIRTH] = df[COLUMNS.DATE_OF_BIRTH].dt.month
    return df


#def

def apply_feature_engineering(df: pd.DataFrame):
    df = create_percentage_from_income(df)
    df = add_birthday_details(df)
    return df


if __name__ == "__main__":
    loan_df = load_ee_data_from_db()
    loan_df = pre_process(loan_df)
    loan_df = apply_feature_engineering(loan_df)

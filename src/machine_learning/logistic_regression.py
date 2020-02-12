import pandas as pd
from src.features.pre_processing import load_ee_data_from_db
from src.features.pre_processing import pre_process
from src.features.feature_engineering import apply_feature_engineering
from src.features.post_processing import post_process

if __name__ == "main":
    loan_df = load_ee_data_from_db()
    loan_df = pre_process(loan_df)
    loan_df = apply_feature_engineering(loan_df)
    loan_df = post_process(loan_df)

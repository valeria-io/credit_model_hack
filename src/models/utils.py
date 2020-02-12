from src.features.pre_processing import pre_process
from src.data.load_bigquery import load_ee_data_from_db
from src.features.feature_engineering import apply_feature_engineering
from src.features.post_processing import remove_non_training_columns
from sklearn.model_selection import train_test_split


def prepare_dataset():
    loan_df = load_ee_data_from_db()
    loan_df = pre_process(loan_df)
    loan_df = apply_feature_engineering(loan_df)
    loan_df = remove_non_training_columns(loan_df)
    return loan_df


def train_test_split(df):
    train, test = train_test_split(df, test_size=0.2)
    return train, test

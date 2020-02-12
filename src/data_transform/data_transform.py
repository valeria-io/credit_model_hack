import pandas as pd


def one_hot_encode_df(df, ignore):
    df_transposed = pd.get_dummies(
        df,
        prefix_sep="_att_",
        dummy_na=True,
        columns=df.drop(ignore, axis=1).select_dtypes(
            exclude=["number", "datetime"]).columns,
    )
    return df_transposed

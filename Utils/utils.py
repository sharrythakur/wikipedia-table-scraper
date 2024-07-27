import pandas as pd


def save_table_to_csv(df, filename):
    df.to_csv(filename, index=False)

import pandas as pd

DATA_FILEPATH = "data/vgsales.csv"


def get_data() -> pd.DataFrame:
    return pd.read_csv(DATA_FILEPATH)

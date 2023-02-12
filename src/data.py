import pandas as pd
import streamlit as st

DATA_FILEPATH = "data/vgsales.csv"


@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv(DATA_FILEPATH)

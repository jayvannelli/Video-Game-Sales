import streamlit as st
from src.data import get_data


def main():
    st.title("Video Game Sales | Kaggle")

    with st.expander("Data source"):
        st.write("https://www.kaggle.com/datasets/thedevastator/global-video-game-sales")

    df = get_data()
    st.dataframe(df)


if __name__ == "__main__":
    main()

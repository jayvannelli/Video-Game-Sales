import streamlit as st
from src.data import get_data

from streamlit_extras.dataframe_explorer import dataframe_explorer


def main():
    st.title("Video Game Sales | Kaggle")

    df = get_data()

    with st.expander("Data source"):
        st.write("https://www.kaggle.com/datasets/thedevastator/global-video-game-sales")

    with st.expander("DataFrame Explorer"):
        filtered_df = dataframe_explorer(df)
        st.dataframe(filtered_df, use_container_width=True)

    st.write("---")

    platform_tab, genre_tab, publisher_tab = st.tabs(
        ["Platform", "Genre", "Publisher"]
    )

    with platform_tab:
        st.subheader("Platform")

        platform = st.selectbox("Select platform", options=df['Platform'].sort_values().unique())
        platform_df = df.loc[df['Platform'] == platform]

        st.dataframe(platform_df)

    with genre_tab:
        st.subheader("Genre")

        genre = st.selectbox("Select genre", options=df['Genre'].sort_values().unique())
        genre_df = df.loc[df['Genre'] == genre]

        st.dataframe(genre_df)

    with publisher_tab:
        st.subheader("Publisher")

        publisher = st.selectbox("Select publisher", options=df['Publisher'].sort_values().unique())
        publisher_df = df.loc[df['Publisher'] == publisher]

        st.dataframe(publisher_df)


if __name__ == "__main__":
    main()

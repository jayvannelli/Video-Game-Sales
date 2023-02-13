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

    overview_tab, platform_tab, genre_tab, publisher_tab = st.tabs(
        ["Overview", "Platform", "Genre", "Publisher"]
    )

    with overview_tab:
        st.subheader("Overview")

        st.bar_chart(df, x="Year", y="Global_Sales")

        left_column, right_column = st.columns(2)
        with left_column:
            st.write("Global sales by genre")
            st.bar_chart(df, x="Genre", y="Global_Sales")
        with right_column:
            st.write("Global sales by platform")
            st.bar_chart(df, x="Platform", y="Global_Sales")

    with platform_tab:
        st.subheader("Platform")

        platform = st.selectbox("Select platform", options=df['Platform'].sort_values().unique())
        platform_df = df.loc[df['Platform'] == platform]

        st.bar_chart(platform_df, x="Year", y="Global_Sales")
        st.bar_chart(platform_df, x="Genre", y="Global_Sales")

        st.dataframe(platform_df)

    with genre_tab:
        st.subheader("Genre")

        genre = st.selectbox("Select genre", options=df['Genre'].sort_values().unique())
        genre_df = df.loc[df['Genre'] == genre]

        st.bar_chart(genre_df, x="Year", y="Global_Sales")
        st.bar_chart(genre_df, x="Platform", y="Global_Sales")

        st.dataframe(genre_df)

    with publisher_tab:
        st.subheader("Publisher")

        publisher = st.selectbox("Select publisher", options=df['Publisher'].sort_values().unique())
        publisher_df = df.loc[df['Publisher'] == publisher]

        st.dataframe(publisher_df)


if __name__ == "__main__":
    main()

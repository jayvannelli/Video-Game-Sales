import streamlit as st
from src.data import get_data

from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.colored_header import colored_header


def main():
    st.set_page_config("Video Game Sales", page_icon="🕹️", layout="wide")
    st.title("Video Game Sales | Kaggle | Streamlit")

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
        colored_header(label="Overview",
                       description="Global sales over time, and broken down by genre & platform.",
                       color_name="blue-70")

        st.write("Global sales over time")
        st.bar_chart(df, x="Year", y="Global_Sales")

        left_column, right_column = st.columns(2)
        with left_column:
            st.write("Global sales by genre")
            st.bar_chart(df, x="Genre", y="Global_Sales")
        with right_column:
            st.write("Global sales by platform")
            st.bar_chart(df, x="Platform", y="Global_Sales")

        st.write("---")
        colored_header(label="Sales by region",
                       description="Sales over time broken down by region.",
                       color_name="red-70")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("North America")
            st.bar_chart(df, x="Year", y="NA_Sales")
        with col2:
            st.write("Europe")
            st.bar_chart(df, x="Year", y="EU_Sales")
        with col3:
            st.write("Japan")
            st.bar_chart(df, x="Year", y="JP_Sales")
        with col4:
            st.write("Other")
            st.bar_chart(df, x="Year", y="Other_Sales")

    with platform_tab:
        colored_header(label="Platform",
                       description="Best selling video games by platform.",
                       color_name="orange-70")

        platform = st.selectbox("Select platform", options=df['Platform'].sort_values().unique())
        platform_df = df.loc[df['Platform'] == platform]

        st.write(f"Global {platform} sales over time")
        st.bar_chart(platform_df, x="Year", y="Global_Sales")

        st.write(f"Global {platform} sales by genre")
        st.bar_chart(platform_df, x="Genre", y="Global_Sales")

        st.write("---")
        st.subheader(f"{platform} sales by region")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("North America")
            st.bar_chart(platform_df, x="Year", y="NA_Sales")
        with col2:
            st.write("Europe")
            st.bar_chart(platform_df, x="Year", y="EU_Sales")
        with col3:
            st.write("Japan")
            st.bar_chart(platform_df, x="Year", y="JP_Sales")
        with col4:
            st.write("Other")
            st.bar_chart(platform_df, x="Year", y="Other_Sales")

        st.dataframe(platform_df)

    with genre_tab:
        colored_header(label="Genre",
                       description="Best selling video games by genre.",
                       color_name="blue-green-70")

        genre = st.selectbox("Select genre", options=df['Genre'].sort_values().unique())
        genre_df = df.loc[df['Genre'] == genre]

        st.write(f"Global {genre} sales over time")
        st.bar_chart(genre_df, x="Year", y="Global_Sales")

        st.write(f"Global {genre} sales by platform")
        st.bar_chart(genre_df, x="Platform", y="Global_Sales")

        st.write("---")
        st.subheader(f"{genre} sales by region")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("North America")
            st.bar_chart(genre_df, x="Year", y="NA_Sales")
        with col2:
            st.write("Europe")
            st.bar_chart(genre_df, x="Year", y="EU_Sales")
        with col3:
            st.write("Japan")
            st.bar_chart(genre_df, x="Year", y="JP_Sales")
        with col4:
            st.write("Other")
            st.bar_chart(genre_df, x="Year", y="Other_Sales")

        st.dataframe(genre_df)

    with publisher_tab:
        colored_header(label="Publisher",
                       description="Best selling video games by publisher.",
                       color_name="violet-70")

        publisher = st.selectbox("Select publisher", options=df['Publisher'].sort_values().unique())
        publisher_df = df.loc[df['Publisher'] == publisher]

        st.write(f"Global {publisher} sales by platform")
        st.bar_chart(publisher_df, x="Platform", y="Global_Sales")

        st.write(f"Global {publisher} sales by genre")
        st.bar_chart(publisher_df, x="Genre", y="Global_Sales")

        st.write("---")
        st.subheader(f"{publisher} sales by region")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("North America")
            st.bar_chart(publisher_df, x="Year", y="NA_Sales")
        with col2:
            st.write("Europe")
            st.bar_chart(publisher_df, x="Year", y="EU_Sales")
        with col3:
            st.write("Japan")
            st.bar_chart(publisher_df, x="Year", y="JP_Sales")
        with col4:
            st.write("Other")
            st.bar_chart(publisher_df, x="Year", y="Other_Sales")

        st.write("---")

        st.dataframe(publisher_df)


if __name__ == "__main__":
    main()

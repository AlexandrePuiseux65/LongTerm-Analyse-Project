import streamlit as st
from function.services.finance import load_stock
from function.services.fetch import load_data
from visual.news_section import display_news
from visual.info_table import display_info_table

def show_info_page():
    df = load_data()

    stock_options = [f"{row['name']} ({row['symbol_paris']})" for _, row in df.iterrows()]
    
    selected_option = st.selectbox(
        "Search for a company:",
        options=stock_options,
        index=None,
        placeholder="Type the name of a company."
    )

    if selected_option:
        ticker = selected_option.split('(')[-1].strip(')')
        with st.spinner(f"Analyzing {ticker}..."):
            try:
                data = load_stock(ticker)
                print(f"DEBUG: Checking data for {data.current_price}")
                if data is not None:
                    display_info_table(data)    
            except Exception as e:
                st.error(f"An error occurred while loading data: {e}")
            try:
                display_news(data.news)
            except Exception as e:
                st.error(f"News Error: {e}")
    else:
        st.info("Please select a company from the search bar above to start the analysis.")
                
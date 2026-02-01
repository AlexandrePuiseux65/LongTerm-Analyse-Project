import streamlit as st
from function.services.finance import load_stock
from function.services.fetch import load_data
from visual.price_chart import plot_stock_history
from visual.metric_table import display_key_ratios, display_key_metrics
import pandas as pd

"""
Comment 101
"""
def show_analysis_page():
    st.title("Stock Analysis")
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
                if data is not None:
                    # Affichage du graphique
                    try:
                        fig = plot_stock_history(data)
                        st.plotly_chart(fig, use_container_width=True)
                    except Exception as e:
                        st.error(f"Chart Error: {e}")

                    # Affichage des Ratios
                    try:
                        display_key_ratios(data)
                    except Exception as e:
                        st.error(f"Ratios Table Error: {e}")

                    # Affichage des Metrics
                    try:
                        display_key_metrics(data)
                    except Exception as e:
                        st.error(f"Metrics Table Error: {e}")
                            
            except Exception as e:
                st.error(f"An error occurred while loading data: {e}")
    else:
        st.info("Please select a company from the search bar above to start the analysis.")
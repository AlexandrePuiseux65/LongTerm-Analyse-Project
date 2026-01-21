import streamlit as st
from page._explaination import show_explication_page
from page._stock_analysis import show_analysis_page
from page._stock_info import show_info_page

# Configuration de la page
st.set_page_config(page_title="Stock analysis app", layout="wide")

# Menu latéral
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to :", ["Stock Analysis", "Stock Information", "Methodology"])

if selection == "Stock Information":
    show_info_page()
elif selection == "Stock Analysis":
    show_analysis_page()
elif selection == "Methodology":
    show_explication_page()
import streamlit as st
from function.domain.ratios import per, payout_ratio, roe, dividend_coverage
from datetime import datetime

def display_key_metrics(stock):
    """Affiche les ratios financiers sous forme de colonnes."""
    year = datetime.now().year - 1
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        val_per = per(stock, year)
        st.metric("PER", f"{round(val_per, 2)}x" if val_per else "N/A")
        
    with col2:
        payout = payout_ratio(stock, year)
        st.metric("Payout Ratio", f"{round(payout * 100, 1)}%" if payout else "N/A")
        
    with col3:
        val_roe = roe(stock, year)
        st.metric("ROE", f"{round(val_roe * 100, 1)}%" if val_roe else "N/A")
        
    with col4:
        cov = dividend_coverage(stock, year)
        st.metric("Couverture", f"{round(cov, 2)}x" if cov else "N/A")
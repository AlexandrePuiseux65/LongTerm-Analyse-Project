import streamlit as st
import pandas as pd

def display_info_table(stock):
    def format_val(num, is_currency=True):
        if num is None: return "N/A"
        suffix = " €" if is_currency else ""
        if num >= 1_000_000_000:
            return f"{num / 1_000_000_000:.2f} B{suffix}"
        if num >= 1_000_000:
            return f"{num / 1_000_000:.2f} M{suffix}"
        return f"{num:,.2f}{suffix}"

    # --- SECTION 1 : COMPANY INFO ---


    # --- SECTION 2 : MARKET DATA ---
    st.markdown("### Market Data")
    market_df = pd.DataFrame([
        {"Metric": "Current Price", "Value": f"{stock.current_price:.2f} €" if stock.current_price else "N/A"},
        {"Metric": "Market Cap", "Value": format_val(stock.market_cap)},
        {"Metric": "Shares Outstanding", "Value": format_val(stock.shares_outstanding, False)}
    ])
    st.table(market_df.set_index("Metric"))

    # --- SECTION 3 : FINANCIAL STATEMENTS (AVEC BOUTONS) ---
    st.markdown("### Financial Statements")
    st.write("Click to inspect the raw data for each statement:")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Income Statement", use_container_width=True):
            st.markdown("#### Raw Income Statement")
            st.dataframe(stock.income_statement)

    with col2:
        if st.button("Balance Sheet", use_container_width=True):
            st.markdown("#### Raw Balance Sheet")
            st.dataframe(stock.balance_sheet)

    with col3:
        if st.button("Cash Flow", use_container_width=True):
            st.markdown("#### Raw Cash Flow")
            st.dataframe(stock.cashflow)

    # --- SECTION 4 : DIVIDEND HISTORY ---
    st.markdown("### Dividend History")
    div_val = stock.dividends.iloc[-1] if not stock.dividends.empty else 0
    dividends_df = pd.DataFrame([
        {"Metric": "Last Dividend Paid", "Value": f"{div_val:.2f} €"},
        {"Metric": "Years of History", "Value": f"{len(stock.dividends.index.year.unique())} years"},
        {"Metric": "Total Records", "Value": len(stock.dividends)}
    ])
    st.table(dividends_df.set_index("Metric"))
import pandas as pd
import yfinance as yf
import streamlit as st

def is_valid_ticker(ticker):
    df = pd.read_csv('data/ticker_list.csv')
    return ticker in df["symbol_paris"].values

@st.cache_data
def load_data():
    return pd.read_csv('data/ticker_list.csv')

class FetchDataStocks:
    def __init__(self, ticker) -> None:
        if not is_valid_ticker(ticker):
            raise ValueError(f"ERREUR: {ticker} not a valid CAC40 ticker")

        self.ticker = ticker
        self.stock = yf.Ticker(ticker)

        self._info = None
        self._financials = None
        self._cashflow = None
        self._balance_sheet = None
        self._history = None
        self._dividends = None
        self._news = None

    def _get_info(self):
        if self._info is None:
            try:
                self._info = self.stock.fast_info
            except Exception:
                self._info = {}
        return self._info

    def _get_financials(self):
        if self._financials is None:
            self._financials = self.stock.financials
        return self._financials

    def _get_cashflow(self):
        if self._cashflow is None:
            self._cashflow = self.stock.cashflow
        return self._cashflow

    def _get_balance_sheet(self):
        if self._balance_sheet is None:
            self._balance_sheet = self.stock.balance_sheet
        return self._balance_sheet

    def get_price_history(self, start="1990-01-01"):
        if self._history is None:
            self._history = self.stock.history(start=start)
        return self._history

    def get_current_price(self):
        info = self._get_info()
        return info.get("lastPrice") or info.get("currentPrice")

    def get_market_cap(self):
        info = self._get_info()
        return info.get("marketCap")

    def get_income_statement(self):
        return self._get_financials()

    def get_cashflow(self):
        return self._get_cashflow()

    def get_balance_sheet(self):
        return self._get_balance_sheet()

    def get_dividends(self):
        if self._dividends is None:
            self._dividends = self.stock.dividends
        return self._dividends

    def get_shares_outstanding(self):
        info = self._get_info()
        return info.get("shares") or info.get("sharesOutstanding")

    def get_sector_info(self):
        return None  # fast_info ne donne pas toujours ça proprement

    def get_growth_estimates(self):
        return None

    def get_news(self):
        if self._news is None:
            try:
                self._news = self.stock.news
            except Exception:
                self._news = []
        return self._news
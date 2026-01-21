import pandas as pd 
import yfinance as yf
from function.services.fetch import FetchDataStocks

def is_per_acceptable(per):
    return per < 15

def is_payout_safe(payout):
    return payout < 0.7

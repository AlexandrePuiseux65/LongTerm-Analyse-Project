from function.services.fetch import FetchDataStocks
from function.domain.stock import Stock

# factory fonction
def load_stock(ticker: str):
    try : 
        fetch = FetchDataStocks(ticker)

        return Stock(
            ticker=ticker,
            prices=fetch.get_price_history(),
            current_price=fetch.get_current_price(),
            market_cap=fetch.get_market_cap(),
            income_statement=fetch.get_income_statement(),
            cashflow=fetch.get_cashflow(),
            balance_sheet=fetch.get_balance_sheet(),
            dividends=fetch.get_dividends(),
            dividents_all= fetch.get_annual_dividend(),
            shares_outstanding=fetch.get_shares_outstanding(),
            news=fetch.get_news()
        )
    except Exception as e: 
        print("Error: N/A data collected from yahoo finance.")
        return None


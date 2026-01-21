class Stock:
    """
    Domain object holding raw financial and market data.
    No calculations, no extraction logic.
    """

    def __init__(
        self,
        ticker,
        prices,
        current_price,
        market_cap,
        income_statement,
        cashflow,
        balance_sheet,
        dividends,
        shares_outstanding
    ):
        self.ticker = ticker

        # Market data
        self.prices = prices
        self.current_price = current_price
        self.market_cap = market_cap

        # Financial statements (raw)
        self.income_statement = income_statement
        self.cashflow = cashflow
        self.balance_sheet = balance_sheet

        # Equity data
        self.dividends = dividends
        self.shares_outstanding = shares_outstanding

    def __repr__(self):
        return f"Stock(ticker={self.ticker}, price={self.current_price}, cap={self.market_cap})"

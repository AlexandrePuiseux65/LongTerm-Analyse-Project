import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
from plotly.subplots import make_subplots
from pytickersymbols import PyTickerSymbols
from caluleElement import MathElementAnalyseYear

class GraphData:
    def __init__(self, ticker) -> None:
        self.ticker = ticker
        self.start_date = "1990-03-01"
        self.stock = yf.Ticker(self.ticker)

    def GetStockInfo(self):
        return pd.DataFrame([self.stock.info])

    def GetStockInfoPerYear(self):
        return pd.DataFrame([self.stock.info.groupby(self.stock.dividends.index.year).sum()])

    def GetStockDividends(self):
        return pd.DataFrame([self.stock.dividends.groupby(self.stock.dividends.index.year).sum()])

    def GetStockCA(self):
        df = self.stock.financials
        
        if "Total Revenue" in df.index:
            revenues = df.loc["Total Revenue"]
        elif "TotalRevenue" in df.index: 
            revenues = df.loc["TotalRevenue"]
        else:
            return None
        return revenues

    def GetStockNetIncome(self):
        df = self.stock.financials
        if "Net Income" in df.index:
            return df.loc["Net Income"]
        return float("nan")

    def GetStockEPS(self):
        df = self.stock.financials
    
        for key in ["Basic EPS", "Diluted EPS", "Earnings Per Share", "EPS"]:
            if key in df.index:
                return df.loc[key]

        return float("nan")

    def GetSharesOutstanding(self):
        return self.stock.info.get("sharesOutstanding", float("nan"))

    def GetStockCashFlowOp(self):
        df = self.stock.cashflow
        for key in ["Operating Cash Flow", "OperatingCashFlow"]:
            if key in df.index:
                return df.loc[key].get(str(self.year), float("nan"))
        return float("nan")

    def GetStockEBITDA(self):
        df = self.stock.financials
        for key in ["Ebitda", "EBITDA"]:
            if key in df.index:
                return df.loc[key].get(str(self.year), float("nan"))
        return float("nan")

    def CFPS(self):
        cf = self.GetStockCashFlowOp()
        if cf != cf: return float("nan")
        return cf / self.GetSharesOutstanding()

    # Graph part

    def DownloadStockPrice(self):
        today_date = datetime.today().strftime("%Y-%m-%d")
        data = yf.download(self.ticker, start=self.start_date, end=today_date, auto_adjust=False)
        data.index = pd.to_datetime(data.index)
        data.columns = [col[0] if isinstance(col, tuple) else col for col in data.columns]
        return data

    def PlotDailyClosingPriceCandle(self, data_stock: pd.DataFrame):
        fig = make_subplots(
            rows=2,
            cols=1,
            shared_xaxes=True,
            vertical_spacing=0.05,
            row_heights=[0.7, 0.3],
            subplot_titles=("Price", "Volume")
        )

        fig.add_trace(
            go.Candlestick(
                x=data_stock.index,
                open=data_stock["Open"],
                high=data_stock["High"],
                low=data_stock["Low"],
                close=data_stock["Close"],
                name="Price"
            ),
            row=1,
            col=1
        )

        fig.add_trace(
            go.Bar(
                x=data_stock.index,
                y=data_stock["Volume"],
                name="Volume",
                opacity=0.4
            ),
            row=2,
            col=1
        )

        fig.update_layout(
            title=f"Daily Candlestick Price and Volume for {self.ticker}",
            template="plotly_white",
            legend=dict(orientation="h", y=1.02),
            xaxis=dict(type="date", rangeslider=dict(visible=True))
        )

        fig.update_yaxes(
            title_text="Price",
            autorange=True,
            fixedrange=False,
            row=1,
            col=1
        )

        fig.update_yaxes(
            title_text="Volume",
            autorange=True,
            fixedrange=False,
            showgrid=False,
            row=2,
            col=1
        )

        fig.show()

    def PlotDailyClosingPrice(self, data_stock: pd.DataFrame):
        if data_stock is None or data_stock.empty:
            raise ValueError("Les données de marché sont vides. Vérifiez le ticker ou la connexion.")
    
        fig = go.Figure(
            go.Scatter(
                x=data_stock.index,
                y=data_stock["Close"],
                mode="lines",
                name="Close Price"
            )
        )

        fig.update_layout(
            title=f"Daily Closing Price {self.ticker}",
            xaxis_title="Date",
            yaxis_title="Price",
            template="plotly_white",
            xaxis=dict(type="date")
        )

        return fig

def GetTicketCAC40():
    stock_data = PyTickerSymbols()
    cac40 = pd.DataFrame(stock_data.get_stocks_by_index('CAC 40'))
    cac40['symbol_paris'] = cac40['symbol'] + '.PA'
    cac40.to_csv("./data/cac40.csv")
    print('Success')

if __name__ == '__main__':
    data = GraphData("AI.PA")

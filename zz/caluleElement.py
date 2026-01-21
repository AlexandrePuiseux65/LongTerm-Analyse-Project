import pandas as pd
import numpy as ny
from dataAndGraph import GraphData

class MathElementAnalyseYear:
    def __init__(self, ticker, year) -> None:
        graph = GraphData(ticker)
        self.price = graph.DownloadStockPrice()
        self.dividend = graph.GetStockDividends()
        self.net_income = graph.GetStockNetIncome()
        self.stock_outs = graph.GetSharesOutstanding()
        self.op_cashflow = graph.GetStockCashFlowOp()
        self.ca = graph.GetStockCA()
        self.year = year

    #  Year-to-Date
    def YTD(self):
        ytd_data = self.price[self.price.index.year == self.year]

        if ytd_data.empty:
            return float("nan")

        ytd_average = ytd_data["Close"].mean()
        print("Year-to-date average:")
        return ytd_average

     # Year-to-Date in pourcent for one chosen year
    def YTD_chosen(self):
        ytd = self.price[self.price.index.year == self.year]

        if ytd.empty:
            return float("nan")

        start = ytd["Close"].iloc[0]
        end = ytd["Close"].iloc[-1]
        print("Price (start-of-year):", start, " | Price (end-of-year):", end)
        return (end - start) / start * 100

    # Divident this year
    def dividends(self):
        try:
            dty = self.dividend.loc["Dividends", self.year]
        except KeyError:
            return float("nan")

        pty = self.price["Close"].groupby(self.price.index.year).first()
        print("Dividends:", dty, " | Price start of the year:", pty[self.year])
        return (dty/pty[self.year])*100

    # BNA for the selected year
    def BNA(self):
        net_year = self.net_income[self.net_income.index.year == self.year]

        if net_year.empty:
            return float("nan")

        ni_year = net_year.iloc[0]

        if not self.stock_outs or self.stock_outs == 0:
            return float("nan")

        print("Net Income:", ni_year, " | Shares Outstanding:", self.stock_outs)
        return ni_year / self.stock_outs

    # Net Margin
    def NetMargin(self):
        if self.ca != float("nan") and self.net_income is not None:
            return self.BNA() * self.stock_outs / self.ca

    # PER
    def PER(self):
        bna = self.BNA()
        if bna != bna: return float("nan")
        last_price = self.price["Close"].iloc[-1]
        return last_price / bna

    # ROE & ROA
    def ROE(self):
        equity = self.stock.balance_sheet.loc["Total Stockholder Equity"]
        eq = equity.get(str(self.year), None)
        if eq: return self.net_income.loc[str(self.year)] / eq
        return float("nan")

    def ROA(self):
        assets = self.stock.balance_sheet.loc["Total Assets"]
        at = assets.get(str(self.year), None)
        if at: return self.net_income.loc[str(self.year)] / at
        return float("nan")

    # levier
    def levier(self):
        ebitda = self.EBITDA()
        debt = self.stock.balance_sheet.loc["Total Debt"].get(str(self.year), None)
        if ebitda and debt:
            return debt / ebitda
        return float("nan")

if __name__ == '__main__':
    math = MathElementAnalyseYear("AI.PA", 2022)
    get = GraphData("AI.PA")

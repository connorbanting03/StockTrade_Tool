import yfinance as yf


def getdata(s):
    symbol = s  # Replace with the stock symbol you want to fetch
    data = yf.download(symbol, start='2020-01-01', end='2023-01-01')
    return data

getdata("AAPL")
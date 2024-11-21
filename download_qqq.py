import yfinance as yf

# Example: Download QQQ data
ticker = "QQQ"
data = yf.download(ticker, start="2019-01-01", end="2024-11-19")
data.to_csv("./qqq.csv")
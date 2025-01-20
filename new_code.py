import yfinance as yf
import matplotlib as plt
import pandas as pd
import numpy as num

def stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info       
        print(f"Fetched data for {ticker} - Price: {info.get('currentPrice')}, PE Ratio: {info.get('trailingPE')}, Dividend Yield: {info.get('dividendYield')}")
        if 'currentPrice' not in info or 'trailingPE' not in info or 'dividendYield' not in info:
            print(f"Missing critical info for {ticker}.")
            return None    
        return {
            "symbol": ticker,
            "price" :info.get("currentPrice"),
            "peratio": info.get("trailingPE"),
            "dividend_yield": info.get("dividendYield"),
            "market_cap": info.get("marketCap"),
}
    except Exception as e:
        print(f"Error fetching data")
        return None
    
def stock_suggest(tickers):
    results =[]
    for ticker in tickers:
        data = stock_data(ticker)
        if data and data["price"] is not None:
            results.append(data)

    filtered = [
        stock for stock in results
        if stock["peratio"] is not None and stock["peratio"] <30 and
            stock ["dividend_yield"] is not None and stock ["dividend_yield"] > 0.01]
    return sorted(filtered, key=lambda x: x["dividend_yield"], reverse= True)


if __name__ == "__main__":
    tickers = ["AAPL", "TSLA", "MSFT", "BA", "T", "F", "DIS", "LCID"]
    suggestions = stock_suggest(tickers)
    
    print("Suggested Stocks")
    for suggestion in suggestions:
        print(f"Symbol: {suggestion['symbol']}, Price: {suggestion['price']}, PE Ratio: {suggestion['peratio']}, Dividend Yield: {suggestion['dividend_yield']}, Market Cap: {suggestion['market_cap']}")




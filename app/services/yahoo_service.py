import requests
from app.utils.cache import stock_cache, history_cache


def get_stock_data(symbol: str):

    cache_key = symbol

    if cache_key in stock_cache:
        return stock_cache[cache_key]

    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    print("Fetching stock data from Yahoo")

    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        raise ValueError("Invalid stock symbol")

    if response.status_code != 200:
        raise Exception("Failed to fetch stock data")

    data = response.json()

    chart = data.get("chart", {})
    result = chart.get("result")

    if not result:
        raise ValueError("Invalid stock symbol or no data found")

    meta = result[0]["meta"]

    stock_data = {
        "symbol": symbol,
        "currency": meta.get("currency"),
        "exchange": meta.get("exchangeName"),
        "current_price": meta.get("regularMarketPrice"),
        "previous_close": meta.get("previousClose"),
        "day_high": meta.get("regularMarketDayHigh"),
        "day_low": meta.get("regularMarketDayLow"),
        "year_high": meta.get("fiftyTwoWeekHigh"),
        "year_low": meta.get("fiftyTwoWeekLow"),
    }

    stock_cache[cache_key] = stock_data

    return stock_data


def get_stock_history(
    symbol: str,
    interval: str = "1d",
    range_period: str = "1mo"
):

    cache_key = f"{symbol}_{interval}_{range_period}"

    if cache_key in history_cache:
        return history_cache[cache_key]

    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/"
        f"{symbol}?interval={interval}&range={range_period}"
    )

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    print("Fetching historical data from Yahoo")

    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        raise ValueError("Invalid stock symbol")

    if response.status_code != 200:
        raise Exception("Failed to fetch historical data")

    data = response.json()

    result = data["chart"]["result"][0]

    timestamps = result.get("timestamp", [])

    quote = result["indicators"]["quote"][0]

    opens = quote.get("open", [])
    highs = quote.get("high", [])
    lows = quote.get("low", [])
    closes = quote.get("close", [])
    volumes = quote.get("volume", [])

    history = []

    for i in range(len(timestamps)):
        history.append({
            "timestamp": timestamps[i],
            "open": opens[i] if i < len(opens) else None,
            "high": highs[i] if i < len(highs) else None,
            "low": lows[i] if i < len(lows) else None,
            "close": closes[i] if i < len(closes) else None,
            "volume": volumes[i] if i < len(volumes) else None,
        })

    history_response = {
        "symbol": symbol,
        "interval": interval,
        "range": range_period,
        "data": history
    }

    history_cache[cache_key] = history_response

    return history_response

def search_stock(query: str):

    url = f"https://query1.finance.yahoo.com/v1/finance/search?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    print("Searching Yahoo Finance")

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("Failed to search stocks")

    data = response.json()

    quotes = data.get("quotes", [])

    results = []

    for item in quotes[:10]:

        results.append({
            "symbol": item.get("symbol"),
            "name": item.get("shortname"),
            "exchange": item.get("exchange"),
            "type": item.get("quoteType"),
        })

    return {
        "query": query,
        "results": results
    }
import requests


def get_stock_data(symbol: str):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

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

    return {
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

def get_stock_history(symbol: str, interval: str = "1d", range_period: str = "1mo"):
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/"
        f"{symbol}?interval={interval}&range={range_period}"
    )

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

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

    return {
        "symbol": symbol,
        "interval": interval,
        "range": range_period,
        "data": history
    }
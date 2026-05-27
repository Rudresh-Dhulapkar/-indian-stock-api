# Indian Stock API

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Render](https://img.shields.io/badge/Hosted%20on-Render-black)
![License](https://img.shields.io/badge/License-MIT-yellow)

Lightweight Indian stock market API built with FastAPI and powered by Yahoo Finance public endpoints.

Provides:

- Live stock prices
- Historical OHLC market data
- Indian stock/company search

Designed for:

- Developers
- Trading dashboards
- Portfolio trackers
- Financial analytics apps
- Learning projects
- RapidAPI publishing

---

# Live API

## Base URL

```txt
https://indian-stock-api-1mac.onrender.com
```

---

# Swagger API Docs

```txt
https://indian-stock-api-1mac.onrender.com/docs
```

---

# RapidAPI

```txt
https://rapidapi.com/RudreshDhulapkar/api/indian-stock-api1
```

---

# Features

- Live Indian stock market data
- Historical OHLC candle data
- Stock/company search endpoint
- FastAPI Swagger documentation
- Lightweight REST architecture
- In-memory caching
- JSON REST API
- Render free-tier deployment
- RapidAPI compatible

---

# Tech Stack

- FastAPI
- Python 3.11
- Requests
- Cachetools
- Yahoo Finance public endpoints
- Render
- RapidAPI

---

# API Endpoints

---

# 1. Get Stock Data

## Endpoint

```http
GET /stock
```

## Example Request

```bash
/stock?symbol=RELIANCE.NS
```

## Live Example

```txt
https://indian-stock-api-1mac.onrender.com/stock?symbol=RELIANCE.NS
```

## Sample Response

```json
{
  "symbol": "RELIANCE.NS",
  "currency": "INR",
  "exchange": "NSI",
  "current_price": 1356.3,
  "previous_close": 1367.0,
  "day_high": 1368.5,
  "day_low": 1352.4,
  "year_high": 1611.8,
  "year_low": 1290.0
}
```

---

# 2. Get Historical Data

## Endpoint

```http
GET /history
```

## Example Request

```bash
/history?symbol=RELIANCE.NS&interval=1d&range_period=1mo
```

## Live Example

```txt
https://indian-stock-api-1mac.onrender.com/history?symbol=RELIANCE.NS&interval=1d&range_period=1mo
```

## Query Parameters

| Parameter | Description |
|---|---|
| symbol | NSE/BSE stock symbol |
| interval | 1d, 1wk, 1mo |
| range_period | 1mo, 6mo, 1y, 5y |

## Response Includes

- Open price
- High price
- Low price
- Close price
- Volume
- Timestamps

## Sample Response

```json
{
  "symbol": "RELIANCE.NS",
  "interval": "1d",
  "range": "1mo",
  "data": [
    {
      "timestamp": 1777261500,
      "open": 1313.0,
      "high": 1371.6,
      "low": 1311.0,
      "close": 1365.8,
      "volume": 24673098
    }
  ]
}
```

---

# 3. Search Stocks

## Endpoint

```http
GET /search
```

## Example Request

```bash
/search?query=reliance
```

## Live Example

```txt
https://indian-stock-api-1mac.onrender.com/search?query=reliance
```

## Sample Response

```json
{
  "query": "reliance",
  "results": [
    {
      "symbol": "RELIANCE.NS",
      "name": "Reliance Industries Limited",
      "exchange": "NSI",
      "type": "EQUITY"
    }
  ]
}
```

---

# Example Indian Stock Symbols

```txt
RELIANCE.NS
TCS.NS
INFY.NS
HDFCBANK.NS
ICICIBANK.NS
SBIN.NS
ITC.NS
LT.NS
WIPRO.NS
ASIANPAINT.NS
```

---

# Local Development Setup

## Clone Repository

```bash
git clone https://github.com/Rudresh-Dhulapkar/indian-stock-api.git
```

## Move Into Project

```bash
cd indian-stock-api
```

## Create Virtual Environment

```bash
python3.11 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Development Server

```bash
uvicorn app.main:app --reload
```

---

# Local API Docs

```txt
http://127.0.0.1:8000/docs
```

---

# Project Structure

```txt
indian-stock-api/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │   ├── stock.py
│   │   ├── history.py
│   │   └── search.py
│   │
│   ├── services/
│   │   └── yahoo_service.py
│   │
│   └── utils/
│       └── cache.py
│
├── requirements.txt
├── render.yaml
├── README.md
└── .gitignore
```

---

# Deployment

Configured for deployment using:

```txt
render.yaml
```

Recommended free hosting platforms:

- Render
- Railway
- Fly.io

---

# Caching

The API uses in-memory TTL caching to:

- Reduce Yahoo Finance requests
- Improve response speed
- Reduce Render free-tier load
- Avoid repeated external API calls

---

# Error Handling

Example invalid stock response:

```json
{
  "detail": "Invalid stock symbol"
}
```

Example failed request response:

```json
{
  "detail": "Failed to fetch stock data"
}
```

---

# Roadmap

Planned features:

- [x] Live stock prices
- [x] Historical OHLC data
- [x] Stock/company search
- [ ] Trending stocks endpoint
- [ ] Top gainers/losers
- [ ] NIFTY/SENSEX endpoints
- [ ] Technical indicators
- [ ] NSE/BSE filters
- [ ] API authentication
- [ ] Redis caching
- [ ] WebSocket live streaming

---

# Contributing

Pull requests, feature suggestions, and improvements are welcome.

Feel free to fork the repository and submit a PR.

---

# Disclaimer

This project uses unofficial Yahoo Finance public endpoints.

This API is intended for:

- Educational purposes
- Development projects
- Learning FastAPI
- Prototype applications

Do not use this API as the sole source for real-money trading decisions.

---

# License

MIT License
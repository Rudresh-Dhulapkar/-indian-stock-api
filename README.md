# Indian Stock API

A lightweight FastAPI-powered Indian stock market API built using Yahoo Finance public endpoints.

Designed for:
- Developers
- Trading dashboards
- Portfolio trackers
- Financial analytics apps
- Learning projects
- RapidAPI publishing

---

# Features

- Live Indian stock market data
- Historical OHLC candle data
- Stock/company search endpoint
- FastAPI Swagger documentation
- Lightweight architecture
- In-memory caching
- Render free-tier compatible
- JSON REST API

---

# Tech Stack

- FastAPI
- Python 3.11
- Requests
- Cachetools
- Yahoo Finance API

---

# Endpoints

## 1. Get Stock Data

### Endpoint

```http
GET /stock
```

### Example

```bash
/stock?symbol=RELIANCE.NS
```

### Sample Response

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

## 2. Get Historical Data

### Endpoint

```http
GET /history
```

### Example

```bash
/history?symbol=RELIANCE.NS&interval=1d&range_period=1mo
```

### Query Parameters

| Parameter | Description |
|---|---|
| symbol | NSE/BSE stock symbol |
| interval | 1d, 1wk, 1mo |
| range_period | 1mo, 6mo, 1y, 5y |

### Response Data

Returns:
- Open price
- High price
- Low price
- Close price
- Volume
- Timestamps

---

## 3. Search Stocks

### Endpoint

```http
GET /search
```

### Example

```bash
/search?query=reliance
```

### Sample Response

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

# Local Development Setup

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/indian-stock-api.git
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

# API Documentation

FastAPI Swagger UI:

```bash
http://127.0.0.1:8000/docs
```

---

# Deployment

Configured for deployment on Render using:

```txt
render.yaml
```

Recommended hosting:
- Render
- Railway
- Fly.io

---

# Caching

The API uses in-memory TTL caching to:
- reduce Yahoo Finance requests
- improve response times
- reduce Render free-tier load

---

# Future Improvements

Planned features:
- Trending stocks endpoint
- Top gainers/losers
- Technical indicators
- NSE/BSE filters
- Rate limiting
- API key authentication
- Redis caching

---

# Disclaimer

This project uses unofficial Yahoo Finance endpoints.

This API is intended for:
- educational purposes
- development projects
- prototype applications

Do not use as a sole source for production-grade financial trading decisions.

---

# License

MIT License
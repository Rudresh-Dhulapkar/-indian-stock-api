# Indian Stock API

A lightweight FastAPI-based Indian stock market API powered by Yahoo Finance.

## Features

- Live stock market data
- Historical OHLC data
- Lightweight architecture
- Built with FastAPI
- Deployable on Render free tier
- Cached responses for improved performance

---

## Tech Stack

- FastAPI
- Python
- Requests
- Cachetools
- Yahoo Finance API

---

## Endpoints

### Get Stock Data

GET `/stock`

#### Example

```bash
/stock?symbol=RELIANCE.NS
```

#### Sample Response

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

### Get Historical Data

GET `/history`

#### Example

```bash
/history?symbol=RELIANCE.NS&interval=1d&range_period=1mo
```

#### Parameters

| Parameter | Description |
|---|---|
| symbol | NSE/BSE stock symbol |
| interval | 1d, 1wk, 1mo |
| range_period | 1mo, 6mo, 1y, 5y |

---

## Local Setup

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/indian-stock-api.git
```

Move into project:

```bash
cd indian-stock-api
```

Create virtual environment:

```bash
python3.11 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
uvicorn app.main:app --reload
```

---

## API Docs

FastAPI Swagger Docs:

```bash
http://127.0.0.1:8000/docs
```

---

## Deployment

Configured for deployment on Render free tier using `render.yaml`.

---

## Disclaimer

This project uses unofficial Yahoo Finance endpoints and is intended for educational and development purposes.
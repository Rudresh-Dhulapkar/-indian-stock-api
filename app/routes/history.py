from fastapi import APIRouter, HTTPException
from app.services.yahoo_service import get_stock_history

router = APIRouter()


@router.get(
    "/history",
    summary="Get historical stock data",
    description="Fetch OHLC historical market data."
)
def history(
    symbol: str,
    interval: str = "1d",
    range_period: str = "1mo"
):
    try:
        data = get_stock_history(symbol, interval, range_period)
        return data

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
from fastapi import APIRouter, HTTPException
from app.services.yahoo_service import get_stock_data

router = APIRouter()


@router.get("/stock")
def stock(symbol: str):
    try:
        data = get_stock_data(symbol)
        return data

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
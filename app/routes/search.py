from fastapi import APIRouter, HTTPException
from app.services.yahoo_service import search_stock

router = APIRouter()


@router.get(
    "/search",
    summary="Search Indian stocks",
    description="Search Indian stocks by company name or symbol."
)
def search(query: str):

    try:
        data = search_stock(query)
        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
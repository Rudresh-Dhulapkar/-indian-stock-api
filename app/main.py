from fastapi import FastAPI
from app.routes.stock import router as stock_router

from app.routes.history import router as history_router

app = FastAPI(
    title="Indian Stock API",
    version="1.0.0"
)

app.include_router(stock_router)
app.include_router(history_router)

@app.get("/")
def home():
    return {
        "message": "Indian Stock API is running"
    }
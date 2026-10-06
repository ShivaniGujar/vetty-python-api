from fastapi import FastAPI, Query

from app.config import settings
from app.services.coingecko_service import CoinGeckoService


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "app_name": settings.app_name,
        "version": settings.app_version
    }


@app.get("/coins")
async def get_coins(
    page_num: int = Query(default=1, ge=1),
    per_page: int = Query(default=10, ge=1)
):
    service = CoinGeckoService()

    coins = await service.get_coins()

    start = (page_num - 1) * per_page
    end = start + per_page

    return coins[start:end]
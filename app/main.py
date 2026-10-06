from fastapi import FastAPI, Query

from app.config import settings
from app.services.coingecko_service import CoinGeckoService
from fastapi import FastAPI, HTTPException, Query


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


@app.get("/categories")
async def get_categories(
    page_num: int = Query(default=1, ge=1),
    per_page: int = Query(default=10, ge=1)
):
    service = CoinGeckoService()

    categories = await service.get_categories()

    start = (page_num - 1) * per_page
    end = start + per_page

    return categories[start:end]

@app.get("/market-data")
async def get_market_data(
    coin_id: str | None = Query(default=None),
    category: str | None = Query(default=None),
    page_num: int = Query(default=1, ge=1),
    per_page: int = Query(default=10, ge=1)
):
    if not coin_id and not category:
        raise HTTPException(
            status_code=400,
            detail="Either coin_id or category must be provided"
        )

    service = CoinGeckoService()

    market_data = await service.get_market_data(
        coin_id=coin_id,
        category=category
    )

    start = (page_num - 1) * per_page
    end = start + per_page

    return market_data[start:end]
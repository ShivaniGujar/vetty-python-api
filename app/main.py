from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Query, Security

from app.config import settings
from app.security import verify_api_key
from app.services.coingecko_service import CoinGeckoService

class CoinResponse(BaseModel):
    id: str
    name: str
    symbol: str

class CategoryResponse(BaseModel):
    category_id: str
    name: str

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


@app.get("/coins", response_model=list[CoinResponse])
async def get_coins(
    page_num: int = Query(default=1, ge=1),
    per_page: int = Query(default=10, ge=1,le=100),
    api_key: str = Security(verify_api_key)
):
    service = CoinGeckoService()

    coins = await service.get_coins()

    start = (page_num - 1) * per_page
    end = start + per_page

    return coins[start:end]




@app.get(
    "/categories",
    response_model=list[CategoryResponse]
)
async def get_categories(
    page_num: int = Query(default=1, ge=1),
    per_page: int = Query(default=10, ge=1, le=100),
    api_key: str = Security(verify_api_key)
):
    service = CoinGeckoService()

    categories = await service.get_categories()

    start = (page_num - 1) * per_page
    end = start + per_page

    return categories[start:end]


@app.get("/market-data")
async def get_market_data(
    coin_id: str | None = Query(default=None, min_length=1),
    category: str | None = Query(default=None, min_length=1),
    page_num: int = Query(default=1, ge=1),
    per_page: int = Query(default=10, ge=1, le=100),
    api_key: str = Security(verify_api_key)
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


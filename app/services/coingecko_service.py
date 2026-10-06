import httpx

from app.config import settings


class CoinGeckoService:
    def __init__(self):
        self.base_url = settings.coingecko_base_url

    async def get_coins(self):
        url = f"{self.base_url}/coins/list"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        response.raise_for_status()

        return response.json()

    async def get_categories(self):
        url = f"{self.base_url}/coins/categories/list"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        response.raise_for_status()

        return response.json()

    async def get_market_data(self, coin_id=None, category=None):
        url = f"{self.base_url}/coins/markets"

        params = {
            "vs_currency": "cad"
        }

        if coin_id:
            params["ids"] = coin_id

        if category:
            params["category"] = category

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)

        response.raise_for_status()

        return response.json()
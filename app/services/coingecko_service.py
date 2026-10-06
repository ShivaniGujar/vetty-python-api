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
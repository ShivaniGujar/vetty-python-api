import logging

import httpx

from app.config import settings
from app.exceptions.handlers import ExternalServiceError


logger = logging.getLogger(__name__)


class CoinGeckoService:
    def __init__(self):
        self.base_url = settings.coingecko_base_url

    async def get_coins(self):
        url = f"{self.base_url}/coins/list"

        logger.info("Fetching coins from CoinGecko")

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(url)

            response.raise_for_status()

            logger.info("Successfully fetched coins from CoinGecko")

            return response.json()

        except httpx.TimeoutException as exc:
            logger.error("CoinGecko request timed out")

            raise ExternalServiceError(
                "CoinGecko request timed out"
            ) from exc

        except httpx.HTTPStatusError as exc:
            logger.error(
                "CoinGecko returned HTTP %s",
                exc.response.status_code,
            )

            raise ExternalServiceError(
                f"CoinGecko returned HTTP {exc.response.status_code}"
            ) from exc

        except httpx.RequestError as exc:
            logger.error("Unable to connect to CoinGecko")

            raise ExternalServiceError(
                "Unable to connect to CoinGecko"
            ) from exc

    async def get_categories(self):
        url = f"{self.base_url}/coins/categories/list"

        logger.info("Fetching categories from CoinGecko")

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(url)

            response.raise_for_status()

            logger.info(
                "Successfully fetched categories from CoinGecko"
            )

            return response.json()

        except httpx.TimeoutException as exc:
            logger.error("CoinGecko request timed out")

            raise ExternalServiceError(
                "CoinGecko request timed out"
            ) from exc

        except httpx.HTTPStatusError as exc:
            logger.error(
                "CoinGecko returned HTTP %s",
                exc.response.status_code,
            )

            raise ExternalServiceError(
                f"CoinGecko returned HTTP {exc.response.status_code}"
            ) from exc

        except httpx.RequestError as exc:
            logger.error("Unable to connect to CoinGecko")

            raise ExternalServiceError(
                "Unable to connect to CoinGecko"
            ) from exc

    async def get_market_data(
        self,
        coin_id=None,
        category=None
    ):
        url = f"{self.base_url}/coins/markets"

        params = {
            "vs_currency": "cad"
        }

        if coin_id:
            params["ids"] = coin_id

        if category:
            params["category"] = category

        logger.info(
            "Fetching market data from CoinGecko | coin_id=%s | category=%s",
            coin_id,
            category,
        )

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(
                    url,
                    params=params
                )

            response.raise_for_status()

            logger.info(
                "Successfully fetched market data from CoinGecko"
            )

            return response.json()

        except httpx.TimeoutException as exc:
            logger.error("CoinGecko request timed out")

            raise ExternalServiceError(
                "CoinGecko request timed out"
            ) from exc

        except httpx.HTTPStatusError as exc:
            logger.error(
                "CoinGecko returned HTTP %s",
                exc.response.status_code,
            )

            raise ExternalServiceError(
                f"CoinGecko returned HTTP {exc.response.status_code}"
            ) from exc

        except httpx.RequestError as exc:
            logger.error("Unable to connect to CoinGecko")

            raise ExternalServiceError(
                "Unable to connect to CoinGecko"
            ) from exc
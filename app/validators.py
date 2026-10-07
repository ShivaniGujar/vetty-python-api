from fastapi import HTTPException


def validate_market_data_filters(
    coin_id: str | None,
    category: str | None
):
    if not coin_id and not category:
        raise HTTPException(
            status_code=400,
            detail="Either coin_id or category must be provided"
        )

    return coin_id, category
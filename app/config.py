from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    #define configuration fields
    app_name: str
    app_version: str

    coingecko_base_url: str

    cache_ttl: int = 60

    webhook_url: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )


settings = Settings()  #Create settings object
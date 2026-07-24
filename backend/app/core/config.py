from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "DevInsight API"
    app_version: str = "0.1.0"

    debug: bool = True

    host: str = "0.0.0.0"
    port: int = 8000

    database_url: str
    redis_url: str

    secret_key: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


settings = Settings()
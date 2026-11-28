from pathlib import Path
from typing import Literal
from urllib.parse import urlsplit

from pydantic import SecretStr, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_ROOT = Path(__file__).resolve().parents[2]
REPOSITORY_ROOT = BACKEND_ROOT.parent
PROJECT_ROOT = (
    REPOSITORY_ROOT if (REPOSITORY_ROOT / ".env.example").is_file() else BACKEND_ROOT
)


class Settings(BaseSettings):
    """Application settings loaded from the environment and the project .env file."""

    environment: Literal["development", "production"] = "development"
    database_url: SecretStr

    redis_url: SecretStr | None = None
    celery_broker_url: SecretStr | None = None
    celery_task_default_queue: str = "cubiland"

    jwt_secret_key: SecretStr | None = None
    jwt_issuer: str = "cubiland"
    jwt_audience: str = "cubiland-api"

    resend_api_key: SecretStr | None = None
    email_from: str | None = None
    frontend_url: str = "http://localhost:3000"

    s3_endpoint: str | None = None
    s3_access_key_id: SecretStr | None = None
    s3_secret_access_key: SecretStr | None = None
    s3_bucket: str | None = None
    s3_region: str = "us-east-1"

    cors_origins: str = "http://localhost:3000,http://localhost:5173"

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @field_validator("database_url")
    @classmethod
    def validate_database_url(cls, value: SecretStr) -> SecretStr:
        """Require a PostgreSQL URL compatible with the async database driver."""
        try:
            parsed_url = urlsplit(value.get_secret_value())
            hostname = parsed_url.hostname
        except ValueError:
            raise ValueError(
                "DATABASE_URL must be a valid PostgreSQL AsyncIO URL."
            ) from None

        if (
            parsed_url.scheme != "postgresql+asyncpg"
            or not hostname
            or not parsed_url.path.strip("/")
        ):
            raise ValueError("DATABASE_URL must be a valid PostgreSQL AsyncIO URL.")
        return value

    @field_validator("cors_origins")
    @classmethod
    def validate_cors_origins(cls, value: str) -> str:
        """Validate comma-separated HTTP origins without accepting empty entries."""
        origins = [origin.strip() for origin in value.split(",")]
        if value.strip() and any(
            not origin
            or urlsplit(origin).scheme not in {"http", "https"}
            or not urlsplit(origin).netloc
            for origin in origins
        ):
            raise ValueError("CORS_ORIGINS must contain valid HTTP origins.")
        return value

    @model_validator(mode="after")
    def validate_production_secrets(self) -> "Settings":
        if self.environment == "production":
            secret = (
                self.jwt_secret_key.get_secret_value()
                if self.jwt_secret_key is not None
                else ""
            )
            if len(secret) < 32 or secret.lower().startswith("change_this"):
                raise ValueError(
                    "JWT_SECRET_KEY must be configured with a secure production value."
                )
        return self

    @property
    def cors_origin_list(self) -> list[str]:
        """Return configured CORS origins as a list for Starlette middleware."""
        if not self.cors_origins.strip():
            return []
        return [origin.strip() for origin in self.cors_origins.split(",")]


settings = Settings()  # type: ignore[call-arg]  # Loaded from environment variables.

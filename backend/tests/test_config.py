import os
from pathlib import Path
from unittest.mock import patch

import pytest
from pydantic import ValidationError

from src.core.config import PROJECT_ROOT, Settings


def test_environment_variables_override_defaults() -> None:
    environment = {
        "DATABASE_URL": ("postgresql+asyncpg://user:password@localhost:5432/cubiland"),
        "ENVIRONMENT": "production",
        "JWT_SECRET_KEY": "s" * 32,
        "CORS_ORIGINS": "https://cubiland.example",
    }
    with patch.dict(os.environ, environment, clear=True):
        settings = Settings(_env_file=None)

    assert settings.environment == "production"
    assert settings.cors_origin_list == ["https://cubiland.example"]
    assert settings.jwt_secret_key.get_secret_value() == "s" * 32


def test_project_root_resolves_from_the_moved_core_module() -> None:
    repository_root = Path(__file__).resolve().parents[2]
    expected_root = (
        repository_root
        if (repository_root / ".env.example").is_file()
        else repository_root / "backend"
    )

    assert PROJECT_ROOT == expected_root


def test_settings_load_from_env_file(tmp_path: Path) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text(
        "DATABASE_URL="
        "postgresql+asyncpg://user:password@localhost:5432/cubiland\n"
        "CORS_ORIGINS=https://cubiland.example\n",
        encoding="utf-8",
    )
    with patch.dict(os.environ, {}, clear=True):
        settings = Settings(_env_file=env_file)

    assert settings.cors_origin_list == ["https://cubiland.example"]


def test_database_url_is_required() -> None:
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValidationError):
            Settings(_env_file=None)


def test_database_url_requires_async_postgresql() -> None:
    with patch.dict(
        os.environ,
        {"DATABASE_URL": "sqlite:///cubiland.db"},
        clear=True,
    ):
        with pytest.raises(ValidationError):
            Settings(_env_file=None)


def test_production_requires_a_configured_jwt_secret() -> None:
    environment = {
        "DATABASE_URL": ("postgresql+asyncpg://user:password@localhost:5432/cubiland"),
        "ENVIRONMENT": "production",
    }
    with patch.dict(os.environ, environment, clear=True):
        with pytest.raises(ValidationError):
            Settings(_env_file=None)


def test_empty_cors_origins_disable_cors() -> None:
    environment = {
        "DATABASE_URL": ("postgresql+asyncpg://user:password@localhost:5432/cubiland"),
        "CORS_ORIGINS": "",
    }
    with patch.dict(os.environ, environment, clear=True):
        settings = Settings(_env_file=None)

    assert settings.cors_origin_list == []

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.config import settings
from src.core.exceptions import register_exception_handlers
from src.core.logging import configure_logging

configure_logging()

api_router = APIRouter(prefix="/api/v1")

api_app = FastAPI(
    title="Cubiland API",
    description="REST API for the Cubiland platform.",
    version="0.1.0",
)

api_app.include_router(api_router)
register_exception_handlers(api_app)


@api_app.get("/health", tags=["health"])
async def health_check() -> dict[str, str]:
    """Return the application process health."""
    return {"status": "ok"}


app = CORSMiddleware(
    app=api_app,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)

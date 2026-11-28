import structlog
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

logger = structlog.get_logger(__name__)

HTTP_ERROR_RESPONSES = {
    400: ("BAD_REQUEST", "The request cannot be processed."),
    401: ("UNAUTHORIZED", "Authentication is missing or invalid."),
    403: ("FORBIDDEN", "You do not have permission to perform this action."),
    404: ("NOT_FOUND", "The requested resource was not found."),
    409: ("CONFLICT", "The request conflicts with the current resource state."),
    422: ("VALIDATION_ERROR", "The request contains invalid data."),
    429: ("TOO_MANY_REQUESTS", "Too many requests."),
}


async def http_exception_handler(
    _request: Request,
    exc: Exception,
) -> JSONResponse:
    if not isinstance(exc, StarletteHTTPException):
        raise TypeError("HTTP exception handler received an unexpected exception.")
    code, message = HTTP_ERROR_RESPONSES.get(
        exc.status_code,
        ("HTTP_ERROR", "The request could not be completed."),
    )
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": code,
                "message": message,
                "details": [],
            }
        },
        headers=exc.headers,
    )


async def request_validation_exception_handler(
    _request: Request,
    exc: Exception,
) -> JSONResponse:
    if not isinstance(exc, RequestValidationError):
        raise TypeError(
            "Validation exception handler received an unexpected exception."
        )
    details: list[dict[str, str]] = []
    for error in exc.errors():
        location = [
            str(part)
            for part in error["loc"]
            if part not in {"body", "query", "path", "header", "cookie"}
        ]
        details.append(
            {
                "field": ".".join(location) or "request",
                "message": error["msg"],
            }
        )

    return JSONResponse(
        status_code=422,
        content={
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "The request contains invalid data.",
                "details": details,
            }
        },
    )


async def unexpected_exception_handler(
    _request: Request,
    exc: Exception,
) -> JSONResponse:
    logger.error(
        "unhandled_application_error",
        exception_type=type(exc).__name__,
    )
    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": "INTERNAL_SERVER_ERROR",
                "message": "An unexpected error occurred.",
                "details": [],
            }
        },
    )


def register_exception_handlers(app: FastAPI) -> None:
    """Register centralized handlers for HTTP, validation, and server errors."""
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(
        RequestValidationError,
        request_validation_exception_handler,
    )
    app.add_exception_handler(Exception, unexpected_exception_handler)

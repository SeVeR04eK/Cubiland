import asyncio
import json
from io import StringIO

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.testclient import TestClient
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import Request

from src.core.exceptions import (
    http_exception_handler,
    register_exception_handlers,
    request_validation_exception_handler,
    unexpected_exception_handler,
)
from src.core.logging import configure_logging
from src.main import (
    api_router,
    app,
    health_check,
)


def test_application_metadata_and_routes_are_initialized() -> None:
    assert app.title == "Cubiland API"
    assert api_router.prefix == "/api/v1"

    client = TestClient(app)
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_application_registers_centralized_exception_handlers() -> None:
    assert app.exception_handlers[StarletteHTTPException] is http_exception_handler
    assert (
        app.exception_handlers[RequestValidationError]
        is request_validation_exception_handler
    )
    assert app.exception_handlers[Exception] is unexpected_exception_handler


def test_exception_handlers_can_be_registered_on_another_app() -> None:
    test_app = FastAPI()
    register_exception_handlers(test_app)

    assert test_app.exception_handlers[StarletteHTTPException] is http_exception_handler
    assert test_app.exception_handlers[RequestValidationError] is (
        request_validation_exception_handler
    )
    assert test_app.exception_handlers[Exception] is unexpected_exception_handler


def test_health_endpoint_returns_ok() -> None:
    assert asyncio.run(health_check()) == {"status": "ok"}


def test_http_exceptions_use_the_documented_error_envelope() -> None:
    response = asyncio.run(
        http_exception_handler(
            Request({"type": "http"}),
            StarletteHTTPException(
                status_code=404,
                detail="Course not found.",
            ),
        )
    )

    assert response.status_code == 404
    assert json.loads(response.body) == {
        "error": {
            "code": "NOT_FOUND",
            "message": "The requested resource was not found.",
            "details": [],
        }
    }


def test_validation_errors_include_field_details() -> None:
    exception = RequestValidationError(
        [
            {
                "type": "missing",
                "loc": ("body", "display_name"),
                "msg": "Field required",
                "input": None,
            }
        ]
    )

    response = asyncio.run(
        request_validation_exception_handler(
            Request({"type": "http"}),
            exception,
        )
    )

    assert response.status_code == 422
    assert json.loads(response.body)["error"]["details"] == [
        {"field": "display_name", "message": "Field required"}
    ]


def test_unexpected_exceptions_return_generic_500_response() -> None:
    output = StringIO()
    configure_logging("development", stream=output)

    exception = RuntimeError("sensitive exception details")

    response = asyncio.run(
        unexpected_exception_handler(
            Request({"type": "http"}),
            exception,
        )
    )

    assert response.status_code == 500
    assert json.loads(response.body) == {
        "error": {
            "code": "INTERNAL_SERVER_ERROR",
            "message": "An unexpected error occurred.",
            "details": [],
        }
    }

    assert "unhandled_application_error" in output.getvalue()
    assert "RuntimeError" in output.getvalue()
    assert "sensitive exception details" not in output.getvalue()

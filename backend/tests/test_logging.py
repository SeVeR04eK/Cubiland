import json
import logging
from io import StringIO

import structlog

from src.core.logging import configure_logging


def test_development_logging_is_readable_and_integrates_structlog_and_stdlib() -> None:
    output = StringIO()
    configure_logging("development", stream=output)

    structlog.get_logger("cubiland.tests").info(
        "structured_event",
        user_id=42,
    )
    logging.getLogger("cubiland.third_party").warning("standard_event")

    rendered = output.getvalue()
    assert "structured_event" in rendered
    assert "user_id=42" in rendered
    assert "standard_event" in rendered
    assert not rendered.lstrip().startswith("{")


def test_production_logging_is_json_and_integrates_standard_logging() -> None:
    output = StringIO()
    configure_logging("production", stream=output)

    structlog.get_logger("cubiland.tests").info("production_event", item_count=3)
    logging.getLogger("cubiland.third_party").warning("standard_event")

    records = [json.loads(line) for line in output.getvalue().splitlines()]
    assert records[0]["event"] == "production_event"
    assert records[0]["item_count"] == 3
    assert records[0]["level"] == "info"
    assert records[0]["logger"] == "cubiland.tests"
    assert records[1]["event"] == "standard_event"
    assert records[1]["level"] == "warning"


def test_reconfiguring_logging_does_not_duplicate_handlers_or_messages() -> None:
    output = StringIO()
    configure_logging("development", stream=output)
    configure_logging("development", stream=output)

    logging.getLogger("cubiland.tests").info("single_event")

    assert len(logging.getLogger().handlers) == 1
    assert output.getvalue().count("single_event") == 1

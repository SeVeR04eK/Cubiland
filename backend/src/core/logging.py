import logging
import sys
from typing import Literal
from typing import TextIO

import structlog
from structlog.types import Processor

from src.core.config import settings

Environment = Literal["development", "production"]


def configure_logging(
    environment: Environment | None = None,
    stream: TextIO | None = None,
) -> None:
    """Configure one structured logging pipeline for the application."""
    selected_environment = environment or settings.environment
    output_stream = stream or sys.stdout
    log_level = (
        logging.DEBUG if selected_environment == "development" else logging.INFO
    )

    shared_processors: list[Processor] = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
    ]

    renderer: Processor
    if selected_environment == "production":
        renderer = structlog.processors.JSONRenderer()
    else:
        renderer = structlog.dev.ConsoleRenderer(colors=output_stream.isatty())

    formatter = structlog.stdlib.ProcessorFormatter(
        foreign_pre_chain=[
            structlog.stdlib.PositionalArgumentsFormatter(),
            *shared_processors,
        ],
        processors=[
            structlog.stdlib.ProcessorFormatter.remove_processors_meta,
            renderer,
        ],
    )
    handler = logging.StreamHandler(output_stream)
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    for existing_handler in root_logger.handlers[:]:
        root_logger.removeHandler(existing_handler)
        existing_handler.close()
    root_logger.setLevel(log_level)
    root_logger.addHandler(handler)

    for existing_logger in logging.root.manager.loggerDict.values():
        if isinstance(existing_logger, logging.Logger):
            for existing_handler in existing_logger.handlers[:]:
                existing_logger.removeHandler(existing_handler)
                existing_handler.close()
            existing_logger.propagate = True

    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            *shared_processors,
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

import logging
from logging import INFO, DEBUG, WARNING, ERROR, CRITICAL
import structlog

def setup_structlog():
    logging.basicConfig(level=logging.INFO)
    structlog.configure(
        processors=[
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.dev.ConsoleRenderer(),
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

def change_log_level(new_level):
    levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }

    if new_level in levels:
        logging.root.setLevel(levels[new_level])
    else:
        raise ValueError("Invalid log level: {}".format(new_level))

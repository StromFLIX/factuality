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
    if(new_level == "DEBUG"):
        new_level = DEBUG
    elif(new_level == "INFO"):
        new_level = INFO
    elif(new_level == "WARNING"):
        new_level = WARNING
    elif(new_level == "ERROR"):
        new_level = ERROR
    elif(new_level == "CRITICAL"):
        new_level = CRITICAL
    else:
        raise ValueError("Invalid log level")
    logging.root.setLevel(new_level)

import structlog

def get_logger(name: str = None) -> structlog.BoundLogger:
    log = structlog.get_logger(name)
    return log
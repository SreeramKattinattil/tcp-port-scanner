import logging
import os


def get_logger():
    """
    Create and return the application logger.
    """

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("tcp_port_scanner")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(
        "logs/scanner.log",
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

import logging
import os


def get_logger():

    os.makedirs(
        "logs",
        exist_ok=True
    )

    logger = logging.getLogger(
        "playwright_framework"
    )

    logger.setLevel(
        logging.INFO
    )

    if not logger.handlers:

        file_handler = logging.FileHandler(
            "logs/framework.log",
            mode="a"
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(
            formatter
        )

        logger.addHandler(
            file_handler
        )

    return logger
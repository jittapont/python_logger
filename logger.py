import logging
import logging.handlers
import os


class Logger:
    @classmethod
    def get_logger(cls, log_path, log_filename):
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        format = "%(asctime)s - %(levelname)s : %(message)s"
        formatter = logging.Formatter(format)
        file_handler = logging.handlers.RotatingFileHandler(
            os.path.join(log_path, f"{log_filename}.log"), maxBytes=20000000, backupCount=3, encoding="UTF-8"
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(formatter)

        if logger.hasHandlers():
            logger.handlers.clear()

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        return logger

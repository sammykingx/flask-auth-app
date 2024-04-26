import logging
import os
from logging.handlers import RotatingFileHandler


log_base_dir = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "logs",
    )
error_log_file = os.path.join(log_base_dir, "error_logs.log")
log_format = logging.Formatter(
        fmt = "=> %(asctime)s - - %(levelname)s: %(message)s " \
              "(Line: %(lineno)d [%(filename)s]",
        datefmt = "%Y/%m/%d %I:%M %p",
    )
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
error_handler = RotatingFileHandler(
        error_log_file, maxBytes=20480, backupCount=200,
    )

error_handler.setFormatter(log_format)
logger.addHandler(error_handler)

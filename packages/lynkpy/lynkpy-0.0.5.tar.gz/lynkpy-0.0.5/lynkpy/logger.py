"""logging module
"""
import logging
import os
import inspect
from concurrent_log_handler import ConcurrentRotatingFileHandler


class Logger:
    def __init__(self, path="logs.log", filename="logs.log", max_bytes=10*1024*1024):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        logfile = os.path.abspath(path)
        handler = ConcurrentRotatingFileHandler(logfile, "a", max_bytes, 0)
        formatter = logging.Formatter("%(asctime)s - %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_info(self, message):
        # Get information about the calling frame
        frame = inspect.currentframe().f_back
        filename = inspect.getframeinfo(frame).filename
        line_number = inspect.getframeinfo(frame).lineno
        self.logger.info(f"{filename}:{line_number} - {message}")
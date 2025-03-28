import logging
import os
from datetime import datetime
from typing import Optional


_DEFAULT_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

class DatetimeLogger(logging.Formatter):
    """
    Custom logging formatter to include date in the log format.
    """
    def formatDatetime(self, record: logging.LogRecord) -> str:
        # Add date to the log message
        record.asctime = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        return super().format(record)

class Logger:
    """
    A simple logger class to handle logging for the application.
    """

    def __init__(self, name: str = "WorkoutManager", log_file: Optional[str] = None):
        self.logger = logging.getLogger(f"{name}:{log_file}")
        self.logger.setLevel(logging.DEBUG)

        # Create a console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Set the formatter
        formatter = DatetimeLogger(fmt=_DEFAULT_LOG_FORMAT)
        ch.setFormatter(formatter)

        # Add the console handler to the logger
        self.logger.addHandler(ch)

        # Set the logger to not propagate to the root logger
        self.logger.propagate = False

    def logDebug(self, message: str, *args):
        """
        Log a debug message.
        :param message: The message to log
        :param args: Additional arguments to format the message
        """
        if args:
            self.logger.debug(message, *args)
        else:
            self.logger.debug(message)

    def logInfo(self, message: str, *args):
        """
        Log an info message.
        :param message: The message to log
        :param args: Additional arguments to format the message
        """
        if args:
            self.logger.info(message, *args)
        else:
            self.logger.info(message)

    def logWarn(self, message: str, *args):
        """
        Log a warning message.
        :param message: The message to log
        :param args: Additional arguments to format the message
        """
        if args:
            self.logger.warning(message, *args)
        else:
            self.logger.warning(message)

    def logError(self, message: str, *args):
        """
        Log an error message.
        :param message: The message to log
        :param args: Additional arguments to format the message
        """
        if args:
            self.logger.error(message, *args)
        else:
            self.logger.error(message)
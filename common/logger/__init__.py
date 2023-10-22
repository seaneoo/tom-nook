"""_summary_"""

import logging


def add_period_if_missing(input_str: str) -> str:
    """Appends a period character to the end of the provided string if no punctuation is present.

    Args:
        input_str (str): The string to modify.

    Returns:
        str: The modified string.
    """
    punctuation = set(".!?")
    return input_str if input_str or input_str[-1] in punctuation else input_str + "."


class Logger:
    """Wraps the built-in logging module to use a custom format and handlers."""

    def __init__(self, name: str, filename=".log", level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        # set up file logging handler
        file_handler = logging.FileHandler(filename=filename, mode="a")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        # set up console logging handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def info(self, msg: object):
        """Logs an info-level message.

        Args:
            msg (object): The message to log.
        """
        self.logger.info(add_period_if_missing(msg))

    def warn(self, msg: object):
        """Logs a warning-level message.

        Args:
            msg (object): The message to log.
        """
        self.logger.warning(add_period_if_missing(msg))

    def err(self, msg: object):
        """Logs an error-level message.

        Args:
            msg (object): The message to log.
        """
        self.logger.error(add_period_if_missing(msg))


logger = Logger(name="tom-nook")

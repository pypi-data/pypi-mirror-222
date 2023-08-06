import logging
from colorlog import ColoredFormatter
from typing import Any, NoReturn
import os

#local imports
from neolibrary.monitoring.config import config


class NeoLogger(logging.Logger):
    """
    This is a customized logger for NeoMedSys project.

    Args:
        name (str): Name of the logger.
        level (int, optional): Logging level. Defaults to logging.NOTSET.

    Returns:
        logging.Logger: A customized logger.
    """
    def __init__(self, name: str, 
                 level: int = config.LOG_LEVEL,
                 level_e: int = config.LOG_LEVEL_E) -> NoReturn:
        """
        This is a customized logger for NeoMedSys project.

        Args:
            name (str): Name of the logger.
            level (int, optional): Logging level. Defaults to logging.NOTSET.

        Returns:
            logging.Logger: A customized logger.
        """
        super().__init__(name, level)
        self.init_logger()
        self.name = name
        self.PATH = config.ROOT + "/logs/" + name + ".log"
        logging.addLevelName(config.SUCCESS, "SUCCESS")
        logging.addLevelName(config.FAIL, "FAIL")
        logging.addLevelName(config.PIPE, "PIPE")
        logging.root.setLevel(level)
        self.formatter = ColoredFormatter(
            config.LOGFORMAT,
            log_colors=config.LOG_COLORS,
        )
        self.e_formatter = ColoredFormatter(
            config.LOGFORMAT_ERROR,
            log_colors=config.LOG_COLORS,
        )
        self.stream = logging.StreamHandler()
        self.file_handler = logging.FileHandler(self.PATH)
        self.file_handler.setLevel(level_e)
        self.stream.setFormatter(self.formatter)
        self.file_handler.setFormatter(self.e_formatter)
        self.setLevel(config.LOG_LEVEL)
        if self.hasHandlers():
            self.handlers.clear()
        self.addHandler(self.stream)
        self.addHandler(self.file_handler)

    def success(self, message: str, *args: Any, **kws: Any) -> NoReturn:
        """
        Log 'message % args' with severity 'SUCCESS'.

        Args:
            message (str): Message to log.
            *args (Any): Arguments to log.
            **kws (Any): Keyword arguments to log.

        Returns:
            None: NoReturn
        """
        if self.isEnabledFor(config.SUCCESS):
            self._log(config.SUCCESS, message, args, **kws)

    def fail(self, message: str, *args: Any, **kws: Any) -> NoReturn:
        """
        Log 'message % args' with severity 'FAIL'.

        Args:
            message (str): Message to log.
            *args (Any): Arguments to log.
            **kws (Any): Keyword arguments to log.

        Returns:
            None: NoReturn
        """
        if self.isEnabledFor(config.FAIL):
            self._log(config.FAIL, message, args, **kws)

    def pipe(self, message: str, *args: Any, **kws: Any) -> NoReturn:
        """
        Log 'message % args' with severity 'PIPE'.

        Args:
            message (str): Message to log.
            *args (Any): Arguments to log.
            **kws (Any): Keyword arguments to log.

        Returns:
            None: NoReturn
        """
        if self.isEnabledFor(config.PIPE):
            self._log(config.PIPE, message, args, **kws)


    def init_logger(self):
        """ 
        Initialize the logger by setting up the folder structure if it doesn't exist.
        """
        if not os.path.exists(config.ROOT + "/logs"):
            os.makedirs(config.ROOT + "/logs")
        



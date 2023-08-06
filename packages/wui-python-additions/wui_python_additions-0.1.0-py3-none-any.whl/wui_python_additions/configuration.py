from configparser import ConfigParser
import logging
import logging.config
from typing import Union
import json
import os
import pathlib

__all__ = ['ConfigurationManager']
logging.basicConfig(format='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s', level=logging.INFO)

class ConfigurationManager:
    """Class handles program initialization using config files.

    Raises:
        FileNotFoundError: Can't find given config path

    Returns:
        ConfigurationManager
    """
    _project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # path to project directory
    _working_dir = os.getcwd() # path to current working directory
    _config_parser = ConfigParser() # Parser that can be used to get config entries
    _data_folder = "" # path to data folder
    __logger = logging.getLogger(__name__)

    @classmethod
    def init_config_file(cls, config_path : str):
        """Initialize config for app from given file

        Args:
            config_path (str): Path to main config file, can be local to working directory.

        Raises:
            FileNotFoundError: if passed config path does not exist
        """
        raise_if_not_found = False
        if config_path:
            raise_if_not_found = True
        if not os.path.isfile(config_path):
            cls.__logger.warning(f'ConfigurationManager: Config file {config_path} does not exists, trying to get file from working directory')
            config_path = os.path.join(cls._working_dir, 'config.ini')
            if not os.path.isfile(config_path):
                if raise_if_not_found:
                    raise FileNotFoundError(f'Config file {config_path} does not exists')
                else:
                    config_path = ""
        cls._config_path = config_path
        if cls._config_path:
            cls.__logger.info(f"Using config file '{cls._config_path}'")
            cls._config_parser.read(cls._config_path)
        else:
            cls.__logger.info("Default config file not found")

    @classmethod
    def init_logging(cls, logging_config_path : str):
        if not os.path.isfile(logging_config_path):
            cls.__logger.warning('ConfigurationManager: Trying to get path for logging config file from \'General\' section from main config file using key \'config_file\'')
            if cls._config_parser and 'General' in cls._config_parser:
                logging_config_path = cls._config_parser['General'].get('config_file', '')
            if not logging_config_path:
                if not os.path.isfile(logging_config_path):
                    cls.__logger.warning(f'ConfigurationManager: Logging config {logging_config_path} does not exists, trying to get file from working directory')
                    logging_config_path = os.path.join(cls._working_dir, "logging.json")
                    if not os.path.isfile(logging_config_path):
                        # Using default logging configuration
                        logging_config_path = ""
        cls._logging_config_path = logging_config_path
        if cls._logging_config_path:
            cls.__logger.info(f"ConfigurationManager: Using logging config file '{cls._logging_config_path}'")
            with open(cls._logging_config_path, 'rt') as f:
                config = json.load(f)
            logging.config.dictConfig(config)
        else:
            cls.__logger.warning(f'ConfigurationManager: Logging config file {logging_config_path} does not exists, using default logger')
        cls.__logger = logging.getLogger(__name__)
        cls.__logger.debug("Logging handlers:")
        root_logger = logging.getLogger() # get the root logger
        cls.__logger.debug(root_logger.handlers)
    
    @classmethod
    def init_data_folder(cls):
        cls._data_folder = pathlib.Path(cls._config_parser['General'].get('data_folder'))
        cls._data_folder.mkdir(parents=True, exist_ok=True)
    
    @classmethod
    def add_logging_level(cls, level_name : str, level_num : int, method_name : Union[str, None] = None):
        """
        Comprehensively adds a new logging level to the `logging` module and the
        currently configured logging class.

        `level_name` becomes an attribute of the `logging` module with the value
        `levelNum`. `method_name` becomes a convenience method for both `logging`
        itself and the class returned by `logging.getLoggerClass()` (usually just
        `logging.Logger`). If `method_name` is not specified, `level_name.lower()` is
        used.

        To avoid accidental clobberings of existing attributes, this method will
        raise an `AttributeError` if the level name is already an attribute of the
        `logging` module or if the method name is already present 

        Example
        -------
        >>> addLoggingLevel('TRACE', logging.DEBUG - 5)
        >>> logging.getLogger(__name__).setLevel("TRACE")
        >>> logging.getLogger(__name__).trace('that worked')
        >>> logging.trace('so did this')
        >>> logging.TRACE
        5

        """
        if not method_name:
            method_name = level_name.lower()

        if hasattr(logging, level_name):
            raise AttributeError('{} already defined in logging module'.format(level_name))
        if hasattr(logging, method_name):
            raise AttributeError('{} already defined in logging module'.format(method_name))
        if hasattr(logging.getLoggerClass(), method_name):
            raise AttributeError('{} already defined in logger class'.format(method_name))

        # This method was inspired by the answers to Stack Overflow post
        # http://stackoverflow.com/q/2183233/2988730, especially
        # http://stackoverflow.com/a/13638084/2988730
        def logForLevel(cls, message, *args, **kwargs):
            if cls.isEnabledFor(level_num):
                cls._log(level_num, message, args, **kwargs)
        def logToRoot(message, *args, **kwargs):
            logging.log(level_num, message, *args, **kwargs)

        logging.addLevelName(level_num, level_name)
        setattr(logging, level_name, level_num)
        setattr(logging.getLoggerClass(), method_name, logForLevel)
        setattr(logging, method_name, logToRoot)
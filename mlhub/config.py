import sys
import pathlib
import logging

import mlhub

PACKAGE_ROOT = pathlib.Path(mlhub.__file__).resolve().parent
LOG_FILE = pathlib.Path().cwd() / 'MLHUB.log'

FORMATTER = logging.Formatter(
    "[%(asctime)s] — %(levelname)s — "
    "%(funcName)s:%(lineno)d — %(message)s\n \n")


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    file_handler = logging.FileHandler(filename=config.LOG_FILE, mode='a')
    file_handler.setFormatter(FORMATTER)
    return file_handler

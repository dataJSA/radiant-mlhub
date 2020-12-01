import os
import pathlib
import logging

from . import config
# Configure logger for use in package
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(config.get_console_handler())
logger.addHandler(config.get_file_handler())
logger.propagate = False


with open(os.path.join(config.PACKAGE_ROOT, 'VERSION')) as version_file:
    __version__ = version_file.read().strip()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
from pathlib import Path

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'mlhub'
DESCRIPTION = 'Radiant MLHub client for accessing earth observa'
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'
URL = ''
DOWNLOAD_URL = 'https://github.com/dataJSA/radiant-mlhub'
EMAIL = ''
AUTHOR = "Joshua Sant'Anna"
REQUIRES_PYTHON = ">=3.6.0"

here = os.path.abspath(os.path.dirname(__file__))

# Import the README for the long description.
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        LONG_DESCRIPTION = '\n' + f.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION

# Load the package's VERSION file as a dictionary.
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME
about = {}
with open(PACKAGE_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['VERSION'] = _version


# Package requirements
def requirements(fname='requirements.txt'):
    with open(fname) as fd:
        return fd.read().splitlines()


def dev_requirements(fname='requirements_dev.txt'):
    with open(fname) as file:
        return file.read().splitlines()


setup(
    name=NAME,
    version=about['VERSION'],
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author="Joshua Sant'Anna",
    author_email=EMAIL,
    url=URL,
    download_url=DOWNLOAD_URL,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=('tests')),
    install_requires=requirements(),
    extra_requires={'dev': dev_requirements(), },
    license='MIT',
    zip_safe=True,
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=['data science', 'satellite imagery']
)

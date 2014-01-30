#!/usr/bin/env python
# 

from charlie import __appname__, __version__
from setuptools import setup

long_description = open('README.rst').read()

setup(
    name       = __appname__,
    version    = __version__,
    packages   = [ 'charlie',],

    author       = "Paul Tagliamonte",
    author_email = "paultag@ubuntu.com",

    long_description = long_description,
    description      = 'Boston MBTA Data',
    license          = "GPLv3",
    url              = "https://github.com/paultag/python-charlie",

    platforms        = ['any']
)

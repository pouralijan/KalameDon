#!/usr/bin/env python3
"""
-*- coding: utf-8 -*-
"""

__title__ = 'KalameDon'
__version__ = '0.1.0.dev0'
__author__ = 'Hassan Pouralijan'
__maintainer__ = 'Hassan Pouralijan'
__email__ = 'pouralijan@gmail.com'
__copyright__ = 'Copyright 2020 by pouarlijan'
__license__ = 'MIT'


def get_version(number: bool=False)->str:
    """
    Return package version.
    -- number: If True return number of version only, otherwise return
        full version.
    """
    if number:
        return '.'.join(__version__.split(".")[:-1])
    return __version__

#from .kalamedon import KalameDon

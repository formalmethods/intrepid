"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017

This module implements some color shortcuts
"""
from colorama import Fore, Style

def fail(message):
    """
    Color message as failure
    """
    return _fmt(Fore.RED, Style.BRIGHT, message)

def warn(message):
    """
    Color message as warning
    """
    return _fmt(Fore.YELLOW, Style.BRIGHT, message)

def good(message):
    """
    Color message as success
    """
    return _fmt(Fore.GREEN, Style.BRIGHT, message)

def info(message):
    """
    Color message as info
    """
    return _fmt(Fore.CYAN, Style.BRIGHT, message)

def dim(message):
    """
    dim message
    """
    return _fmt(Fore.BLACK, Style.BRIGHT, message)

def enhance(message):
    """
    enhance message
    """
    return _fmt(Fore.WHITE, Style.BRIGHT, message)

def _fmt(color, style, message):
    """
    Helper routine
    """
    return color + style + message + Fore.RESET + Style.RESET_ALL

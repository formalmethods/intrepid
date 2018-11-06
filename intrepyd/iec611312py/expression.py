"""
Copyright (C) 2018 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 01/11/2018

This module implements infrastructure to store expressions
"""

from intrepyd.visitable import Visitable

class VariableOcc(Visitable):
    """
    Stores a variable occurrence
    """
    def __init__(self, var):
        self._var = var

    @property
    def var(self):
        """
        Getter
        """
        return self._var

class ConstantOcc(Visitable):
    """
    Stores a constant occurrence
    """
    def __init__(self, cst):
        self._cst = cst

    @property
    def cst(self):
        """
        Getter
        """
        return self._cst

class Expression(Visitable):
    """
    Base class for expressions
    """
    def __init__(self, operator, arguments):
        self._operator = operator
        self._arguments = arguments

    @property
    def operator(self):
        return self._operator
    
    @property
    def arguments(self):
        return self._arguments

TRUE = ConstantOcc('TRUE')
FALSE = ConstantOcc('FALSE')
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

class ExpressionBase(Visitable):
    """
    Base class for expressions
    """
    def __init__(self):
        self._datatype = None

    @property 
    def datatype(self):
        return self._datatype

    @datatype.setter
    def datatype(self, x):
        self._datatype = x

class VariableOcc(ExpressionBase):
    """
    Stores a variable occurrence
    """
    def __init__(self, var):
        ExpressionBase.__init__(self)
        self._var = var

    @property
    def var(self):
        """
        Getter
        """
        return self._var

class ConstantOcc(ExpressionBase):
    """
    Stores a constant occurrence
    """
    def __init__(self, cst):
        ExpressionBase.__init__(self)
        self._cst = cst

    @property
    def cst(self):
        """
        Getter
        """
        return self._cst

class Expression(ExpressionBase):
    """
    Base class for expressions
    """
    def __init__(self, operator, arguments):
        ExpressionBase.__init__(self)
        self._operator = operator
        self._arguments = arguments

    @property
    def operator(self):
        return self._operator
    
    @property
    def arguments(self):
        return self._arguments

class Range(ExpressionBase):
    def __init__(self, first, last):
        ExpressionBase.__init__(self)
        if first > last:
            raise RuntimeError('From is greater than to in range expression')
        self._first = first
        self._last = last

class Ite(ExpressionBase):
    """
    Term If-then-else. This construct does not exist in ST language. It is used
    as intermediate step before translating into intrepyd
    """
    def __init__(self, condition, then_term, else_term):
        ExpressionBase.__init__(self)
        self._condition = condition
        self._then_term = then_term
        self._else_term = else_term

    @property
    def condition(self):
        return self._condition

    @property
    def then_term(self):
        return self._then_term

    @property
    def else_term(self):
        return self._else_term

TRUE = ConstantOcc('TRUE')
FALSE = ConstantOcc('FALSE')
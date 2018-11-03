"""
Copyright (C) 2018 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 02/11/2018

This module implements a printer for the parsed AST
"""

from intrepyd.iec611312py.visitor import Visitor
from intrepyd.iec611312py.statement import Assignment
from intrepyd.iec611312py.expression import VariableOcc, Expression

class AstPrinter(Visitor):
    """
    Visitor for printing AST on a string
    """
    def __init__(self):
        self._result = ''

    @property
    def result(self):
        return self._result

    def _visit_assignment(self, obj):
        obj.lhs.accept(self)
        self._result += ' := '
        obj.rhs.accept(self)

    def _visit_expression(self, obj):
        pass

    def _visit_variable_occ(self, obj):
        self._result += obj.var.name

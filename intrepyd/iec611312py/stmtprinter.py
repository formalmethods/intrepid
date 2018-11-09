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

class StmtPrinter(Visitor):
    """
    Visitor for printing Statements on a string
    """
    def __init__(self):
        self._result = ''
        self._indent = 0

    @property
    def result(self):
        return self._result

    def processStatements(self, statements):
        for statement in statements:
            statement.accept(self)

    def _visit_assignment(self, obj):
        obj.lhs.accept(self)
        self._result += ' := '
        obj.rhs.accept(self)
        self._result += ';'

    def _visit_ifthenelse(self, obj):
        first = True
        if len(obj.conditions) != len(obj.stmt_blocks):
            raise RuntimeError('Wrong number of conditions and statements')
        for i in range(len(obj.conditions)):
            if first:
                self._result += 'IF '
                first = False
            else:
                self._result += 'ELIF '
            obj.conditions[i].accept(self)
            self._result += ' THEN '
            for statements in obj.stmt_blocks:
                for i in range(len(statements)):
                    statements[i].accept(self)
                    self._result += ' '
        self._result += 'END_IF;'

    def _visit_expression(self, expression):
        args = expression.arguments
        nargs = len(args)
        if nargs == 1:
            self._result += expression.operator + '('
            expression.arguments[0].accept(self)
            self._result += ')'
            return
        elif nargs == 2:
            self._result += '('
            args[0].accept(self)
            self._result += ' ' + expression.operator + ' '
            args[1].accept(self)
            self._result += ')'

    def _visit_variable_occ(self, variableOcc):
        self._result += variableOcc.var.name

    def _visit_constant_occ(self, constantOcc):
        self._result += constantOcc.cst

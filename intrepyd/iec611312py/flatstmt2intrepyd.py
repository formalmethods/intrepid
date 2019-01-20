"""
Copyright (C) 2018 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 29/10/2018

This module implements the translation from flat statements into intrepyd
"""

from intrepyd.iec611312py.visitor import Visitor
from intrepyd.iec611312py.statement import Assignment
from intrepyd.iec611312py.expression import Ite, Expression, ConstantOcc, VariableOcc

STOP2INTREPYDUNARYOP = {
    '-' : 'mk_minus',
    'not' : 'mk_not'
}

STOP2INTREPYDBINARYOP = {
    '+' : 'mk_add',
    '-' : 'mk_sub',
    '*' : 'mk_mul',
    '/' : 'mk_div',
    '=' : 'mk_eq',
    '<>' : 'mk_neq',
    '<' : 'mk_lt',
    '>' : 'mk_gt',
    '<=' : 'mk_leq',
    '>=' : 'mk_geq',
    'OR' : 'mk_or',
    'AND' : 'mk_and',
    'XOR' : 'mk_xor',
}

class FlatStmt2Intrepyd(Visitor):
    """
    Visitor for outputting the intrepyd equivalent of an AST
    """
    def __init__(self, indent, context, var2latch):
        self._result = ''
        self._indent = indent
        self._count = 0
        self._var2latch = var2latch
        self._usedlatches = set()
        self._prefix = context + '.'

    @property
    def result(self):
        return self._result

    def processStatements(self, statements):
        for statement in statements:
            if not isinstance(statement, Assignment):
                raise RuntimeError('Expected Assignment, got ' + str(type(statement)))
            statement.accept(self)
        for name in self._var2latch:
            latch, init = self._var2latch[name]
            if latch in self._usedlatches:
                continue
            self._indent_result()
            self._result += self._prefix + 'set_latch_init_next(' +\
                            latch + ', ' +\
                            init + ', ' +\
                            latch + ')\n'

    def _indent_result(self):
        self._result += ' ' * self._indent

    def _getTmpVar(self):
        self._count += 1
        return '__tmp_' + str(self._count)

    def _visit_assignment(self, obj):
        name = obj.lhs.var.name
        next_ = obj.rhs.accept(self)
        if name in self._var2latch:
            latch, init = self._var2latch[name]
            self._indent_result()
            self._result += self._prefix + 'set_latch_init_next(' +\
                            latch + ', ' +\
                            init + ', ' +\
                            next_ + ')'
            self._usedlatches.add(latch)
        else:
            self._indent_result()
            self._result += name + ' = ' + next_
        self._result += '\n'

    def _visit_expression(self, expression):
        result = self._getTmpVar()
        args = expression.arguments
        nargs = len(args)
        self._indent_result()
        self._result += result + ' = '
        if nargs == 1:
            if not expression.operator in STOP2INTREPYDUNARYOP:
                raise RuntimeError('Could not handle unary op ' + expression.operator)
            self._result += self._prefix + STOP2INTREPYDUNARYOP[expression.operator] +\
                            '(' + args[0].accept(self) + ')'
        elif nargs == 2:
            if not expression.operator in STOP2INTREPYDBINARYOP:
                raise RuntimeError('Could not handle binary op ' + expression.operator)
            self._result += self._prefix + STOP2INTREPYDBINARYOP[expression.operator] + '(' +\
                            args[0].accept(self) + ', ' +\
                            args[1].accept(self) + ')'
        else:
            raise RuntimeError('Could not handle op ' + expression.operator)
        self._result += '\n'
        return result

    def _visit_ite(self, ite):
        result = self._getTmpVar()
        self._indent_result()
        self._result += result + ' = ' +\
                        self._prefix + 'mk_ite(' +\
                        ite.condition.accept(self) + ', ' +\
                        ite.then_term.accept(self) + ', ' +\
                        ite.else_term.accept(self) + ')\n'
        return result

    def _visit_variable_occ(self, variableOcc):
        return variableOcc.var.name

    def _visit_constant_occ(self, constantOcc):
        return constantOcc.cst




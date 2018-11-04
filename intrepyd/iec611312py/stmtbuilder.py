"""
Copyright (C) 2018 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 29/10/2018

This module implements the main parsing routine of IEC61131 text
"""

from intrepyd.iec611312py.IEC61131ParserVisitor import IEC61131ParserVisitor
from intrepyd.iec611312py.statement import Assignment
from intrepyd.iec611312py.expression import VariableOcc, Expression

class STMTBuilder(IEC61131ParserVisitor):
    """
    Vistor that builds statements from the IEC program
    """
    def __init__(self, name2var):
        self._statements = []
        self._name2var = name2var

    @property
    def statements(self):
        return self._statements

    def visitAssignVariable(self, ctx):
        lhs = ctx.getChild(0).accept(self)
        rhs = ctx.getChild(2).accept(self)
        self._statements.append(Assignment(lhs, rhs))

    def visitExpression(self, ctx):
        return ctx.getChild(0).accept(self)

    def visitBinaryBoolExpression(self, ctx):
        operator = ctx.op.text
        arguments = [ctx.getChild(0).accept(self), ctx.getChild(2).accept(self)]
        return Expression(operator, arguments)

    def visitUnaryBoolExpression(self, ctx):
        operator = ctx.getChild(0).getText()
        return Expression(operator, [ctx.getChild(1).accept(self)])
    
    def visitZeroaryBoolExpression(self, ctx):
        return ctx.getChild(0).accept(self)

    def visitParBoolExpression(self, ctx):
        return ctx.subexpr.accept(self)

    def visitParTermExpression(self, ctx):
        return ctx.subexpr.accept(self)
    
    def visitVariable_name(self, ctx):
        var = ctx.getText()
        if not var in self._name2var:
            raise RuntimeError('Undeclared variable ' + var)
        return VariableOcc(self._name2var[var])

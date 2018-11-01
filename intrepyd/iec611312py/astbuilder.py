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
from intrepyd.iec611312py.assignment import Assignment

class ASTBuilder(IEC61131ParserVisitor):
    """
    Vistor that builds the internal AST for the
    IEC program
    """
    def __init__(self):
        self._body = None

    @property
    def body(self):
        return self._body

    def visitAssign_stmt(self, ctx):
        lhs = ctx.getChild(0).accept(self)
        rhs = ctx.getChild(2).accept(self)
        return Assignment(lhs, rhs)

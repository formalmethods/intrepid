"""
This module implements the building of a formula
"""

from intrepyd.formula2py.FormulaVisitor import FormulaVisitor
from intrepyd.formula2py.FormulaParser import FormulaParser

class FormulaBuilder(FormulaVisitor):
    """
    This class implements a builder for a formula in string
    """

    def __init__(self):
        self._formula = None

    @property
    def formula(self):
        """
        Gets the built formula
        """
        return self._formula

    def visitFormula(self, ctx: FormulaParser.FormulaContext):
        self._formula = ctx.getChild(0).accept(self)

    def visitAndExpr(self, ctx):
        child_count = ctx.getChildCount()
        assert child_count >= 3, child_count
        assert child_count % 2 == 1, child_count
        return {'AND': [ctx.getChild(i).accept(self) for i in range(0, child_count, 2)]}

    def visitOrExpr(self, ctx):
        child_count = ctx.getChildCount()
        assert child_count >= 3, child_count
        assert child_count % 2 == 1, child_count
        return {'OR': [ctx.getChild(i).accept(self) for i in range(0, child_count, 2)]}

    def visitNotExpr(self, ctx):
        assert ctx.getChildCount() == 2
        return {'NOT': ctx.getChild(1).accept(self)}

    def visitPreExpr(self, ctx):
        assert ctx.getChildCount() == 2
        return {'PRE': ctx.getChild(1).accept(self)}

    def visitParExpr(self, ctx):
        assert ctx.getChildCount() == 3
        return ctx.getChild(1).accept(self)

    def visitParID(self, ctx: FormulaParser.ParIDContext):
        return ctx.getText()

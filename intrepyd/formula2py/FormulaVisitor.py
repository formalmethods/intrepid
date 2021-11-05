# Generated from Formula.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FormulaParser import FormulaParser
else:
    from FormulaParser import FormulaParser

# This class defines a complete generic visitor for a parse tree produced by FormulaParser.

class FormulaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FormulaParser#formula.
    def visitFormula(self, ctx:FormulaParser.FormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#parExpr.
    def visitParExpr(self, ctx:FormulaParser.ParExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#notExpr.
    def visitNotExpr(self, ctx:FormulaParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#parID.
    def visitParID(self, ctx:FormulaParser.ParIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#orExpr.
    def visitOrExpr(self, ctx:FormulaParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#preExpr.
    def visitPreExpr(self, ctx:FormulaParser.PreExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#andExpr.
    def visitAndExpr(self, ctx:FormulaParser.AndExprContext):
        return self.visitChildren(ctx)



del FormulaParser
# Generated from ST.g4 by ANTLR 4.6
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by STParser.

class STVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by STParser#program.
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#datatypedef.
    def visitDatatypedef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#constant.
    def visitConstant(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#node.
    def visitNode(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#instrList.
    def visitInstrList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#instr.
    def visitInstr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#varDeclList.
    def visitVarDeclList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#varDeclGroup.
    def visitVarDeclGroup(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#plainType.
    def visitPlainType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#recordType.
    def visitRecordType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#enumType.
    def visitEnumType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#arrayType.
    def visitArrayType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#subrangeType.
    def visitSubrangeType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#userType.
    def visitUserType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#primitiveType.
    def visitPrimitiveType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#bound.
    def visitBound(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#prop.
    def visitProp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#realizabilityInputs.
    def visitRealizabilityInputs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#ivc.
    def visitIvc(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#main.
    def visitMain(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#assertion.
    def visitAssertion(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#equation.
    def visitEquation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#lhs.
    def visitLhs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#recordExpr.
    def visitRecordExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#intExpr.
    def visitIntExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#arrayExpr.
    def visitArrayExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#castExpr.
    def visitCastExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#realExpr.
    def visitRealExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#ifThenElseExpr.
    def visitIfThenElseExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#binaryExpr.
    def visitBinaryExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#preExpr.
    def visitPreExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#initCurrExpr.
    def visitInitCurrExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#nodeCallExpr.
    def visitNodeCallExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#recordAccessExpr.
    def visitRecordAccessExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#negateExpr.
    def visitNegateExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#condactExpr.
    def visitCondactExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#notExpr.
    def visitNotExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#arrayAccessExpr.
    def visitArrayAccessExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#arrayUpdateExpr.
    def visitArrayUpdateExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#boolExpr.
    def visitBoolExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#tupleExpr.
    def visitTupleExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#recordUpdateExpr.
    def visitRecordUpdateExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#idExpr.
    def visitIdExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#baseEID.
    def visitBaseEID(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#arrayEID.
    def visitArrayEID(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STParser#recordEID.
    def visitRecordEID(self, ctx):
        return self.visitChildren(ctx)



# Generated from Lustre.g4 by ANTLR 4.7.2
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by LustreParser.

class LustreVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LustreParser#program.
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#datatypedef.
    def visitDatatypedef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#constant.
    def visitConstant(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#node.
    def visitNode(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#instrList.
    def visitInstrList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#instr.
    def visitInstr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#varDeclList.
    def visitVarDeclList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#varDeclGroup.
    def visitVarDeclGroup(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#plainType.
    def visitPlainType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#recordType.
    def visitRecordType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#enumType.
    def visitEnumType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#arrayType.
    def visitArrayType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#subrangeType.
    def visitSubrangeType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#userType.
    def visitUserType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#primitiveType.
    def visitPrimitiveType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#bound.
    def visitBound(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#prop.
    def visitProp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#realizabilityInputs.
    def visitRealizabilityInputs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#ivc.
    def visitIvc(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#main.
    def visitMain(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#assertion.
    def visitAssertion(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#equation.
    def visitEquation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#lhs.
    def visitLhs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#recordExpr.
    def visitRecordExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#intExpr.
    def visitIntExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#arrayExpr.
    def visitArrayExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#castExpr.
    def visitCastExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#realExpr.
    def visitRealExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#ifThenElseExpr.
    def visitIfThenElseExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#binaryExpr.
    def visitBinaryExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#preExpr.
    def visitPreExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#initCurrExpr.
    def visitInitCurrExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#nodeCallExpr.
    def visitNodeCallExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#recordAccessExpr.
    def visitRecordAccessExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#negateExpr.
    def visitNegateExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#condactExpr.
    def visitCondactExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#notExpr.
    def visitNotExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#arrayAccessExpr.
    def visitArrayAccessExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#arrayUpdateExpr.
    def visitArrayUpdateExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#boolExpr.
    def visitBoolExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#tupleExpr.
    def visitTupleExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#recordUpdateExpr.
    def visitRecordUpdateExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#idExpr.
    def visitIdExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#baseEID.
    def visitBaseEID(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#arrayEID.
    def visitArrayEID(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#recordEID.
    def visitRecordEID(self, ctx):
        return self.visitChildren(ctx)



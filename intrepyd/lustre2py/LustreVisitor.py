# Generated from Lustre.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LustreParser import LustreParser
else:
    from LustreParser import LustreParser

# This class defines a complete generic visitor for a parse tree produced by LustreParser.

class LustreVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LustreParser#program.
    def visitProgram(self, ctx:LustreParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#datatypedef.
    def visitDatatypedef(self, ctx:LustreParser.DatatypedefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#constant.
    def visitConstant(self, ctx:LustreParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#node.
    def visitNode(self, ctx:LustreParser.NodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#instrList.
    def visitInstrList(self, ctx:LustreParser.InstrListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#instr.
    def visitInstr(self, ctx:LustreParser.InstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#varDeclList.
    def visitVarDeclList(self, ctx:LustreParser.VarDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#varDeclGroup.
    def visitVarDeclGroup(self, ctx:LustreParser.VarDeclGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#plainType.
    def visitPlainType(self, ctx:LustreParser.PlainTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#recordType.
    def visitRecordType(self, ctx:LustreParser.RecordTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#enumType.
    def visitEnumType(self, ctx:LustreParser.EnumTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#arrayType.
    def visitArrayType(self, ctx:LustreParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#subrangeType.
    def visitSubrangeType(self, ctx:LustreParser.SubrangeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#userType.
    def visitUserType(self, ctx:LustreParser.UserTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#primitiveType.
    def visitPrimitiveType(self, ctx:LustreParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#bound.
    def visitBound(self, ctx:LustreParser.BoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#prop.
    def visitProp(self, ctx:LustreParser.PropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#realizabilityInputs.
    def visitRealizabilityInputs(self, ctx:LustreParser.RealizabilityInputsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#ivc.
    def visitIvc(self, ctx:LustreParser.IvcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#main.
    def visitMain(self, ctx:LustreParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#assertion.
    def visitAssertion(self, ctx:LustreParser.AssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#equation.
    def visitEquation(self, ctx:LustreParser.EquationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#lhs.
    def visitLhs(self, ctx:LustreParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#recordExpr.
    def visitRecordExpr(self, ctx:LustreParser.RecordExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#intExpr.
    def visitIntExpr(self, ctx:LustreParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#arrayExpr.
    def visitArrayExpr(self, ctx:LustreParser.ArrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#castExpr.
    def visitCastExpr(self, ctx:LustreParser.CastExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#realExpr.
    def visitRealExpr(self, ctx:LustreParser.RealExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#ifThenElseExpr.
    def visitIfThenElseExpr(self, ctx:LustreParser.IfThenElseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#binaryExpr.
    def visitBinaryExpr(self, ctx:LustreParser.BinaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#preExpr.
    def visitPreExpr(self, ctx:LustreParser.PreExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#initCurrExpr.
    def visitInitCurrExpr(self, ctx:LustreParser.InitCurrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#nodeCallExpr.
    def visitNodeCallExpr(self, ctx:LustreParser.NodeCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#recordAccessExpr.
    def visitRecordAccessExpr(self, ctx:LustreParser.RecordAccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#negateExpr.
    def visitNegateExpr(self, ctx:LustreParser.NegateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#condactExpr.
    def visitCondactExpr(self, ctx:LustreParser.CondactExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#notExpr.
    def visitNotExpr(self, ctx:LustreParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#arrayAccessExpr.
    def visitArrayAccessExpr(self, ctx:LustreParser.ArrayAccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#arrayUpdateExpr.
    def visitArrayUpdateExpr(self, ctx:LustreParser.ArrayUpdateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#boolExpr.
    def visitBoolExpr(self, ctx:LustreParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#tupleExpr.
    def visitTupleExpr(self, ctx:LustreParser.TupleExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#recordUpdateExpr.
    def visitRecordUpdateExpr(self, ctx:LustreParser.RecordUpdateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#idExpr.
    def visitIdExpr(self, ctx:LustreParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#baseEID.
    def visitBaseEID(self, ctx:LustreParser.BaseEIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#arrayEID.
    def visitArrayEID(self, ctx:LustreParser.ArrayEIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LustreParser#recordEID.
    def visitRecordEID(self, ctx:LustreParser.RecordEIDContext):
        return self.visitChildren(ctx)



del LustreParser
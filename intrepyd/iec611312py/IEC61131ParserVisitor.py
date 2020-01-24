# Generated from IEC61131Parser.g4 by ANTLR 4.7.2
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by IEC61131ParserParser.

class IEC61131ParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IEC61131ParserParser#programDecl.
    def visitProgramDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#fbDecl.
    def visitFbDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#fb_std_names.
    def visitFb_std_names(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#bodyIL.
    def visitBodyIL(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#bodyST.
    def visitBodyST(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#variable_blocks.
    def visitVariable_blocks(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#varGlobalBlock.
    def visitVarGlobalBlock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#varLocalBlock.
    def visitVarLocalBlock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#varInputBlock.
    def visitVarInputBlock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#varOutputBlock.
    def visitVarOutputBlock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#varInOutBlock.
    def visitVarInOutBlock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#varExternalBlock.
    def visitVarExternalBlock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#variable_decls.
    def visitVariable_decls(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#varDeclInit.
    def visitVarDeclInit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#varDeclNoInit.
    def visitVarDeclNoInit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#varDeclRevLoc.
    def visitVarDeclRevLoc(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#located_at.
    def visitLocated_at(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#variable_init.
    def visitVariable_init(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#basicDataType.
    def visitBasicDataType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#timeDataType.
    def visitTimeDataType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#arrayDataType.
    def visitArrayDataType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#stdFbDataType.
    def visitStdFbDataType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#usrFbDataType.
    def visitUsrFbDataType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#instrFull.
    def visitInstrFull(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#instrLabel.
    def visitInstrLabel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#instrIlInstr.
    def visitInstrIlInstr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#label.
    def visitLabel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#ilInstrUnarySimple.
    def visitIlInstrUnarySimple(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#ilInstrUnaryExpr.
    def visitIlInstrUnaryExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#ilInstrZeroary.
    def visitIlInstrZeroary(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#ilInstrCall.
    def visitIlInstrCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#ilInstrJump.
    def visitIlInstrJump(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#ilInstrReturn.
    def visitIlInstrReturn(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#il_instr_op.
    def visitIl_instr_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#il_expr_uop.
    def visitIl_expr_uop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#il_expr_bop.
    def visitIl_expr_bop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#ilExprComplex.
    def visitIlExprComplex(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#ilExprSimple.
    def visitIlExprSimple(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#il_instruction_list.
    def visitIl_instruction_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#il_instruction_one.
    def visitIl_instruction_one(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#il_expr_simple.
    def visitIl_expr_simple(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#il_call_pars.
    def visitIl_call_pars(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#il_call_args.
    def visitIl_call_args(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#il_call_arg.
    def visitIl_call_arg(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#st_stmt.
    def visitSt_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#assignVariable.
    def visitAssignVariable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#assignArrayCell.
    def visitAssignArrayCell(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#assignBitAccess.
    def visitAssignBitAccess(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#assignCompositeAccess.
    def visitAssignCompositeAccess(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#if_stmt.
    def visitIf_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#if_simple_stmt.
    def visitIf_simple_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#if_elseif_stmt.
    def visitIf_elseif_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#if_else_stmt.
    def visitIf_else_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#if_complete_stmt.
    def visitIf_complete_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#elsif_stmt_list.
    def visitElsif_stmt_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#elsif_stmt.
    def visitElsif_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#else_stmt.
    def visitElse_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#stmt_block.
    def visitStmt_block(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#case_stmt.
    def visitCase_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#case_selections.
    def visitCase_selections(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#case_selection.
    def visitCase_selection(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#case_list.
    def visitCase_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#caseRange.
    def visitCaseRange(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#caseExpression.
    def visitCaseExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#iteration_stmt.
    def visitIteration_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#for_stmt.
    def visitFor_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#control_variable.
    def visitControl_variable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#for_list.
    def visitFor_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#while_stmt.
    def visitWhile_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#repeat_stmt.
    def visitRepeat_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#expression.
    def visitExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#unaryBoolExpression.
    def visitUnaryBoolExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#binaryBoolExpression.
    def visitBinaryBoolExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#parBoolExpression.
    def visitParBoolExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#leafBoolExpression.
    def visitLeafBoolExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#callBoolExpression.
    def visitCallBoolExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#callTermExpression.
    def visitCallTermExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#leafTermExpression.
    def visitLeafTermExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#unaryTermExpression.
    def visitUnaryTermExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#binaryTermExpression.
    def visitBinaryTermExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#parTermExpression.
    def visitParTermExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#customCallExpression.
    def visitCustomCallExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#func_param_init.
    def visitFunc_param_init(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#leaf_expression.
    def visitLeaf_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#constant.
    def visitConstant(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#numeric_literal.
    def visitNumeric_literal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#int_literal.
    def visitInt_literal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#uns_int.
    def visitUns_int(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#signed_int.
    def visitSigned_int(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#real_literal.
    def visitReal_literal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#bool_literal.
    def visitBool_literal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#time_literal.
    def visitTime_literal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#variable_name.
    def visitVariable_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#custom_func_name.
    def visitCustom_func_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#simple_var.
    def visitSimple_var(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#array_access.
    def visitArray_access(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#composite_access.
    def visitComposite_access(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#variable_bit_access.
    def visitVariable_bit_access(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#conversion_function.
    def visitConversion_function(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#std_func_name.
    def visitStd_func_name(self, ctx):
        return self.visitChildren(ctx)



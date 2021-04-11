# Generated from IEC61131Parser.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .IEC61131ParserParser import IEC61131ParserParser
else:
    from IEC61131ParserParser import IEC61131ParserParser

# This class defines a complete generic visitor for a parse tree produced by IEC61131ParserParser.

class IEC61131ParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IEC61131ParserParser#programDecl.
    def visitProgramDecl(self, ctx:IEC61131ParserParser.ProgramDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#fbDecl.
    def visitFbDecl(self, ctx:IEC61131ParserParser.FbDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#fb_std_names.
    def visitFb_std_names(self, ctx:IEC61131ParserParser.Fb_std_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#bodyIL.
    def visitBodyIL(self, ctx:IEC61131ParserParser.BodyILContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#bodyST.
    def visitBodyST(self, ctx:IEC61131ParserParser.BodySTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#variable_blocks.
    def visitVariable_blocks(self, ctx:IEC61131ParserParser.Variable_blocksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#varGlobalBlock.
    def visitVarGlobalBlock(self, ctx:IEC61131ParserParser.VarGlobalBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#varLocalBlock.
    def visitVarLocalBlock(self, ctx:IEC61131ParserParser.VarLocalBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#varInputBlock.
    def visitVarInputBlock(self, ctx:IEC61131ParserParser.VarInputBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#varOutputBlock.
    def visitVarOutputBlock(self, ctx:IEC61131ParserParser.VarOutputBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#varInOutBlock.
    def visitVarInOutBlock(self, ctx:IEC61131ParserParser.VarInOutBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#varExternalBlock.
    def visitVarExternalBlock(self, ctx:IEC61131ParserParser.VarExternalBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#variable_decls.
    def visitVariable_decls(self, ctx:IEC61131ParserParser.Variable_declsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#varDeclInit.
    def visitVarDeclInit(self, ctx:IEC61131ParserParser.VarDeclInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#varDeclNoInit.
    def visitVarDeclNoInit(self, ctx:IEC61131ParserParser.VarDeclNoInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#varDeclRevLoc.
    def visitVarDeclRevLoc(self, ctx:IEC61131ParserParser.VarDeclRevLocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#located_at.
    def visitLocated_at(self, ctx:IEC61131ParserParser.Located_atContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#variable_init.
    def visitVariable_init(self, ctx:IEC61131ParserParser.Variable_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#basicDataType.
    def visitBasicDataType(self, ctx:IEC61131ParserParser.BasicDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#timeDataType.
    def visitTimeDataType(self, ctx:IEC61131ParserParser.TimeDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#arrayDataType.
    def visitArrayDataType(self, ctx:IEC61131ParserParser.ArrayDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#stdFbDataType.
    def visitStdFbDataType(self, ctx:IEC61131ParserParser.StdFbDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#usrFbDataType.
    def visitUsrFbDataType(self, ctx:IEC61131ParserParser.UsrFbDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#instrFull.
    def visitInstrFull(self, ctx:IEC61131ParserParser.InstrFullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#instrLabel.
    def visitInstrLabel(self, ctx:IEC61131ParserParser.InstrLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#instrIlInstr.
    def visitInstrIlInstr(self, ctx:IEC61131ParserParser.InstrIlInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#label.
    def visitLabel(self, ctx:IEC61131ParserParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#ilInstrUnarySimple.
    def visitIlInstrUnarySimple(self, ctx:IEC61131ParserParser.IlInstrUnarySimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#ilInstrUnaryExpr.
    def visitIlInstrUnaryExpr(self, ctx:IEC61131ParserParser.IlInstrUnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#ilInstrZeroary.
    def visitIlInstrZeroary(self, ctx:IEC61131ParserParser.IlInstrZeroaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#ilInstrCall.
    def visitIlInstrCall(self, ctx:IEC61131ParserParser.IlInstrCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#ilInstrJump.
    def visitIlInstrJump(self, ctx:IEC61131ParserParser.IlInstrJumpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#ilInstrReturn.
    def visitIlInstrReturn(self, ctx:IEC61131ParserParser.IlInstrReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#il_instr_op.
    def visitIl_instr_op(self, ctx:IEC61131ParserParser.Il_instr_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#il_expr_uop.
    def visitIl_expr_uop(self, ctx:IEC61131ParserParser.Il_expr_uopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#il_expr_bop.
    def visitIl_expr_bop(self, ctx:IEC61131ParserParser.Il_expr_bopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#ilExprComplex.
    def visitIlExprComplex(self, ctx:IEC61131ParserParser.IlExprComplexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#ilExprSimple.
    def visitIlExprSimple(self, ctx:IEC61131ParserParser.IlExprSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#il_instruction_list.
    def visitIl_instruction_list(self, ctx:IEC61131ParserParser.Il_instruction_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#il_instruction_one.
    def visitIl_instruction_one(self, ctx:IEC61131ParserParser.Il_instruction_oneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#il_expr_simple.
    def visitIl_expr_simple(self, ctx:IEC61131ParserParser.Il_expr_simpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#il_call_pars.
    def visitIl_call_pars(self, ctx:IEC61131ParserParser.Il_call_parsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#il_call_args.
    def visitIl_call_args(self, ctx:IEC61131ParserParser.Il_call_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#il_call_arg.
    def visitIl_call_arg(self, ctx:IEC61131ParserParser.Il_call_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#st_stmt.
    def visitSt_stmt(self, ctx:IEC61131ParserParser.St_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#assignVariable.
    def visitAssignVariable(self, ctx:IEC61131ParserParser.AssignVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#assignArrayCell.
    def visitAssignArrayCell(self, ctx:IEC61131ParserParser.AssignArrayCellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#assignBitAccess.
    def visitAssignBitAccess(self, ctx:IEC61131ParserParser.AssignBitAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#assignCompositeAccess.
    def visitAssignCompositeAccess(self, ctx:IEC61131ParserParser.AssignCompositeAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#if_stmt.
    def visitIf_stmt(self, ctx:IEC61131ParserParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#if_simple_stmt.
    def visitIf_simple_stmt(self, ctx:IEC61131ParserParser.If_simple_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#if_elseif_stmt.
    def visitIf_elseif_stmt(self, ctx:IEC61131ParserParser.If_elseif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#if_else_stmt.
    def visitIf_else_stmt(self, ctx:IEC61131ParserParser.If_else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#if_complete_stmt.
    def visitIf_complete_stmt(self, ctx:IEC61131ParserParser.If_complete_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#elsif_stmt_list.
    def visitElsif_stmt_list(self, ctx:IEC61131ParserParser.Elsif_stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#elsif_stmt.
    def visitElsif_stmt(self, ctx:IEC61131ParserParser.Elsif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#else_stmt.
    def visitElse_stmt(self, ctx:IEC61131ParserParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#stmt_block.
    def visitStmt_block(self, ctx:IEC61131ParserParser.Stmt_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#case_stmt.
    def visitCase_stmt(self, ctx:IEC61131ParserParser.Case_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#case_selections.
    def visitCase_selections(self, ctx:IEC61131ParserParser.Case_selectionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#case_selection.
    def visitCase_selection(self, ctx:IEC61131ParserParser.Case_selectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#case_list.
    def visitCase_list(self, ctx:IEC61131ParserParser.Case_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#caseRange.
    def visitCaseRange(self, ctx:IEC61131ParserParser.CaseRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#caseExpression.
    def visitCaseExpression(self, ctx:IEC61131ParserParser.CaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#iteration_stmt.
    def visitIteration_stmt(self, ctx:IEC61131ParserParser.Iteration_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#for_stmt.
    def visitFor_stmt(self, ctx:IEC61131ParserParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#control_variable.
    def visitControl_variable(self, ctx:IEC61131ParserParser.Control_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#for_list.
    def visitFor_list(self, ctx:IEC61131ParserParser.For_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#while_stmt.
    def visitWhile_stmt(self, ctx:IEC61131ParserParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#repeat_stmt.
    def visitRepeat_stmt(self, ctx:IEC61131ParserParser.Repeat_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#expression.
    def visitExpression(self, ctx:IEC61131ParserParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#unaryBoolExpression.
    def visitUnaryBoolExpression(self, ctx:IEC61131ParserParser.UnaryBoolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#binaryBoolExpression.
    def visitBinaryBoolExpression(self, ctx:IEC61131ParserParser.BinaryBoolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#parBoolExpression.
    def visitParBoolExpression(self, ctx:IEC61131ParserParser.ParBoolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#leafBoolExpression.
    def visitLeafBoolExpression(self, ctx:IEC61131ParserParser.LeafBoolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#callBoolExpression.
    def visitCallBoolExpression(self, ctx:IEC61131ParserParser.CallBoolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#callTermExpression.
    def visitCallTermExpression(self, ctx:IEC61131ParserParser.CallTermExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#leafTermExpression.
    def visitLeafTermExpression(self, ctx:IEC61131ParserParser.LeafTermExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#unaryTermExpression.
    def visitUnaryTermExpression(self, ctx:IEC61131ParserParser.UnaryTermExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#binaryTermExpression.
    def visitBinaryTermExpression(self, ctx:IEC61131ParserParser.BinaryTermExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#parTermExpression.
    def visitParTermExpression(self, ctx:IEC61131ParserParser.ParTermExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#customCallExpression.
    def visitCustomCallExpression(self, ctx:IEC61131ParserParser.CustomCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#func_param_init.
    def visitFunc_param_init(self, ctx:IEC61131ParserParser.Func_param_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#leaf_expression.
    def visitLeaf_expression(self, ctx:IEC61131ParserParser.Leaf_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#constant.
    def visitConstant(self, ctx:IEC61131ParserParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#numeric_literal.
    def visitNumeric_literal(self, ctx:IEC61131ParserParser.Numeric_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#int_literal.
    def visitInt_literal(self, ctx:IEC61131ParserParser.Int_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#uns_int.
    def visitUns_int(self, ctx:IEC61131ParserParser.Uns_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#signed_int.
    def visitSigned_int(self, ctx:IEC61131ParserParser.Signed_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#real_literal.
    def visitReal_literal(self, ctx:IEC61131ParserParser.Real_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#bool_literal.
    def visitBool_literal(self, ctx:IEC61131ParserParser.Bool_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#time_literal.
    def visitTime_literal(self, ctx:IEC61131ParserParser.Time_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#variable_name.
    def visitVariable_name(self, ctx:IEC61131ParserParser.Variable_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#custom_func_name.
    def visitCustom_func_name(self, ctx:IEC61131ParserParser.Custom_func_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#simple_var.
    def visitSimple_var(self, ctx:IEC61131ParserParser.Simple_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#array_access.
    def visitArray_access(self, ctx:IEC61131ParserParser.Array_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#composite_access.
    def visitComposite_access(self, ctx:IEC61131ParserParser.Composite_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#variable_bit_access.
    def visitVariable_bit_access(self, ctx:IEC61131ParserParser.Variable_bit_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#conversion_function.
    def visitConversion_function(self, ctx:IEC61131ParserParser.Conversion_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IEC61131ParserParser#std_func_name.
    def visitStd_func_name(self, ctx:IEC61131ParserParser.Std_func_nameContext):
        return self.visitChildren(ctx)



del IEC61131ParserParser
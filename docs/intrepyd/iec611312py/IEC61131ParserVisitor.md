Module intrepyd.iec611312py.IEC61131ParserVisitor
=================================================

Classes
-------

`IEC61131ParserVisitor()`
:   

    ### Ancestors (in MRO)

    * antlr4.tree.Tree.ParseTreeVisitor

    ### Descendants

    * intrepyd.iec611312py.stmtbuilder.STMTBuilder

    ### Methods

    `visitArrayDataType(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.ArrayDataTypeContext)`
    :

    `visitArray_access(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Array_accessContext)`
    :

    `visitAssignArrayCell(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.AssignArrayCellContext)`
    :

    `visitAssignBitAccess(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.AssignBitAccessContext)`
    :

    `visitAssignCompositeAccess(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.AssignCompositeAccessContext)`
    :

    `visitAssignVariable(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.AssignVariableContext)`
    :

    `visitBasicDataType(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.BasicDataTypeContext)`
    :

    `visitBinaryBoolExpression(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.BinaryBoolExpressionContext)`
    :

    `visitBinaryTermExpression(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.BinaryTermExpressionContext)`
    :

    `visitBodyIL(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.BodyILContext)`
    :

    `visitBodyST(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.BodySTContext)`
    :

    `visitBool_literal(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Bool_literalContext)`
    :

    `visitCallBoolExpression(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.CallBoolExpressionContext)`
    :

    `visitCallTermExpression(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.CallTermExpressionContext)`
    :

    `visitCaseExpression(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.CaseExpressionContext)`
    :

    `visitCaseRange(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.CaseRangeContext)`
    :

    `visitCase_list(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Case_listContext)`
    :

    `visitCase_selection(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Case_selectionContext)`
    :

    `visitCase_selections(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Case_selectionsContext)`
    :

    `visitCase_stmt(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Case_stmtContext)`
    :

    `visitComposite_access(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Composite_accessContext)`
    :

    `visitConstant(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.ConstantContext)`
    :

    `visitControl_variable(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Control_variableContext)`
    :

    `visitConversion_function(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Conversion_functionContext)`
    :

    `visitCustomCallExpression(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.CustomCallExpressionContext)`
    :

    `visitCustom_func_name(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Custom_func_nameContext)`
    :

    `visitElse_stmt(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Else_stmtContext)`
    :

    `visitElsif_stmt(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Elsif_stmtContext)`
    :

    `visitElsif_stmt_list(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Elsif_stmt_listContext)`
    :

    `visitExpression(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.ExpressionContext)`
    :

    `visitFbDecl(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.FbDeclContext)`
    :

    `visitFb_std_names(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Fb_std_namesContext)`
    :

    `visitFor_list(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.For_listContext)`
    :

    `visitFor_stmt(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.For_stmtContext)`
    :

    `visitFunc_param_init(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Func_param_initContext)`
    :

    `visitIf_complete_stmt(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.If_complete_stmtContext)`
    :

    `visitIf_else_stmt(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.If_else_stmtContext)`
    :

    `visitIf_elseif_stmt(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.If_elseif_stmtContext)`
    :

    `visitIf_simple_stmt(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.If_simple_stmtContext)`
    :

    `visitIf_stmt(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.If_stmtContext)`
    :

    `visitIlExprComplex(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.IlExprComplexContext)`
    :

    `visitIlExprSimple(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.IlExprSimpleContext)`
    :

    `visitIlInstrCall(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.IlInstrCallContext)`
    :

    `visitIlInstrJump(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.IlInstrJumpContext)`
    :

    `visitIlInstrReturn(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.IlInstrReturnContext)`
    :

    `visitIlInstrUnaryExpr(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.IlInstrUnaryExprContext)`
    :

    `visitIlInstrUnarySimple(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.IlInstrUnarySimpleContext)`
    :

    `visitIlInstrZeroary(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.IlInstrZeroaryContext)`
    :

    `visitIl_call_arg(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Il_call_argContext)`
    :

    `visitIl_call_args(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Il_call_argsContext)`
    :

    `visitIl_call_pars(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Il_call_parsContext)`
    :

    `visitIl_expr_bop(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Il_expr_bopContext)`
    :

    `visitIl_expr_simple(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Il_expr_simpleContext)`
    :

    `visitIl_expr_uop(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Il_expr_uopContext)`
    :

    `visitIl_instr_op(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Il_instr_opContext)`
    :

    `visitIl_instruction_list(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Il_instruction_listContext)`
    :

    `visitIl_instruction_one(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Il_instruction_oneContext)`
    :

    `visitInstrFull(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.InstrFullContext)`
    :

    `visitInstrIlInstr(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.InstrIlInstrContext)`
    :

    `visitInstrLabel(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.InstrLabelContext)`
    :

    `visitInt_literal(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Int_literalContext)`
    :

    `visitIteration_stmt(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Iteration_stmtContext)`
    :

    `visitLabel(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.LabelContext)`
    :

    `visitLeafBoolExpression(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.LeafBoolExpressionContext)`
    :

    `visitLeafTermExpression(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.LeafTermExpressionContext)`
    :

    `visitLeaf_expression(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Leaf_expressionContext)`
    :

    `visitLocated_at(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Located_atContext)`
    :

    `visitNumeric_literal(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Numeric_literalContext)`
    :

    `visitParBoolExpression(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.ParBoolExpressionContext)`
    :

    `visitParTermExpression(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.ParTermExpressionContext)`
    :

    `visitProgramDecl(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.ProgramDeclContext)`
    :

    `visitReal_literal(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Real_literalContext)`
    :

    `visitRepeat_stmt(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Repeat_stmtContext)`
    :

    `visitSigned_int(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Signed_intContext)`
    :

    `visitSimple_var(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Simple_varContext)`
    :

    `visitSt_stmt(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.St_stmtContext)`
    :

    `visitStdFbDataType(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.StdFbDataTypeContext)`
    :

    `visitStd_func_name(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Std_func_nameContext)`
    :

    `visitStmt_block(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Stmt_blockContext)`
    :

    `visitTimeDataType(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.TimeDataTypeContext)`
    :

    `visitTime_literal(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Time_literalContext)`
    :

    `visitUnaryBoolExpression(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.UnaryBoolExpressionContext)`
    :

    `visitUnaryTermExpression(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.UnaryTermExpressionContext)`
    :

    `visitUns_int(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Uns_intContext)`
    :

    `visitUsrFbDataType(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.UsrFbDataTypeContext)`
    :

    `visitVarDeclInit(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.VarDeclInitContext)`
    :

    `visitVarDeclNoInit(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.VarDeclNoInitContext)`
    :

    `visitVarDeclRevLoc(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.VarDeclRevLocContext)`
    :

    `visitVarExternalBlock(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.VarExternalBlockContext)`
    :

    `visitVarGlobalBlock(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.VarGlobalBlockContext)`
    :

    `visitVarInOutBlock(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.VarInOutBlockContext)`
    :

    `visitVarInputBlock(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.VarInputBlockContext)`
    :

    `visitVarLocalBlock(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.VarLocalBlockContext)`
    :

    `visitVarOutputBlock(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.VarOutputBlockContext)`
    :

    `visitVariable_bit_access(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Variable_bit_accessContext)`
    :

    `visitVariable_blocks(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Variable_blocksContext)`
    :

    `visitVariable_decls(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Variable_declsContext)`
    :

    `visitVariable_init(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Variable_initContext)`
    :

    `visitVariable_name(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.Variable_nameContext)`
    :

    `visitWhile_stmt(self, ctx: intrepyd.iec611312py.IEC61131ParserParser.IEC61131ParserParser.While_stmtContext)`
    :
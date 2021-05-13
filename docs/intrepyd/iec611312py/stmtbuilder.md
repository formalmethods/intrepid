Module intrepyd.iec611312py.stmtbuilder
=======================================
This module implements the main parsing routine of IEC61131 text

Functions
---------

    
`computeCompositeDatatype(var, name2var)`
:   

    
`isNumber(text)`
:   

Classes
-------

`STMTBuilder(name2var, pou2inputs)`
:   Vistor that builds statements from the IEC program

    ### Ancestors (in MRO)

    * intrepyd.iec611312py.IEC61131ParserVisitor.IEC61131ParserVisitor
    * antlr4.tree.Tree.ParseTreeVisitor

    ### Instance variables

    `statements`
    :

    ### Methods

    `visitArray_access(self, ctx)`
    :

    `visitAssignCompositeAccess(self, ctx)`
    :

    `visitAssignVariable(self, ctx)`
    :

    `visitBinaryBoolExpression(self, ctx)`
    :

    `visitBinaryTermExpression(self, ctx)`
    :

    `visitBodyST(self, ctx)`
    :

    `visitCallBoolExpression(self, ctx)`
    :

    `visitCallTermExpression(self, ctx)`
    :

    `visitCaseExpression(self, ctx)`
    :

    `visitCaseRange(self, ctx)`
    :

    `visitCase_list(self, ctx)`
    :

    `visitCase_selection(self, ctx)`
    :

    `visitCase_selections(self, ctx)`
    :

    `visitCase_stmt(self, ctx)`
    :

    `visitComposite_access(self, ctx)`
    :

    `visitConstant(self, ctx)`
    :

    `visitCustomCallExpression(self, ctx)`
    :

    `visitElsif_stmt(self, ctx)`
    :

    `visitElsif_stmt_list(self, ctx)`
    :

    `visitExpression(self, ctx)`
    :

    `visitFunc_param_init(self, ctx)`
    :

    `visitIf_complete_stmt(self, ctx)`
    :

    `visitIf_else_stmt(self, ctx)`
    :

    `visitIf_elseif_stmt(self, ctx)`
    :

    `visitIf_simple_stmt(self, ctx)`
    :

    `visitIf_stmt(self, ctx)`
    :

    `visitLeafBoolExpression(self, ctx)`
    :

    `visitParBoolExpression(self, ctx)`
    :

    `visitParTermExpression(self, ctx)`
    :

    `visitSimple_var(self, ctx)`
    :

    `visitSt_stmt(self, ctx)`
    :

    `visitStmt_block(self, ctx)`
    :

    `visitUnaryBoolExpression(self, ctx)`
    :

    `visitUnaryTermExpression(self, ctx)`
    :

    `visitVariable_bit_access(self, ctx)`
    :

    `visit_stmt(self, ctx)`
    :
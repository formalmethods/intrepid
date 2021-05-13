Module intrepyd.lustre2py.astbuilder
====================================
This module implements the main parsing routine of Lustre files

Classes
-------

`ASTBuilder()`
:   Vistor that builds the internal AST for the
    Lustre program

    ### Ancestors (in MRO)

    * intrepyd.lustre2py.LustreVisitor.LustreVisitor
    * antlr4.tree.Tree.ParseTreeVisitor

    ### Instance variables

    `nodes`
    :   Getter

    ### Methods

    `visitArrayAccessExpr(self, ctx)`
    :

    `visitArrayEID(self, ctx)`
    :

    `visitArrayExpr(self, ctx)`
    :

    `visitArrayType(self, ctx)`
    :

    `visitAssertion(self, ctx)`
    :

    `visitBaseEID(self, ctx)`
    :

    `visitBinaryExpr(self, ctx)`
    :

    `visitBoolExpr(self, ctx)`
    :

    `visitCastExpr(self, ctx)`
    :

    `visitCondactExpr(self, ctx)`
    :

    `visitEnumType(self, ctx)`
    :

    `visitEquation(self, ctx)`
    :

    `visitIdExpr(self, ctx)`
    :

    `visitIfThenElseExpr(self, ctx)`
    :

    `visitInitCurrExpr(self, ctx)`
    :

    `visitIntExpr(self, ctx)`
    :

    `visitIvc(self, ctx)`
    :

    `visitLhs(self, ctx)`
    :

    `visitMain(self, ctx)`
    :

    `visitNegateExpr(self, ctx)`
    :

    `visitNode(self, ctx)`
    :

    `visitNodeCallExpr(self, ctx)`
    :

    `visitNotExpr(self, ctx)`
    :

    `visitPreExpr(self, ctx)`
    :

    `visitPrimitiveType(self, ctx)`
    :

    `visitProp(self, ctx)`
    :

    `visitRealExpr(self, ctx)`
    :

    `visitRealizabilityInputs(self, ctx)`
    :

    `visitRecordAccessExpr(self, ctx)`
    :

    `visitRecordEID(self, ctx)`
    :

    `visitRecordExpr(self, ctx)`
    :

    `visitRecordType(self, ctx)`
    :

    `visitSubrangeType(self, ctx)`
    :

    `visitTupleExpr(self, ctx)`
    :

    `visitUserType(self, ctx)`
    :

    `visitVarDeclGroup(self, ctx)`
    :

    `visitVarDeclList(self, ctx)`
    :
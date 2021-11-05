Module intrepyd.formula2py.formulabuilder
=========================================
This module implements the building of a formula

Classes
-------

`FormulaBuilder()`
:   This class implements a builder for a formula in string

    ### Ancestors (in MRO)

    * intrepyd.formula2py.FormulaVisitor.FormulaVisitor
    * antlr4.tree.Tree.ParseTreeVisitor

    ### Instance variables

    `formula`
    :   Gets the built formula

    ### Methods

    `visitAndExpr(self, ctx)`
    :

    `visitFormula(self, ctx: intrepyd.formula2py.FormulaParser.FormulaParser.FormulaContext)`
    :

    `visitNotExpr(self, ctx)`
    :

    `visitOrExpr(self, ctx)`
    :

    `visitParExpr(self, ctx)`
    :

    `visitParID(self, ctx: intrepyd.formula2py.FormulaParser.FormulaParser.ParIDContext)`
    :

    `visitPreExpr(self, ctx)`
    :
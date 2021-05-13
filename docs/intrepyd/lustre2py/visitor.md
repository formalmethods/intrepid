Module intrepyd.lustre2py.visitor
=================================
This module implements a generic vistor infrastructure

Classes
-------

`Visitor()`
:   Abstract visitor class

    ### Descendants

    * intrepyd.lustre2py.ast2intrepyd.Ast2Intrepyd
    * intrepyd.lustre2py.astprinter.AstPrinter

    ### Methods

    `visit(self, obj)`
    :   Dispatches visit to a proper method
Module intrepyd.iec611312py.visitor
===================================
This module implements a generic vistor infrastructure

Classes
-------

`Visitor()`
:   Abstract visitor class

    ### Descendants

    * intrepyd.iec611312py.flatstmt2intrepyd.FlatStmt2Intrepyd
    * intrepyd.iec611312py.inferdatatype.InferDatatypeBottomUp
    * intrepyd.iec611312py.inferdatatype.InferDatatypeTopDown
    * intrepyd.iec611312py.stmtprinter.StmtPrinter

    ### Methods

    `visit(self, obj)`
    :   Dispatches visit to a proper method
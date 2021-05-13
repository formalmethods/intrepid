Module intrepyd.iec611312py.flatstmt2intrepyd
=============================================
This module implements the translation from flat statements into intrepyd

Classes
-------

`FlatStmt2Intrepyd(indent, context, var2latch, outfile)`
:   Visitor for outputting the intrepyd equivalent of an AST

    ### Ancestors (in MRO)

    * intrepyd.iec611312py.visitor.Visitor

    ### Methods

    `process_statements(self, statements, process_latches=True)`
    :   Processes the given statements
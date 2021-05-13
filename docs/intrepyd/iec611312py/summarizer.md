Module intrepyd.iec611312py.summarizer
======================================
This module implements a summarizer for ST assignments

Classes
-------

`Summarizer()`
:   Summarizer for ST assignments

    ### Instance variables

    `assignments`
    :   Returns assignments

    ### Methods

    `substitute(self, rhs, summary)`
    :   Substitute

    `substitute_in_term(self, var, expression, term)`
    :   Substitute in term

    `summarize_stmt_block(self, block)`
    :   Summarizes a statement block
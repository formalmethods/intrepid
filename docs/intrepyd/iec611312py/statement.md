Module intrepyd.iec611312py.statement
=====================================
This module implements infrastructure to store statements

Classes
-------

`Assignment(lhs, rhs)`
:   Stores an assignment

    ### Ancestors (in MRO)

    * intrepyd.visitable.Visitable

    ### Instance variables

    `lhs`
    :   Getter

    `rhs`
    :   Getter

`Case(expression, selections, stmt_blocks)`
:   Stores a case statement

    ### Ancestors (in MRO)

    * intrepyd.visitable.Visitable

    ### Instance variables

    `expression`
    :   Getter

    `selections`
    :   Getter

    `stmt_blocks`
    :   Getter

`IfThenElse(conditions, stmt_blocks)`
:   Stores an if-then-else

    ### Ancestors (in MRO)

    * intrepyd.visitable.Visitable

    ### Instance variables

    `conditions`
    :   Getter

    `stmt_blocks`
    :   Getter
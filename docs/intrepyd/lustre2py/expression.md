Module intrepyd.lustre2py.expression
====================================
This module implements infrastructure to store Lustre expressions

Classes
-------

`BinaryExpression(operator, left, right)`
:   Class for binary functions

    ### Ancestors (in MRO)

    * intrepyd.lustre2py.expression.Expression
    * intrepyd.visitable.Visitable

    ### Instance variables

    `left`
    :   Getter

    `operator`
    :   Getter

    `right`
    :   Getter

`CallExpression(cid, params)`
:   Class for node calls

    ### Ancestors (in MRO)

    * intrepyd.lustre2py.expression.Expression
    * intrepyd.visitable.Visitable

    ### Instance variables

    `cid`
    :   Getter

    `params`
    :   Getter

`Expression(kind)`
:   Abstract class for expressions

    ### Ancestors (in MRO)

    * intrepyd.visitable.Visitable

    ### Descendants

    * intrepyd.lustre2py.expression.BinaryExpression
    * intrepyd.lustre2py.expression.CallExpression
    * intrepyd.lustre2py.expression.ITEExpression
    * intrepyd.lustre2py.expression.InitCurrExpression
    * intrepyd.lustre2py.expression.LiteralExpression
    * intrepyd.lustre2py.expression.TupleExpression
    * intrepyd.lustre2py.expression.UnaryExpression
    * intrepyd.lustre2py.expression.ZeroaryExpression

    ### Class variables

    `BINARY`
    :

    `BOOL`
    :

    `CALL`
    :

    `INITCURR`
    :

    `INT`
    :

    `ITE`
    :

    `LITERAL`
    :

    `REAL`
    :

    `TUPLE`
    :

    `UNARY`
    :

    `ZEROARY`
    :

    ### Instance variables

    `kind`
    :   Getter

`ITEExpression(if_, then_, else_)`
:   Class for if then elses

    ### Ancestors (in MRO)

    * intrepyd.lustre2py.expression.Expression
    * intrepyd.visitable.Visitable

    ### Instance variables

    `else_`
    :   Getter

    `if_`
    :   Getter

    `then_`
    :   Getter

`InitCurrExpression(init, curr)`
:   Class for init curr

    ### Ancestors (in MRO)

    * intrepyd.lustre2py.expression.Expression
    * intrepyd.visitable.Visitable

    ### Instance variables

    `curr`
    :   Getter

    `init`
    :   Getter

`LiteralExpression(value, datatype)`
:   Class for numeric or boolean literals

    ### Ancestors (in MRO)

    * intrepyd.lustre2py.expression.Expression
    * intrepyd.visitable.Visitable

    ### Instance variables

    `datatype`
    :   Getter

    `value`
    :   Getter

`TupleExpression(expressions)`
:   Class for tuples

    ### Ancestors (in MRO)

    * intrepyd.lustre2py.expression.Expression
    * intrepyd.visitable.Visitable

    ### Instance variables

    `expressions`
    :   Getter

`UnaryExpression(operator, operand)`
:   Class for unary functions

    ### Ancestors (in MRO)

    * intrepyd.lustre2py.expression.Expression
    * intrepyd.visitable.Visitable

    ### Instance variables

    `operand`
    :   Getter

    `operator`
    :   Getter

`ZeroaryExpression(name)`
:   Class for zero-arity functions

    ### Ancestors (in MRO)

    * intrepyd.lustre2py.expression.Expression
    * intrepyd.visitable.Visitable

    ### Instance variables

    `name`
    :   Getter
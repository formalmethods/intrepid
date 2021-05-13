Module intrepyd.iec611312py.expression
======================================
This module implements infrastructure to store expressions

Classes
-------

`ConstantOcc(cst)`
:   Stores a constant occurrence

    ### Ancestors (in MRO)

    * intrepyd.iec611312py.expression.ExpressionBase
    * intrepyd.visitable.Visitable

    ### Instance variables

    `cst`
    :   Getter

`Expression(operator, arguments)`
:   Base class for expressions

    ### Ancestors (in MRO)

    * intrepyd.iec611312py.expression.ExpressionBase
    * intrepyd.visitable.Visitable

    ### Instance variables

    `arguments`
    :   Returns arguments

    `operator`
    :   Returns operator

`ExpressionBase()`
:   Base class for expressions

    ### Ancestors (in MRO)

    * intrepyd.visitable.Visitable

    ### Descendants

    * intrepyd.iec611312py.expression.ConstantOcc
    * intrepyd.iec611312py.expression.Expression
    * intrepyd.iec611312py.expression.FunctionOcc
    * intrepyd.iec611312py.expression.Ite
    * intrepyd.iec611312py.expression.ParamInit
    * intrepyd.iec611312py.expression.Range
    * intrepyd.iec611312py.expression.VariableOcc

    ### Instance variables

    `datatype`
    :   Return the datatype

`FunctionOcc(name, param_inits)`
:   A function call occurrence

    ### Ancestors (in MRO)

    * intrepyd.iec611312py.expression.ExpressionBase
    * intrepyd.visitable.Visitable

    ### Instance variables

    `name`
    :   Return name

    `param_inits`
    :   Return param inits

`Ite(condition, then_term, else_term)`
:   Term If-then-else. This construct does not exist in ST language. It is used
    as intermediate step before translating into intrepyd

    ### Ancestors (in MRO)

    * intrepyd.iec611312py.expression.ExpressionBase
    * intrepyd.visitable.Visitable

    ### Instance variables

    `condition`
    :   Return condition term

    `else_term`
    :   Return else term

    `then_term`
    :   Return then term

`ParamInit(lhs, rhs)`
:   Holds a parameter initialization for function calls

    ### Ancestors (in MRO)

    * intrepyd.iec611312py.expression.ExpressionBase
    * intrepyd.visitable.Visitable

    ### Instance variables

    `lhs`
    :   Returns the lhs

    `rhs`
    :   Returns the rhs

`Range(first, last)`
:   A range

    ### Ancestors (in MRO)

    * intrepyd.iec611312py.expression.ExpressionBase
    * intrepyd.visitable.Visitable

`VariableOcc(var)`
:   Stores a variable occurrence

    ### Ancestors (in MRO)

    * intrepyd.iec611312py.expression.ExpressionBase
    * intrepyd.visitable.Visitable

    ### Instance variables

    `var`
    :   Getter
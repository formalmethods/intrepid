Module intrepyd.visitable
=========================
This module implements a simple visitable decorator

Classes
-------

`Visitable()`
:   Implementation of a base class that adds
    the capability of being visited by a visitor

    ### Descendants

    * intrepyd.iec611312py.datatype.Datatype
    * intrepyd.iec611312py.expression.ExpressionBase
    * intrepyd.iec611312py.statement.Assignment
    * intrepyd.iec611312py.statement.Case
    * intrepyd.iec611312py.statement.IfThenElse
    * intrepyd.iec611312py.variable.Variable
    * intrepyd.lustre2py.datatype.Datatype
    * intrepyd.lustre2py.expression.Expression
    * intrepyd.lustre2py.instruction.Instruction
    * intrepyd.lustre2py.node.Node
    * intrepyd.lustre2py.variable.VarDeclGroup

    ### Methods

    `accept(self, visitor)`
    :   Function to be called to trigger a visitor
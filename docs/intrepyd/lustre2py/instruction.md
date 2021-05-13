Module intrepyd.lustre2py.instruction
=====================================
This module implements infrastructure to store instructions

Classes
-------

`Equation(lhs, expression)`
:   Class for representing equations

    ### Ancestors (in MRO)

    * intrepyd.lustre2py.instruction.Instruction
    * intrepyd.visitable.Visitable

    ### Instance variables

    `expression`
    :   Getter

    `lhs`
    :   Getter

    ### Methods

    `push_pre(self)`
    :   Push pre to variables

`Instruction(kind)`
:   Abstract class that stores instructions

    ### Ancestors (in MRO)

    * intrepyd.visitable.Visitable

    ### Descendants

    * intrepyd.lustre2py.instruction.Equation
    * intrepyd.lustre2py.instruction.Ivc
    * intrepyd.lustre2py.instruction.Property
    * intrepyd.lustre2py.instruction.RealInputs

    ### Class variables

    `ASSERTION`
    :

    `EQUATION`
    :

    `IVC`
    :

    `MAIN`
    :

    `PROPERTY`
    :

    `REAL_INPUTS`
    :

`Ivc(ids)`
:   Class for representing ivcs

    ### Ancestors (in MRO)

    * intrepyd.lustre2py.instruction.Instruction
    * intrepyd.visitable.Visitable

`Property(expr)`
:   Class for representing properties

    ### Ancestors (in MRO)

    * intrepyd.lustre2py.instruction.Instruction
    * intrepyd.visitable.Visitable

`RealInputs(ids)`
:   Class for representing realizability inputs

    ### Ancestors (in MRO)

    * intrepyd.lustre2py.instruction.Instruction
    * intrepyd.visitable.Visitable
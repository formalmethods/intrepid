Module intrepyd.iec611312py.datatype
====================================
This module implements infrastructure to store datatypes

Classes
-------

`Array(dtname)`
:   Stores an array

    ### Ancestors (in MRO)

    * intrepyd.iec611312py.datatype.Datatype
    * intrepyd.visitable.Visitable

`Datatype(dtname)`
:   Stores a datatype

    ### Ancestors (in MRO)

    * intrepyd.visitable.Visitable

    ### Descendants

    * intrepyd.iec611312py.datatype.Array
    * intrepyd.iec611312py.datatype.Enum
    * intrepyd.iec611312py.datatype.Primitive
    * intrepyd.iec611312py.datatype.Struct
    * intrepyd.iec611312py.datatype.Subrange
    * intrepyd.iec611312py.function.Function
    * intrepyd.iec611312py.functionblock.FunctionBlock

    ### Static methods

    `add(name, datatype)`
    :   Adds a datatype

    `get(name)`
    :   Get a datatype

    `is_primitive(dtname)`
    :   Check if type is primitive

    ### Instance variables

    `dtname`
    :   Getter

`Enum(dtname)`
:   Stores an enum

    ### Ancestors (in MRO)

    * intrepyd.iec611312py.datatype.Datatype
    * intrepyd.visitable.Visitable

`Primitive(dtname)`
:   Stores a primitive datatype (SINT, USINT, ..., REAL, ...)

    ### Ancestors (in MRO)

    * intrepyd.iec611312py.datatype.Datatype
    * intrepyd.visitable.Visitable

`Struct(name, fields)`
:   Stores a struct

    ### Ancestors (in MRO)

    * intrepyd.iec611312py.datatype.Datatype
    * intrepyd.visitable.Visitable

    ### Instance variables

    `fields`
    :   Return the fields

`Subrange(dtname)`
:   Stores a subrange

    ### Ancestors (in MRO)

    * intrepyd.iec611312py.datatype.Datatype
    * intrepyd.visitable.Visitable
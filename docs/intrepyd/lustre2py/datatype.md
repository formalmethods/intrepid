Module intrepyd.lustre2py.datatype
==================================
This module implements infrastructure to store datatypes

Classes
-------

`Array(kind)`
:   Stores an array

    ### Ancestors (in MRO)

    * intrepyd.lustre2py.datatype.Datatype
    * intrepyd.visitable.Visitable

`Datatype(kind)`
:   Stores a datatype

    ### Ancestors (in MRO)

    * intrepyd.visitable.Visitable

    ### Descendants

    * intrepyd.lustre2py.datatype.Array
    * intrepyd.lustre2py.datatype.Enum
    * intrepyd.lustre2py.datatype.Primitive
    * intrepyd.lustre2py.datatype.Struct
    * intrepyd.lustre2py.datatype.Subrange

    ### Class variables

    `ARRAY`
    :

    `ENUM`
    :

    `PRIMITIVE`
    :

    `STRUCT`
    :

    `SUBRANGE`
    :

`Enum(kind)`
:   Stores an enum

    ### Ancestors (in MRO)

    * intrepyd.lustre2py.datatype.Datatype
    * intrepyd.visitable.Visitable

`Primitive(name)`
:   Stores a primitive datatype (int, real, bool)

    ### Ancestors (in MRO)

    * intrepyd.lustre2py.datatype.Datatype
    * intrepyd.visitable.Visitable

    ### Instance variables

    `name`
    :   Getter

`Struct(kind)`
:   Stores a struct

    ### Ancestors (in MRO)

    * intrepyd.lustre2py.datatype.Datatype
    * intrepyd.visitable.Visitable

`Subrange(kind)`
:   Stores a subrange

    ### Ancestors (in MRO)

    * intrepyd.lustre2py.datatype.Datatype
    * intrepyd.visitable.Visitable
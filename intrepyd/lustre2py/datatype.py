"""
This module implements infrastructure to store datatypes
"""

from intrepyd.visitable import Visitable

class Datatype(Visitable):
    """
    Stores a datatype
    """
    def __init__(self, kind):
        self._kind = kind

    PRIMITIVE = 'PRIMITIVE'
    ARRAY = 'ARRAY'
    STRUCT = 'STRUCT'
    ENUM = 'ENUM'
    SUBRANGE = 'SUBRANGE'

class Primitive(Datatype):
    """
    Stores a primitive datatype (int, real, bool)
    """
    def __init__(self, name):
        Datatype.__init__(self, Datatype.PRIMITIVE)
        self._name = name

    @property
    def name(self):
        """
        Getter
        """
        return self._name

class Array(Datatype):
    """
    Stores an array
    """

class Struct(Datatype):
    """
    Stores a struct
    """

class Enum(Datatype):
    """
    Stores an enum
    """

class Subrange(Datatype):
    """
    Stores a subrange
    """

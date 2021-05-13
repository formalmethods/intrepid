"""
This module implements infrastructure to store datatypes
"""

from intrepyd.visitable import Visitable

PRIMITIVEDATATYPES = {
    'BOOL',
    'INT',
    'UINT',
    'SINT',
    'USINT',
    'DINT',
    'UDINT',
    'REAL',
    'LREAL',
}

class Datatype(Visitable):
    """
    Stores a datatype
    """

    _name2datatype = {}
    def __init__(self, dtname):
        self._dtname = dtname

    # def __eq__(self, other):
    #     raise NotImplementedError

    # def __ne__(self, other):
    #     raise NotImplementedError

    @property
    def dtname(self):
        """
        Getter
        """
        return self._dtname

    @staticmethod
    def add(name, datatype):
        """
        Adds a datatype
        """
        Datatype._name2datatype[name] = datatype

    @staticmethod
    def get(name):
        """
        Get a datatype
        """
        return Datatype._name2datatype[name]

    @staticmethod
    def is_primitive(dtname):
        """
        Check if type is primitive
        """
        return dtname in PRIMITIVEDATATYPES

class Primitive(Datatype):
    """
    Stores a primitive datatype (SINT, USINT, ..., REAL, ...)
    """
    def __init__(self, dtname):
        Datatype.__init__(self, dtname)

    def __eq__(self, other):
        return self.dtname == other.dtname

    def __ne__(self, other):
        return self.dtname != other.dtname

class Array(Datatype):
    """
    Stores an array
    """

class Struct(Datatype):
    """
    Stores a struct
    """
    def __init__(self, name, fields):
        Datatype.__init__(self, name)
        self._fields = fields

    @property
    def fields(self):
        """
        Return the fields
        """
        return self._fields

class Enum(Datatype):
    """
    Stores an enum
    """

class Subrange(Datatype):
    """
    Stores a subrange
    """

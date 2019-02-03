"""
Copyright (C) 2018 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 01/11/2018

This module implements infrastructure to store datatypes
"""

from intrepyd.visitable import Visitable
import re

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

    _name2datatype = {}

    """
    Stores a datatype
    """
    def __init__(self, dtname):
        self._dtname = dtname

    def __eq__(self, other):
        raise NotImplementedError

    def __ne__(self, other):
        raise NotImplementedError

    @property
    def dtname(self):
        """
        Getter
        """
        return self._dtname

    @staticmethod
    def add(name, datatype):
        Datatype._name2datatype[name] = datatype

    @staticmethod
    def get(name):
        return Datatype._name2datatype[name]

    @staticmethod
    def isPrimitive(dtname):
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
    pass

class Struct(Datatype):
    """
    Stores a struct
    """
    def __init__(self, name, fields):
        Datatype.__init__(self, name)
        self._fields = fields

    @property
    def fields(self):
        return self._fields

class Enum(Datatype):
    """
    Stores an enum
    """
    pass

class Subrange(Datatype):
    """
    Stores a subrange
    """
    pass

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

class Datatype(Visitable):
    """
    Stores a datatype
    """
    def __init__(self, name, kind):
        self._name = name
        self._kind = kind

    @property
    def name(self):
        """
        Getter
        """
        return self._name

    PRIMITIVE = 'PRIMITIVE'
    FBLOCK = 'FBLOCK'
    ARRAY = 'ARRAY'
    STRUCT = 'STRUCT'
    ENUM = 'ENUM'
    SUBRANGE = 'SUBRANGE'
    INSTANCE = 'INSTANCE'

class Primitive(Datatype):
    """
    Stores a primitive datatype (SINT, USINT, ..., REAL, ...)
    """
    def __init__(self, name):
        Datatype.__init__(self, name, Datatype.PRIMITIVE)

class Instance(Datatype):
    """
    Stores a function block instance
    """
    def __init__(self, name, function_block):
        Datatype.__init__(self, name, Datatype.INSTANCE)
        self._function_block = function_block

    @property
    def function_block(self):
        """
        Getter
        """
        return self._function_block

class Array(Datatype):
    """
    Stores an array
    """
    pass

class Struct(Datatype):
    """
    Stores a struct
    """
    pass

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

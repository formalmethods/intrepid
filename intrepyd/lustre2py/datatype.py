"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017

This module implements infrastructure to store datatypes
"""

from intrepyd.lustre2py.visitable import Visitable

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

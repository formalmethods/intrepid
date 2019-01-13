"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 01/11/2018

This module implements infrastructure to store variables
"""

from intrepyd.visitable import Visitable

class Variable(Visitable):
    """
    Stores a variable
    """
    def __init__(self, name, datatype, kind):
        self._name = name
        self._datatype = datatype
        self._kind = kind

    @property
    def name(self):
        """
        Getter
        """
        return self._name

    @property
    def datatype(self):
        """
        Getter
        """
        return self._datatype

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'
    LOCAL = 'LOCAL'
    TEMP = 'TEMP'
    FIELD = 'FIELD'

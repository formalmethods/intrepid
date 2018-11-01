"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 01/04/2017

This module implements infrastructures for variables
"""

from intrepyd.visitable import Visitable

class VarDeclGroup(Visitable):
    """
    A variable declaration group
    """
    def __init__(self, variables, datatype):
        self._variables = variables
        self._datatype = datatype

    @property
    def variables(self):
        """
        Getter
        """
        return self._variables

    @property
    def datatype(self):
        """
        Getter
        """
        return self._datatype

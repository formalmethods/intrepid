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

class Assignment(Visitable):
    """
    Stores an assignment
    """
    def __init__(self, lhs, rhs):
        self._lhs = lhs
        self._rhs = rhs

    @property
    def lhs(self):
        """
        Getter
        """
        return self._lhs

    @property
    def rhs(self):
        """
        Getter
        """
        return self._rhs

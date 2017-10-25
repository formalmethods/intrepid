"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 01/04/2017

This module implements a basic AST node
"""

class Ast(object):
    """
    Stores an AST
    """
    def __init__(self, nodes):
        self._nodes = nodes

    @property
    def nodes(self):
        """
        Getter
        """
        return self._nodes

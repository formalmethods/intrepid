"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017

This module implements a simple visitable decorator
"""

class Visitable(object):
    """
    Implementation of a base class that adds
    the capability of being visited by a visitor
    """
    def accept(self, visitor):
        """
        Function to be called to trigger a visitor
        """
        return visitor.visit(self)

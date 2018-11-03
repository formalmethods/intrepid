"""
Copyright (C) 2018 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 29/10/2018

This module implements the main store of a FunctionBlock
"""

from intrepyd.iec611312py.datatype import Datatype

class FunctionBlock(Datatype):
    """
    Holds function block parsed data
    """
    def __init__(self, name, input_vars, output_vars, temp_vars, assignments):
        Datatype.__init__(self, name, Datatype.FBLOCK)
        self._input_vars = input_vars
        self._output_vars = output_vars
        self._temp_vars = temp_vars
        self._assignments = assignments

    @property
    def input_vars(self):
        return self._input_vars

    @property
    def output_vars(self):
        return self._output_vars
    
    @property
    def assignments(self):
        return self._assignments

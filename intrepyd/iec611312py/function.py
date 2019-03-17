"""
Copyright (C) 2018 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 16/03/2019

This module implements the main store of a Function
"""

from intrepyd.iec611312py.datatype import Datatype

class Function(Datatype):
    """
    Holds function parsed data
    """
    def __init__(self, name, input_vars, output_vars, local_vars, statements):
        Datatype.__init__(self, name)
        self._input_vars = input_vars
        self._output_vars = output_vars
        self._local_vars = local_vars
        self._statements = statements

    @property
    def input_vars(self):
        return self._input_vars

    @property
    def output_vars(self):
        return self._output_vars

    @property
    def local_vars(self):
        return self._local_vars
    
    @property
    def statements(self):
        return self._statements

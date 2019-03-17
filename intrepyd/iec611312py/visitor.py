"""
Copyright (C) 2018 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 02/11/2018

This module implements a generic vistor infrastructure
"""

from intrepyd.iec611312py.statement import Assignment, IfThenElse, Case
from intrepyd.iec611312py.expression import VariableOcc, ConstantOcc, Expression, Ite, FunctionOcc, ParamInit

class Visitor(object):
    """
    Abstract visitor class
    """
    def visit(self, obj):
        """
        Dispatches visit to a proper method
        """
        if isinstance(obj, Assignment):
            return self._visit_assignment(obj)
        elif isinstance(obj, IfThenElse):
            return self._visit_ifthenelse(obj)
        elif isinstance(obj, Case):
            return self._visit_case(obj)
        elif isinstance(obj, Expression):
            return self._visit_expression(obj)
        elif isinstance(obj, VariableOcc):
            return self._visit_variable_occ(obj)
        elif isinstance(obj, ConstantOcc):
            return self._visit_constant_occ(obj)
        elif isinstance(obj, Ite):
            return self._visit_ite(obj)
        elif isinstance(obj, FunctionOcc):
            return self._visit_function_occ(obj)
        elif isinstance(obj, ParamInit):
            return self._visit_param_init(obj)
        raise TypeError('Type not found ' + str(type(obj)))

    def _visit_assignment(self, obj):
        """
        Visits Assignment
        """
        raise NotImplementedError

    def _visit_ite(self, obj):
        """
        Visits Ite
        """
        raise NotImplementedError

    def _visit_ifthenelse(self, obj):
        """
        Visits if-then-else
        """
        raise NotImplementedError

    def _visit_case(self, obj):
        """
        Visits case
        """
        raise NotImplementedError

    def _visit_expression(self, obj):
        """
        Visits Expression
        """
        raise NotImplementedError

    def _visit_variable_occ(self, obj):
        """
        Visits Variable occurrence
        """
        raise NotImplementedError

    def _visit_constant_occ(self, obj):
        """
        Visits Constant occurrence
        """
        raise NotImplementedError

    def _visit_function_occ(self, obj):
        """
        Visits Function call occurrence
        """
        raise NotImplementedError

    def _visit_param_init(self, obj):
        """
        Visits Param init occurrence
        """
        raise NotImplementedError

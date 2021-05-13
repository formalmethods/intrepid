"""
This module implements a generic vistor infrastructure
"""

from intrepyd.iec611312py.statement import Assignment, IfThenElse, Case
from intrepyd.iec611312py.expression import VariableOcc, ConstantOcc, Expression, Ite, FunctionOcc, ParamInit

class Visitor:
    """
    Abstract visitor class
    """
    def visit(self, obj):
        """
        Dispatches visit to a proper method
        """
        if isinstance(obj, Assignment):
            return self._visit_assignment(obj)
        if isinstance(obj, IfThenElse):
            return self._visit_ifthenelse(obj)
        if isinstance(obj, Case):
            return self._visit_case(obj)
        if isinstance(obj, Expression):
            return self._visit_expression(obj)
        if isinstance(obj, VariableOcc):
            return self._visit_variable_occ(obj)
        if isinstance(obj, ConstantOcc):
            return self._visit_constant_occ(obj)
        if isinstance(obj, Ite):
            return self._visit_ite(obj)
        if isinstance(obj, FunctionOcc):
            return self._visit_function_occ(obj)
        if isinstance(obj, ParamInit):
            return self._visit_param_init(obj)
        raise TypeError('Type not found ' + str(type(obj)))

    def _visit_assignment(self, obj):
        """
        Visits Assignment
        """
        raise NotImplementedError

    def _visit_ite(self, ite):
        """
        Visits Ite
        """
        raise NotImplementedError

    def _visit_ifthenelse(self, obj):
        """
        Visits if-then-else
        """
        raise NotImplementedError

    def _visit_case(self, case):
        """
        Visits case
        """
        raise NotImplementedError

    def _visit_expression(self, expression):
        """
        Visits Expression
        """
        raise NotImplementedError

    def _visit_variable_occ(self, variable_occ):
        """
        Visits Variable occurrence
        """
        raise NotImplementedError

    def _visit_constant_occ(self, constant_occ):
        """
        Visits Constant occurrence
        """
        raise NotImplementedError

    def _visit_function_occ(self, function_occ):
        """
        Visits Function call occurrence
        """
        raise NotImplementedError

    def _visit_param_init(self, obj):
        """
        Visits Param init occurrence
        """
        raise NotImplementedError

"""
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

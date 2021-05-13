"""
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
        """
        Returns the input vars
        """
        return self._input_vars

    @property
    def output_vars(self):
        """
        Returns the output vars
        """
        return self._output_vars

    @property
    def local_vars(self):
        """
        Returns the local vars
        """
        return self._local_vars

    @property
    def statements(self):
        """
        Returns the statements
        """
        return self._statements

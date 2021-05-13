"""
This module implements the main store of a FunctionBlock
"""

from intrepyd.iec611312py.datatype import Datatype

class FunctionBlock(Datatype):
    """
    Holds function block parsed data
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

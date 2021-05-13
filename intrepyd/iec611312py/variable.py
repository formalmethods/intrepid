"""
This module implements infrastructure to store variables
"""

from intrepyd.visitable import Visitable

class Variable(Visitable):
    """
    Stores a variable
    """
    def __init__(self, name, datatype, kind):
        self._name = name
        self._datatype = datatype
        self._kind = kind

    @property
    def name(self):
        """
        Getter
        """
        return self._name

    @property
    def datatype(self):
        """
        Getter
        """
        return self._datatype

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'
    LOCAL = 'LOCAL'
    TEMP = 'TEMP'
    FIELD = 'FIELD'

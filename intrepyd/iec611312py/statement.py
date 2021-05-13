"""
This module implements infrastructure to store statements
"""

from intrepyd.visitable import Visitable
from intrepyd.iec611312py.expression import TRUE

class Assignment(Visitable):
    """
    Stores an assignment
    """
    def __init__(self, lhs, rhs):
        self._lhs = lhs
        self._rhs = rhs

    @property
    def lhs(self):
        """
        Getter
        """
        return self._lhs

    @property
    def rhs(self):
        """
        Getter
        """
        return self._rhs

class IfThenElse(Visitable):
    """
    Stores an if-then-else
    """
    def __init__(self, conditions, stmt_blocks):
        self._conditions = conditions
        self._stmt_blocks = stmt_blocks
        if len(self._conditions) == len(self._stmt_blocks):
            return
        if len(self._conditions) == len(self._stmt_blocks) - 1:
            # chain with final else
            self._conditions.append(TRUE)
            return
        raise RuntimeError('Wrong number of conditions in if')

    @property
    def conditions(self):
        """
        Getter
        """
        return self._conditions

    @property
    def stmt_blocks(self):
        """
        Getter
        """
        return self._stmt_blocks

class Case(Visitable):
    """
    Stores a case statement
    """
    def __init__(self, expression, selections, stmt_blocks):
        self._expression = expression
        self._selections = selections
        self._stmt_blocks = stmt_blocks
        if len(self._selections) == len(self._stmt_blocks):
            return
        if len(self._selections) == len(self._stmt_blocks) - 1:
            # chain with final else
            self._selections.append(expression)
            return
        raise RuntimeError('Wrong number of conditions in case')

    @property
    def expression(self):
        """
        Getter
        """
        return self._expression

    @property
    def selections(self):
        """
        Getter
        """
        return self._selections

    @property
    def stmt_blocks(self):
        """
        Getter
        """
        return self._stmt_blocks

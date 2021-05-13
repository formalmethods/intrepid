"""
This module implements a simple visitable decorator
"""

class Visitable:
    """
    Implementation of a base class that adds
    the capability of being visited by a visitor
    """
    def accept(self, visitor):
        """
        Function to be called to trigger a visitor
        """
        return visitor.visit(self)

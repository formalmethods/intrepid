"""
This module implements a basic AST node
"""

class Ast:
    """
    Stores an AST
    """
    def __init__(self, nodes):
        self._nodes = nodes

    @property
    def nodes(self):
        """
        Getter
        """
        return self._nodes

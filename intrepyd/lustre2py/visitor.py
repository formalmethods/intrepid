"""
This module implements a generic vistor infrastructure
"""

from intrepyd.lustre2py.expression import ZeroaryExpression, UnaryExpression, BinaryExpression,\
                                          CallExpression, InitCurrExpression, ITEExpression,\
                                          LiteralExpression, TupleExpression
from intrepyd.lustre2py.instruction import Equation, Property
from intrepyd.lustre2py.node import Node
from intrepyd.lustre2py.variable import VarDeclGroup
from intrepyd.lustre2py.datatype import Primitive, Enum, Array, Struct, Subrange


class Visitor:
    """
    Abstract visitor class
    """
    def visit(self, obj):
        """
        Dispatches visit to a proper method
        """
        if isinstance(obj, ZeroaryExpression):
            return self._visit_zeroary_expression(obj)
        if isinstance(obj, UnaryExpression):
            return self._visit_unary_expression(obj)
        if isinstance(obj, BinaryExpression):
            return self._visit_binary_expression(obj)
        if isinstance(obj, CallExpression):
            return self._visit_call_expression(obj)
        if isinstance(obj, LiteralExpression):
            return self._visit_literal_expression(obj)
        if isinstance(obj, InitCurrExpression):
            return self._visit_init_curr_expression(obj)
        if isinstance(obj, ITEExpression):
            return self._visit_ite_expression(obj)
        if isinstance(obj, TupleExpression):
            return self._visit_tuple_expression(obj)
        if isinstance(obj, Equation):
            return self._visit_equation(obj)
        if isinstance(obj, Node):
            return self._visit_node(obj)
        if isinstance(obj, VarDeclGroup):
            return self._visit_var_decl_group(obj)
        if isinstance(obj, Primitive):
            return self._visit_primitive(obj)
        if isinstance(obj, Enum):
            return self._visit_enum(obj)
        if isinstance(obj, Struct):
            return self._visit_struct(obj)
        if isinstance(obj, Array):
            return self._visit_array(obj)
        if isinstance(obj, Subrange):
            return self._visit_subrange(obj)
        if isinstance(obj, Property):
            return self._visit_property(obj)
        raise TypeError('Type not found')

    def _visit_zeroary_expression(self, expr):
        raise NotImplementedError

    def _visit_unary_expression(self, expr):
        raise NotImplementedError

    def _visit_binary_expression(self, expr):
        raise NotImplementedError

    def _visit_call_expression(self, expr):
        raise NotImplementedError

    def _visit_literal_expression(self, expr):
        raise NotImplementedError

    def _visit_init_curr_expression(self, expr):
        raise NotImplementedError

    def _visit_ite_expression(self, expr):
        raise NotImplementedError

    def _visit_tuple_expression(self, ttuple):
        raise NotImplementedError

    def _visit_node(self, node):
        raise NotImplementedError

    def _visit_equation(self, equat):
        raise NotImplementedError

    def _visit_var_decl_group(self, grp):
        raise NotImplementedError

    def _visit_primitive(self, obj):
        raise NotImplementedError

    def _visit_enum(self, obj):
        raise NotImplementedError

    def _visit_struct(self, obj):
        raise NotImplementedError

    def _visit_array(self, obj):
        raise NotImplementedError

    def _visit_subrange(self, obj):
        raise NotImplementedError

    def _visit_property(self, obj):
        raise NotImplementedError

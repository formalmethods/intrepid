"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017

This module implements a generic vistor infrastructure
"""

from intrepyd.lustre2py.expression import ZeroaryExpression, UnaryExpression, BinaryExpression,\
                                          CallExpression, InitCurrExpression, ITEExpression,\
                                          LiteralExpression, TupleExpression
from intrepyd.lustre2py.instruction import Equation, Property
from intrepyd.lustre2py.node import Node
from intrepyd.lustre2py.variable import VarDeclGroup
from intrepyd.lustre2py.datatype import Primitive, Enum, Array, Struct, Subrange


class Visitor(object):
    """
    Abstract visitor class
    """
    def visit(self, obj):
        """
        Dispatches visit to a proper method
        """
        if isinstance(obj, ZeroaryExpression):
            return self._visit_zeroary_expression(obj)
        elif isinstance(obj, UnaryExpression):
            return self._visit_unary_expression(obj)
        elif isinstance(obj, BinaryExpression):
            return self._visit_binary_expression(obj)
        elif isinstance(obj, CallExpression):
            return self._visit_call_expression(obj)
        elif isinstance(obj, LiteralExpression):
            return self._visit_literal_expression(obj)
        elif isinstance(obj, InitCurrExpression):
            return self._visit_init_curr_expression(obj)
        elif isinstance(obj, ITEExpression):
            return self._visit_ite_expression(obj)
        elif isinstance(obj, TupleExpression):
            return self._visit_tuple_expression(obj)
        elif isinstance(obj, Equation):
            return self._visit_equation(obj)
        elif isinstance(obj, Node):
            return self._visit_node(obj)
        elif isinstance(obj, VarDeclGroup):
            return self._visit_var_decl_group(obj)
        elif isinstance(obj, Primitive):
            return self._visit_primitive(obj)
        elif isinstance(obj, Enum):
            return self._visit_enum(obj)
        elif isinstance(obj, Struct):
            return self._visit_struct(obj)
        elif isinstance(obj, Array):
            return self._visit_array(obj)
        elif isinstance(obj, Subrange):
            return self._visit_subrange(obj)
        elif isinstance(obj, Property):
            return self._visit_property(obj)
        raise TypeError('Type not found')

    def _visit_zeroary_expression(self, obj):
        """
        Visits ZeroaryExpression
        """
        raise NotImplementedError

    def _visit_unary_expression(self, obj):
        """
        Visits UnaryExpression
        """
        raise NotImplementedError

    def _visit_binary_expression(self, obj):
        """
        Visits BinaryExpression
        """
        raise NotImplementedError

    def _visit_call_expression(self, obj):
        """
        Visits CallExpression
        """
        raise NotImplementedError

    def _visit_literal_expression(self, obj):
        """
        Visits LiteralExpression
        """
        raise NotImplementedError

    def _visit_init_curr_expression(self, obj):
        """
        Visits InitCurrExpression
        """
        raise NotImplementedError

    def _visit_ite_expression(self, obj):
        """
        Visits ITEExpression
        """
        raise NotImplementedError

    def _visit_tuple_expression(self, obj):
        """
        Visits TupleExpression
        """
        raise NotImplementedError

    def _visit_node(self, obj):
        """
        Visits Node
        """
        raise NotImplementedError

    def _visit_equation(self, obj):
        """
        Visits Equation
        """
        raise NotImplementedError

    def _visit_var_decl_group(self, obj):
        """
        Visits Var decl group
        """
        raise NotImplementedError

    def _visit_primitive(self, obj):
        """
        Visits primitive datatype
        """
        raise NotImplementedError

    def _visit_enum(self, obj):
        """
        Visits enum dataype
        """
        raise NotImplementedError

    def _visit_struct(self, obj):
        """
        Visits struct datatype
        """
        raise NotImplementedError

    def _visit_array(self, obj):
        """
        Visits array datatype
        """
        raise NotImplementedError

    def _visit_subrange(self, obj):
        """
        Visits subrange datatype
        """
        raise NotImplementedError

    def _visit_property(self, obj):
        """
        Visits properties
        """
        raise NotImplementedError

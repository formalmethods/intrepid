"""
This module implements a printer for the parsed AST
"""

from intrepyd.lustre2py.visitor import Visitor
from intrepyd.lustre2py.node import Node
from intrepyd.lustre2py.instruction import Equation, Property

class AstPrinter(Visitor):
    """
    Visitor for printing AST on stdout
    """
    def __init__(self):
        pass

    def _visit_node(self, node):
        assert isinstance(node, Node)
        print('\nbegin node', node.name)
        if len(node.input_decls) > 0:
            print('\nbegin inputs')
            for inp in node.input_decls:
                inp.accept(self)
            print('end inputs')
        if len(node.output_decls) > 0:
            print('\nbegin outputs')
            for out in node.output_decls:
                out.accept(self)
            print('end outputs')
        if len(node.local_decls) > 0:
            print('\nbegin locals')
            for loc in node.local_decls:
                loc.accept(self)
            print('end locals')
        print('\nbegin equations')
        for equat in node.equations:
            print(equat.accept(self))
        print('end equations')
        if node.main:
            print('--%MAIN;')
        for prop in node.properties:
            print('--%PROPERTY', prop.accept(self) + ';')
        print('\nend node', node.name)

    def _visit_var_decl_list(self, lst):
        for grp in lst.var_decl_groups:
            grp.accept(self)

    def _visit_var_decl_group(self, grp):
        var_list = '\t'
        sep = ''
        for var in grp.variables:
            var_list += sep + var
            sep = ', '
        print(var_list, ':', grp.datatype.accept(self) + ';')

    def _visit_equation(self, equat):
        assert isinstance(equat, Equation)
        result = '\t'
        sep = ''
        put_par = len(equat.lhs) > 1
        if put_par:
            result += '('
        for lhs in equat.lhs:
            result += sep + lhs
            sep = ', '
        if put_par:
            result += ')'
        result += ' = '
        result += equat.expression.accept(self) + ';'
        return result

    def _visit_init_curr_expression(self, expr):
        result = expr.init.accept(self)
        result += ' -> '
        result += expr.curr.accept(self)
        return result

    def _visit_literal_expression(self, expr):
        return expr.value

    def _visit_zeroary_expression(self, expr):
        return expr.name

    def _visit_unary_expression(self, expr):
        result = expr.operator + ' '
        result += expr.operand.accept(self)
        return result

    def _visit_binary_expression(self, expr):
        result = expr.left.accept(self)
        result += ' ' + expr.operator + ' '
        result += expr.right.accept(self)
        return result

    def _visit_ite_expression(self, expr):
        result = 'if '
        result += expr.if_.accept(self)
        result += ' then '
        result += expr.then_.accept(self)
        result += ' else '
        result += expr.else_.accept(self)
        return result

    def _visit_call_expression(self, expr):
        result = expr.cid
        result += '('
        sep = ''
        for param in expr.params:
            result += sep + param.accept(self)
            sep = ', '
        result += ')'
        return result

    def _visit_primitive(self, obj):
        return obj.name

    def _visit_tuple_expression(self, ttuple):
        result = '('
        sep = ''
        for expr in ttuple.expressions:
            result += sep + expr.accept(self)
            sep = ', '
        result += ')'
        return result

    def _visit_enum(self, obj):
        raise NotImplementedError

    def _visit_struct(self, obj):
        raise NotImplementedError

    def _visit_array(self, obj):
        raise NotImplementedError

    def _visit_subrange(self, obj):
        raise NotImplementedError

    def _visit_property(self, obj):
        assert isinstance(obj, Property)
        return obj.expression.accept(self)

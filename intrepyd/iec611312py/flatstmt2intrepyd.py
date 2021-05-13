"""
This module implements the translation from flat statements into intrepyd
"""

import sys
from intrepyd.iec611312py.visitor import Visitor
from intrepyd.iec611312py.statement import Assignment
from intrepyd.iec611312py.utils import sanitize_name
from intrepyd.iec611312py.expression import TRUE, FALSE

STOP2INTREPYDUNARYOP = {
    '-' : 'mk_minus',
    'NOT' : 'mk_not',
    'TO_USINT': 'mk_cast_to_uint8',
    'TO_UINT': 'mk_cast_to_uint16',
    'TO_UDINT': 'mk_cast_to_uint32',
    'TO_SINT': 'mk_cast_to_int8',
    'TO_INT': 'mk_cast_to_int16',
    'TO_DINT': 'mk_cast_to_int32'
}

STOP2INTREPYDBINARYOP = {
    '+' : 'mk_add',
    '-' : 'mk_sub',
    '*' : 'mk_mul',
    '/' : 'mk_div',
    '=' : 'mk_eq',
    '<>' : 'mk_neq',
    '<' : 'mk_lt',
    '>' : 'mk_gt',
    '<=' : 'mk_leq',
    '>=' : 'mk_geq',
    'OR' : 'mk_or',
    'AND' : 'mk_and',
    'XOR' : 'mk_xor',
}

datatype2py = {
    'SINT' : 'int8',
    'USINT' : 'uint8',
    'INT' : 'int16',
    'UINT' : 'uint16',
    'DINT' : 'int32',
    'UDINT' : 'uint32',
    'LINT' : 'int64',
    'ULINT' : 'uint64',
    'REAL' : 'float32',
    'LREAL' : 'float64'
}

class FlatStmt2Intrepyd(Visitor):
    """
    Visitor for outputting the intrepyd equivalent of an AST
    """
    def __init__(self, indent, context, var2latch, outfile):
        self._indent = indent
        self._current_indent = 0
        self._count = 0
        self._var2latch = var2latch
        self._usedlatches = set()
        self._prefix = context + '.'
        self._outfile = outfile

    def process_statements(self, statements, process_latches = True):
        """
        Processes the given statements
        """
        self._inc_indent()
        for statement in statements:
            sys.stdout.flush()
            if not isinstance(statement, Assignment):
                raise RuntimeError('Expected Assignment, got ' + str(type(statement)))
            statement.accept(self)
        if not process_latches:
            return
        for name in self._var2latch:
            latch, init = self._var2latch[name]
            if latch in self._usedlatches:
                continue
            self._indent_result()
            self._outfile.write(self._prefix + 'set_latch_init_next(' +\
                                latch + ', ' +\
                                init + ', ' +\
                                latch + ')\n')

    def _indent_result(self):
        self._outfile.write(' ' * self._current_indent * self._indent)

    def _inc_indent(self):
        self._current_indent += 1

    def _dec_indent(self):
        self._current_indent -= 1

    def _get_tmp_var(self):
        self._count += 1
        return '__tmp_' + str(self._count)

    def _visit_assignment(self, obj):
        name = obj.lhs.var.name
        next_ = obj.rhs.accept(self)
        if name in self._var2latch:
            latch, init = self._var2latch[name]
            self._indent_result()
            self._outfile.write(self._prefix + 'set_latch_init_next(' +\
                                latch + ', ' +\
                                init + ', ' +\
                                next_ + ')')
            self._usedlatches.add(latch)
        else:
            self._indent_result()
            self._outfile.write(sanitize_name(name) + ' = ' + next_)
        self._outfile.write('\n')

    def _visit_expression(self, expression):
        result = self._get_tmp_var()
        args = expression.arguments
        nargs = len(args)
        result_args = []
        for arg in args:
            result_args.append(arg.accept(self))
        self._indent_result()
        self._outfile.write(result + ' = ')
        operator = expression.operator
        pos = operator.find('TO_')
        if pos != -1:
            operator = operator[pos:]
        if nargs == 1:
            if not operator in STOP2INTREPYDUNARYOP:
                raise RuntimeError('Could not handle unary op ' + operator)
            self._outfile.write(self._prefix + STOP2INTREPYDUNARYOP[operator] +\
                                '(' + result_args[0] + ')')
        elif nargs == 2:
            if not expression.operator in STOP2INTREPYDBINARYOP:
                raise RuntimeError('Could not handle binary op ' + expression.operator)
            self._outfile.write(self._prefix + STOP2INTREPYDBINARYOP[expression.operator] + '(' +\
                                result_args[0] + ', ' +\
                                result_args[1] + ')')
        else:
            raise RuntimeError('Could not handle op ' + expression.operator)
        self._outfile.write('\n')
        return result

    def _visit_ite(self, ite):
        i = ite.condition.accept(self)
        t = ite.then_term.accept(self)
        e = ite.else_term.accept(self)
        result = self._get_tmp_var()
        self._indent_result()
        self._outfile.write(result + ' = ' +\
                            self._prefix + 'mk_ite(' + i + ', ' + t + ', ' + e + ')\n')
        return result

    def _visit_variable_occ(self, variable_occ):
        return sanitize_name(variable_occ.var.name)

    def _visit_constant_occ(self, constant_occ):
        if constant_occ.cst == FALSE.cst:
            return self._prefix + 'mk_false()'
        if constant_occ.cst == TRUE.cst:
            return self._prefix + 'mk_true()'
        return self._prefix + 'mk_number("' + constant_occ.cst + '", ' +\
               self._prefix + 'mk_' + datatype2py[constant_occ.datatype.dtname] + '_type())'

    def _visit_function_occ(self, function_occ):
        params = ''
        sep = ''
        for param_init in function_occ.param_inits:
            params += sep + param_init.lhs + ' = ' + param_init.rhs.accept(self)
            sep = ', '
        result = self._get_tmp_var()
        self._indent_result()
        self._outfile.write(result + ' = self.' + function_occ.name + '(' + params + ')\n')
        return result

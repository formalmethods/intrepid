"""
Tests for stmt flattener
"""

import intrepyd
from intrepyd.iec611312py.plcopen import parse_plc_open_file
from intrepyd.iec611312py.parsest import parse_st
from intrepyd.iec611312py.variable import Variable
from intrepyd.iec611312py.flatstmt2intrepyd import FlatStmt2Intrepyd
from intrepyd.iec611312py.flattener import Flattener
from intrepyd.iec611312py.expression import VariableOcc, Ite
from intrepyd.iec611312py.statement import Assignment
from intrepyd.iec611312py.datatype import Primitive, Struct
from intrepyd.iec611312py.inferdatatype import InferDatatypeBottomUp, InferDatatypeTopDown
from intrepyd.iec611312py.stmtprinter import StmtPrinter
import io
import unittest

boolType = Primitive('BOOL')
intType = Primitive('INT')
usintType = Primitive('USINT')
FALSE = 'ctx.mk_false()'
TRUE = 'ctx.mk_true()'

class TestSTFlatStmt2Intrepyd(unittest.TestCase):
    def normalize_string(self, string):
        string = string.replace(' ', '')
        string = string.replace('\n', '')
        return string

    def _run_tests(self, program, name2var, var2latch, expected):
        statements = parse_st(program, name2var, {})
        flattener = Flattener()
        flattened_statements = flattener.flatten_stmt_block(statements)
        idbu = InferDatatypeBottomUp()
        idbu.process_statements(flattened_statements)
        idtd = InferDatatypeTopDown()
        idtd.process_statements(flattened_statements)
        stringio = io.StringIO()
        flatstmt2intrepyd = FlatStmt2Intrepyd(4, 'ctx', var2latch, stringio)
        flatstmt2intrepyd.process_statements(flattened_statements)
        self.assertEqual(self.normalize_string(expected),
                          self.normalize_string(stringio.getvalue()))

    def test_assignment_1(self):
        name2var = {
            'In1' : Variable('In1', boolType, Variable.INPUT),
            'In2' : Variable('In2', boolType, Variable.INPUT),
            'Out1' : Variable('Out1', boolType, Variable.OUTPUT)
        }
        program = 'Out1 := In1 AND In2;'
        expected = \
            """
            __tmp_1 = ctx.mk_and(In1, In2)
            Out1 = __tmp_1
            """
        self._run_tests(program, name2var, {}, expected)

    def test_assignment_2(self):
        name2var = {
            'a' : Variable('a', boolType, Variable.INPUT),
            'b' : Variable('b', boolType, Variable.INPUT),
            'c' : Variable('c', boolType, Variable.LOCAL),
        }
        program = 'c := a AND b;'
        expected = \
            """
            __tmp_1 = ctx.mk_and(a, b)
            ctx.set_latch_init_next(latch, ctx.mk_false(), __tmp_1)
            """
        self._run_tests(program, name2var, {'c': ('latch', FALSE)}, expected)

    def test_if_1(self):
        name2var = {
            'a' : Variable('a', boolType, Variable.LOCAL),
            'b' : Variable('b', boolType, Variable.LOCAL),
            'c' : Variable('c', boolType, Variable.LOCAL),
        }
        program = \
            """
            IF a THEN
                b := c;
            END_IF;
            """
        expected = \
            """
            __tmp_1 = ctx.mk_ite(a,c,b)
            b = __tmp_1
            """
        self._run_tests(program, name2var, {}, expected)

    def test_case_1(self):
        name2var = {
            'a' : Variable('a', intType, Variable.LOCAL),
            'b' : Variable('b', boolType, Variable.LOCAL),
            'c' : Variable('c', boolType, Variable.LOCAL),
        }

        program = \
            """
            CASE a OF
            0:
                b := c;
            END_CASE;
            """
        expected = \
            """
            __tmp_1 = ctx.mk_eq(a, ctx.mk_number("0", ctx.mk_int16_type()))
            __tmp_2 = ctx.mk_ite(__tmp_1,c,b)
            b = __tmp_2
            """
        self._run_tests(program, name2var, {}, expected)

    def test_case_2(self):

        name2var = {
            'a' : Variable('a', usintType, Variable.INPUT),
            'b' : Variable('b', usintType, Variable.LOCAL),
            'c' : Variable('c', usintType, Variable.OUTPUT),
        }

        program = \
            """
            CASE a OF
            0:
                b := 0;
            END_CASE;
            c := b;
            """
        expected = \
            """
            __tmp_1 = ctx.mk_eq(a,ctx.mk_number("0",ctx.mk_uint8_type()))
            __tmp_2 = ctx.mk_ite(__tmp_1,ctx.mk_number("0",ctx.mk_uint8_type()),b)
            b___1 = __tmp_2
            __tmp_3 = ctx.mk_eq(a,ctx.mk_number("0",ctx.mk_uint8_type()))
            __tmp_4 = ctx.mk_ite(__tmp_3,ctx.mk_number("0",ctx.mk_uint8_type()),b)
            b = __tmp_4
            c = b___1
            """
        self._run_tests(program, name2var, {}, expected)

if __name__ == '__main__':
    unittest.main()

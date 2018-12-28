"""
Copyright (C) 2018 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 04/11/2018
"""

import unittest
from intrepyd.iec611312py.parsest import parseST
from intrepyd.iec611312py.variable import Variable
from intrepyd.iec611312py.stmtprinter import StmtPrinter
from intrepyd.iec611312py.flattener import flattenStmtBlock
from intrepyd.iec611312py.expression import VariableOcc, Ite
from intrepyd.iec611312py.statement import Assignment
from intrepyd.iec611312py.datatype import Primitive, Struct

boolType = Primitive('BOOL')

class TestSTFlattener(unittest.TestCase):
    def _run_tests(self, program, name2var):
        statements = parseST(program[0], name2var)
        flattened_statements = flattenStmtBlock(statements)
        printer = StmtPrinter()
        printer.processStatements(flattened_statements)
        actual = printer.result
        expected = program[1]
        self.assertEquals(expected, actual)

    def test_assignment_1(self):
        name2var = {
            'In1' : Variable('In1', boolType, Variable.INPUT),
            'In2' : Variable('In2', boolType, Variable.INPUT),
            'In3' : Variable('In3', boolType, Variable.INPUT),
            'Out1' : Variable('Out1', boolType, Variable.OUTPUT)
        }
        program = (
            'Out1 := In1 AND In2;', 'Out1 := (In1 AND In2);'
        )
        self._run_tests(program, name2var)

    def test_assignment_2(self):
        name2var = {
            'a' : Variable('a', boolType, Variable.LOCAL),
            'b' : Variable('b', boolType, Variable.LOCAL),
            'c' : Variable('c', boolType, Variable.LOCAL),
            'd' : Variable('d', boolType, Variable.LOCAL)
        }
        program = (
            """
            a := b;
            c := d;
            """,
            'a := b;c := d;'
        )
        self._run_tests(program, name2var)

    def test_if_1(self):
        name2var = {
            'a' : Variable('a', boolType, Variable.LOCAL),
            'b' : Variable('b', boolType, Variable.LOCAL),
            'c' : Variable('c', boolType, Variable.LOCAL),
        }
        program = (
            """
            IF a THEN
                b := c;
            END_IF;
            """,
            'b := ite(a, c, b);'
        )
        self._run_tests(program, name2var)

    def test_if_2(self):
        name2var = {
            'a' : Variable('a', boolType, Variable.LOCAL),
            'b' : Variable('b', boolType, Variable.LOCAL),
            'c' : Variable('c', boolType, Variable.LOCAL),
            'd' : Variable('d', boolType, Variable.LOCAL),
        }
        program = (
            """
            IF a THEN
                b := c;
            ELSE
                b := d;
            END_IF;
            """,
            'b := ite(a, c, d);'
        )
        self._run_tests(program, name2var)

    def test_if_3(self):
        name2var = {
            'a' : Variable('a', boolType, Variable.LOCAL),
            'b' : Variable('b', boolType, Variable.LOCAL),
            'c' : Variable('c', boolType, Variable.LOCAL),
            'd' : Variable('d', boolType, Variable.LOCAL),
        }
        program = (
            """
            IF a THEN
                b := c;
            ELSE
                d := c;
            END_IF;
            """,
            'b := ite(a, c, b);d := ite(a, d, c);'
        )
        self._run_tests(program, name2var)

    def test_if_4(self):
        name2var = {
            'a' : Variable('a', boolType, Variable.LOCAL),
            'b' : Variable('b', boolType, Variable.LOCAL),
            'c' : Variable('c', boolType, Variable.LOCAL),
        }
        program = (
            """
            IF a THEN
                IF b THEN
                    b := c;
                END_IF;
            END_IF;
            """,
            'b := ite(a, ite(b, c, b), b);'
        )
        self._run_tests(program, name2var)

    def test_if_5(self):
        name2var = {
            'a' : Variable('a', boolType, Variable.LOCAL),
            'b' : Variable('b', boolType, Variable.LOCAL),
            'c' : Variable('c', boolType, Variable.LOCAL),
            'd' : Variable('d', boolType, Variable.LOCAL),
        }
        program = (
            """
            IF a THEN
                b := c;
            ELSE
                c := b;
            END_IF;
            """,
            ''
        )
        self._run_tests(program, name2var)

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
from intrepyd.iec611312py.summarizer import summarizeStmtBlock
from intrepyd.iec611312py.datatype import Primitive, Struct
from intrepyd.iec611312py.expression import VariableOcc, Ite
from intrepyd.iec611312py.statement import Assignment

boolType = Primitive('BOOL')

class TestSTSummarizer(unittest.TestCase):
    def _run_test(self, program, name2var, expected):
        statements = parseST(program, name2var)
        self._run_test_helper(statements, expected)

    def _run_test_helper(self, statements, expected):
        summary = summarizeStmtBlock(statements)
        actual = {}
        for assignment in summary:
            printer = StmtPrinter()
            assignment.rhs.accept(printer)
            actual[assignment.lhs.var.name] = printer.result
        self.assertEqual(expected, actual)

    def test_1(self):
        name2var = {
            'a' : Variable('a', boolType, Variable.LOCAL),
            'b' : Variable('b', boolType, Variable.LOCAL),
            'c' : Variable('c', boolType, Variable.LOCAL)
        }
        program = """
        a := TRUE;
        b := FALSE;
        c := a AND b;
        """
        expected = {
            'a': 'TRUE',
            'b': 'FALSE',
            'c': '(TRUE AND FALSE)'
        }
        self._run_test(program, name2var, expected)

    def test_2(self):
        name2var = {
            'a' : Variable('a', boolType, Variable.LOCAL),
            'b' : Variable('b', boolType, Variable.LOCAL),
            'c' : Variable('c', boolType, Variable.LOCAL)
        }
        program = """
        a := TRUE;
        b := FALSE;
        a := b;
        c := (a AND b);
        """
        expected = {
            'a': 'FALSE',
            'b': 'FALSE',
            'c': '(FALSE AND FALSE)'
        }
        self._run_test(program, name2var, expected)

    def test_3(self):
        name2var = {
            'a' : Variable('a', boolType, Variable.LOCAL),
            'b' : Variable('b', boolType, Variable.LOCAL),
            'c' : Variable('c', boolType, Variable.LOCAL)
        }
        program = """
        a := b;
        c := a;
        """
        expected = {
            'a': 'b',
            'c': 'b',
        }
        self._run_test(program, name2var, expected)

    def test_4(self):
        name2var = {
            'a' : Variable('a', boolType, Variable.LOCAL),
            'b' : Variable('b', boolType, Variable.LOCAL),
            'c' : Variable('c', boolType, Variable.LOCAL)
        }
        program = """
        a := b AND FALSE;
        c := a;
        a := c AND TRUE;
        """
        expected = {
            'a': '((b AND FALSE) AND TRUE)',
            'c': '(b AND FALSE)',
        }
        self._run_test(program, name2var, expected)

    def test_5(self):
        name2var = {
            'a' : VariableOcc(Variable('a', boolType, Variable.LOCAL)),
            'b' : VariableOcc(Variable('b', boolType, Variable.LOCAL)),
            'c' : VariableOcc(Variable('c', boolType, Variable.LOCAL)),
            'd' : VariableOcc(Variable('d', boolType, Variable.LOCAL)),
            'e' : VariableOcc(Variable('e', boolType, Variable.LOCAL)),
            'f' : VariableOcc(Variable('f', boolType, Variable.LOCAL))
        }
        statements = [
            Assignment(name2var['a'], Ite(name2var['b'], name2var['c'], name2var['d'])),
            Assignment(name2var['e'], name2var['a']),
            Assignment(name2var['f'], Ite(name2var['a'], name2var['a'], name2var['a'])),
        ]
        expected = {
            'a': 'ite(b, c, d)',
            'e': 'ite(b, c, d)',
            'f': 'ite(ite(b, c, d), ite(b, c, d), ite(b, c, d))',
        }
        self._run_test_helper(statements, expected)

    def test_6(self):
        name2var = {
            'a' : Variable('a', boolType, Variable.LOCAL),
            'b' : Variable('b', boolType, Variable.LOCAL),
            'c' : Variable('c', boolType, Variable.LOCAL)
        }
        program = """
        a := a AND b;
        """
        expected = {
            'a': '(a AND b)'
        }
        self._run_test(program, name2var, expected)

    def test_7(self):
        name2var = {
            'a' : VariableOcc(Variable('a', boolType, Variable.LOCAL)),
            'b' : VariableOcc(Variable('b', boolType, Variable.LOCAL)),
            'c' : VariableOcc(Variable('c', boolType, Variable.LOCAL)),
        }
        statements = [
            Assignment(name2var['a'], Ite(name2var['b'], name2var['a'], name2var['c']))
        ]
        expected = {
            'a': 'ite(b, a, c)',
        }
        self._run_test_helper(statements, expected)

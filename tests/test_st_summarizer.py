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
from intrepyd.iec611312py.summarizer import summarizeBlock
from intrepyd.iec611312py.datatype import Primitive, Struct

boolType = Primitive('BOOL')
intType = Primitive('INT')
usintType = Primitive('USINT')
uintType = Primitive('UINT')
dintType = Primitive('DINT')
udintType = Primitive('UDINT')

class TestSTSummarizer(unittest.TestCase):
    def _run_test(self, program, name2var, expected):
        statements = parseST(program, name2var)
        summary = summarizeBlock(statements)
        actual = {}
        for key, value in summary.iteritems():
            key_printer = StmtPrinter()
            key.accept(key_printer)
            key_str = key_printer.result
            value_printer = StmtPrinter()
            value.accept(value_printer)
            value_str = value_printer.result
            actual[key_str] = value_str
        self.assertEqual(expected, actual)

    def test_bool_1(self):
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



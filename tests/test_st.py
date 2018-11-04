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
from intrepyd.iec611312py.datatype import Datatype
from intrepyd.iec611312py.stmtprinter import StmtPrinter

boolType = Datatype('BOOL', 'PRIMITIVE')
intType = Datatype('INT', 'PRIMITIVE')

class TestST(unittest.TestCase):
    def _run_tests(self, programs, name2var):
        for prog in programs:
            statements = parseST(prog[0], name2var)
            self.assertEquals(1, len(statements))
            printer = StmtPrinter()
            printer.processStatements(statements)
            actual = printer.result
            expected = prog[1]
            self.assertEquals(expected, actual)

    def test_st_bool(self):
        name2var = {
            'In1' : Variable('In1', boolType, 'INPUT'),
            'In2' : Variable('In2', boolType, 'INPUT'),
            'In3' : Variable('In3', boolType, 'INPUT'),
            'Out1' : Variable('Out1', boolType, 'OUTPUT')
        }
        programs = [
            ['Out1 := In1 AND In2;',          'Out1 := (In1 AND In2);\n'],
            ['Out1 := In1 OR In2;',           'Out1 := (In1 OR In2);\n'],
            ['Out1 := In1 XOR In2;',          'Out1 := (In1 XOR In2);\n'],
            ['Out1 := NOT In1;',              'Out1 := NOT(In1);\n'],
            ['Out1 := (In1 AND In2);',        'Out1 := (In1 AND In2);\n'],
            ['Out1 := (In1 AND In2) OR In3;', 'Out1 := ((In1 AND In2) OR In3);\n'],
        ]
        self._run_tests(programs, name2var)

    def test_st_int(self):
        name2var = {
            'In1' : Variable('In1', intType, 'INPUT'),
            'In2' : Variable('In2', intType, 'INPUT'),
            'In3' : Variable('In3', intType, 'INPUT'),
            'Out1' : Variable('Out1', intType, 'OUTPUT')
        }
        programs = [
            ['Out1 := In1 + In2;',         'Out1 := (In1 + In2);\n'],
            ['Out1 := -In1;',              'Out1 := -(In1);\n'],
            ['Out1 := (In1 + In2) - In3;', 'Out1 := ((In1 + In2) - In3);\n'],
        ]
        self._run_tests(programs, name2var)

    def test_st_mixed(self):
        name2var = {
            'In1' : Variable('In1', intType, 'INPUT'),
            'In2' : Variable('In2', intType, 'INPUT'),
            'In3' : Variable('In3', boolType, 'INPUT'),
            'Out1' : Variable('Out1', boolType, 'OUTPUT'),
            'Out2' : Variable('Out2', intType, 'OUTPUT'),
        }
        programs = [
            ['Out1 := In1 < In2;',              'Out1 := (In1 < In2);\n'],
            ['Out1 := In1 = In2;',              'Out1 := (In1 = In2);\n'],
            ['Out1 := (In1 > In2) AND In3;',    'Out1 := ((In1 > In2) AND In3);\n'],
            ['Out1 := INT_TO_BOOL(In1 + In2);', 'Out1 := INT_TO_BOOL((In1 + In2));\n'],
            ['Out2 := BOOL_TO_INT(In3) + In1;', 'Out2 := (BOOL_TO_INT(In3) + In1);\n'],
        ]
        self._run_tests(programs, name2var)

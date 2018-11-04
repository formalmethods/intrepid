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

name2var = {
    'In1' : Variable('In1', boolType, 'INPUT'),
    'In2' : Variable('In2', boolType, 'INPUT'),
    'Out1' : Variable('Out1', boolType, 'OUTPUT')
}

programs = [
    ['Out1 := In1 AND In2;',   'Out1 := In1 AND In2;\n'],
    ['Out1 := In1 OR In2;',    'Out1 := In1 OR In2;\n'],
    ['Out1 := In1 XOR In2;',   'Out1 := In1 XOR In2;\n'],
    ['Out1 := NOT In1;',       'Out1 := NOT In1;\n'],
    ['Out1 := (In1 AND In2);', 'Out1 := In1 AND In2;\n'],
]

class TestST(unittest.TestCase):
    def test_st_01(self):
        for prog in programs:
            statements = parseST(prog[0], name2var)
            self.assertEquals(1, len(statements))
            printer = StmtPrinter()
            printer.processStatements(statements)
            actual = printer.result
            expected = prog[1]
            self.assertEquals(expected, actual)

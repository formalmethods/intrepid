"""
Copyright (C) 2019 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/01/2019
"""

import unittest
from intrepyd.iec611312py.stmtprinter import StmtPrinter
from intrepyd.iec611312py.expression import ConstantOcc, VariableOcc, Ite
from intrepyd.iec611312py.variable import Variable
from intrepyd.iec611312py.datatype import Primitive
from intrepyd.iec611312py.expression import Expression
from intrepyd.iec611312py.inferdatatype import InferDatatypeBottomUp, InferDatatypeTopDown
from intrepyd.iec611312py.statement import Assignment

boolType = Primitive('BOOL')
intType = Primitive('INT')

class TestSTInferDatatype(unittest.TestCase):
    def test_eq_1(self):
        a = Variable('a', intType, Variable.LOCAL)
        var = VariableOcc(a)
        cst = ConstantOcc('0')
        eq = Expression('=', [var, cst])
        idbu = InferDatatypeBottomUp()
        idbu.processStatements([eq])
        self.assertEqual(eq.datatype, boolType)
        idtd = InferDatatypeTopDown()
        idtd.processStatements([eq])
        self.assertEqual(cst.datatype, intType)

    def test_eq_2(self):
        a = Variable('a', intType, Variable.LOCAL)
        var = VariableOcc(a)
        cst = ConstantOcc('0')
        plus = Expression('+', [var, cst])
        idbu = InferDatatypeBottomUp()
        idbu.processStatements([plus])
        self.assertEqual(plus.datatype, intType)
        idtd = InferDatatypeTopDown()
        idtd.processStatements([plus])
        self.assertEqual(cst.datatype, intType)

    def test_eq_3(self):
        a = Variable('a', intType, Variable.LOCAL)
        var = VariableOcc(a)
        cst = ConstantOcc('0')
        assign = Assignment(var, cst)
        idbu = InferDatatypeBottomUp()
        idbu.processStatements([assign])
        idtd = InferDatatypeTopDown()
        idtd.processStatements([assign])
        self.assertEqual(cst.datatype, intType)

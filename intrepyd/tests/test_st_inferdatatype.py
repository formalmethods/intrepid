import unittest
from intrepyd.iec611312py.expression import ConstantOcc, VariableOcc
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
        idbu.process_statements([eq])
        self.assertEqual(eq.datatype, boolType)
        idtd = InferDatatypeTopDown()
        idtd.process_statements([eq])
        self.assertEqual(cst.datatype, intType)

    def test_eq_2(self):
        a = Variable('a', intType, Variable.LOCAL)
        var = VariableOcc(a)
        cst = ConstantOcc('0')
        plus = Expression('+', [var, cst])
        idbu = InferDatatypeBottomUp()
        idbu.process_statements([plus])
        self.assertEqual(plus.datatype, intType)
        idtd = InferDatatypeTopDown()
        idtd.process_statements([plus])
        self.assertEqual(cst.datatype, intType)

    def test_eq_3(self):
        a = Variable('a', intType, Variable.LOCAL)
        var = VariableOcc(a)
        cst = ConstantOcc('0')
        assign = Assignment(var, cst)
        idbu = InferDatatypeBottomUp()
        idbu.process_statements([assign])
        idtd = InferDatatypeTopDown()
        idtd.process_statements([assign])
        self.assertEqual(cst.datatype, intType)

if __name__ == "__main__":
    unittest.main()

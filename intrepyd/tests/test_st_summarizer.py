import unittest
from intrepyd.iec611312py.parsest import parse_st
from intrepyd.iec611312py.variable import Variable
from intrepyd.iec611312py.stmtprinter import StmtPrinter
from intrepyd.iec611312py.summarizer import Summarizer
from intrepyd.iec611312py.datatype import Primitive
from intrepyd.iec611312py.expression import VariableOcc, Ite
from intrepyd.iec611312py.statement import Assignment

boolType = Primitive('BOOL')

class TestSTSummarizer(unittest.TestCase):
    def _run_test(self, program, name2var, expected_assignments, expected_extra_assignments):
        statements = parse_st(program, name2var, {})
        self._run_test_helper(statements, expected_assignments, expected_extra_assignments)

    def _run_test_helper(self, statements, expected_assignments, expected_extra_assignments):
        summarizer = Summarizer()
        summary = summarizer.summarize_stmt_block(statements)
        actual = {}
        for assignment in summary:
            printer = StmtPrinter()
            assignment.rhs.accept(printer)
            actual[assignment.lhs.var.name] = printer.result
        self.assertEqual(expected_assignments, actual)
        actual = {}
        for assignment in summarizer.assignments:
            printer = StmtPrinter()
            assignment.rhs.accept(printer)
            actual[assignment.lhs.var.name] = printer.result
        self.assertEqual(expected_extra_assignments, actual)


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
        expected_assignments = {
            'a': 'TRUE',
            'b': 'FALSE',
            'c': '(a___1 AND b___2)'
        }
        expected_extra_assignments = {
            'a___1': 'TRUE',
            'b___2': 'FALSE'
        }
        self._run_test(program, name2var, expected_assignments, expected_extra_assignments)

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
        expected_assignments = {
            'a': 'b___1',
            'b': 'FALSE',
            'c': '(a___2 AND b___3)'
        }
        expected_extra_assignments = {
            'a___2': 'b___1',
            'b___1': 'FALSE',
            'b___3': 'FALSE'
        }
        self._run_test(program, name2var, expected_assignments, expected_extra_assignments)

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
        expected_assignments = {
            'a': 'b',
            'c': 'a___1',
        }
        expected_extra_assignments = {
            'a___1': 'b'
        }
        self._run_test(program, name2var, expected_assignments, expected_extra_assignments)

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
        expected_assignments = {
            'a': '(c___2 AND TRUE)',
            'c': 'a___1',
        }
        expected_extra_assignments = {
            'c___2': 'a___1',
            'a___1': '(b AND FALSE)'
        }
        self._run_test(program, name2var, expected_assignments, expected_extra_assignments)

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
        expected_assignments = {
            'a': 'ite(b, c, d)',
            'e': 'a___1',
            'f': 'ite(a___2, a___3, a___4)',
        }
        expected_extra_assignments = {
            'a___1': 'ite(b, c, d)',
            'a___2': 'ite(b, c, d)',
            'a___3': 'ite(b, c, d)',
            'a___4': 'ite(b, c, d)'
        }
        self._run_test_helper(statements, expected_assignments, expected_extra_assignments)

    def test_6(self):
        name2var = {
            'a' : Variable('a', boolType, Variable.LOCAL),
            'b' : Variable('b', boolType, Variable.LOCAL),
            'c' : Variable('c', boolType, Variable.LOCAL)
        }
        program = """
        a := a AND b;
        """
        expected_assignments = {
            'a': '(a AND b)'
        }
        self._run_test(program, name2var, expected_assignments, {})

    def test_7(self):
        name2var = {
            'a' : VariableOcc(Variable('a', boolType, Variable.LOCAL)),
            'b' : VariableOcc(Variable('b', boolType, Variable.LOCAL)),
            'c' : VariableOcc(Variable('c', boolType, Variable.LOCAL)),
        }
        statements = [
            Assignment(name2var['a'], Ite(name2var['b'], name2var['a'], name2var['c']))
        ]
        expected_assignments = {
            'a': 'ite(b, a, c)',
        }
        self._run_test_helper(statements, expected_assignments, {})

if __name__ == "__main__":
    unittest.main()

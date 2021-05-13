import unittest
from intrepyd.iec611312py.plcopen import parse_plc_open_file
from intrepyd.iec611312py.parsest import parse_st
from intrepyd.iec611312py.variable import Variable
from intrepyd.iec611312py.stmtprinter import StmtPrinter
from intrepyd.iec611312py.flattener import Flattener
from intrepyd.iec611312py.datatype import Primitive
from . import from_fixture_path

boolType = Primitive('BOOL')
intType = Primitive('INT')

class TestSTFlattener(unittest.TestCase):
    def _run_tests(self, program, name2var):
        statements = parse_st(program[0], name2var, {})
        flattener = Flattener()
        flattened_statements = flattener.flatten_stmt_block(statements)
        printer = StmtPrinter()
        printer.processStatements(flattened_statements)
        actual = printer.result
        expected = program[1]
        self.assertEqual(expected, actual)

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
            'd' : Variable('d', boolType, Variable.LOCAL)
        }
        program = (
            """
            IF a THEN
                b := c;
            ELSE
                c := b;
            END_IF;
            """,
            'b___1 := ite(a, c, b);b := ite(a, c, b);c := ite(a, c, b___1);'
        )
        self._run_tests(program, name2var)

    def test_case_1(self):
        name2var = {
            'a' : Variable('a', intType, Variable.LOCAL),
            'b' : Variable('b', boolType, Variable.LOCAL)
        }
        program = (
            """
            CASE a OF
            0:
                b := 0;
            1:
                b := 1;
            ELSE
                b := 2;
            END_CASE;
            """,
            'b := ite((a = 0), 0, ite((a = 1), 1, ite((a = a), 2, b)));'
        )
        self._run_tests(program, name2var)

    def test_integration_1(self):
        pous = parse_plc_open_file(from_fixture_path('openplc/simple1.xml'))
        self.assertEqual(1, len(pous))
        flattener = Flattener()
        flattened_statements = flattener.flatten_stmt_block(pous[0].statements)
        printer = StmtPrinter()
        printer.processStatements(flattened_statements)
        self.assertEqual('output1 := (local1 + input1);', printer.result)

    def test_integration_2(self):
        pous = parse_plc_open_file(from_fixture_path('openplc/if1.xml'))
        self.assertEqual(1, len(pous))
        flattener = Flattener()
        flattened_statements = flattener.flatten_stmt_block(pous[0].statements)
        printer = StmtPrinter()
        printer.processStatements(flattened_statements)
        self.assertEqual('c_is_active_c2_GPCA_SW_Logi := ite((c_is_active_c2_GPCA_SW_Logi = 0), 1, ite((c_is_c2_GPCA_SW_Logical_Arc = 1), 2, 3));',
                         printer.result)

if __name__ == "__main__":
    unittest.main()

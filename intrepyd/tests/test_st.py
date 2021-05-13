"""
Test for ST language
"""
from intrepyd.iec611312py.parsest import parse_st
from intrepyd.iec611312py.variable import Variable
from intrepyd.iec611312py.datatype import Primitive, Struct
from intrepyd.iec611312py.stmtprinter import StmtPrinter
import unittest

boolType = Primitive('BOOL')
intType = Primitive('INT')
usintType = Primitive('USINT')
uintType = Primitive('UINT')
dintType = Primitive('DINT')
udintType = Primitive('UDINT')

class TestST(unittest.TestCase):
    def _run_tests(self, programs, name2var):
        for prog in programs:
            statements = parse_st(prog[0], name2var, {})
            printer = StmtPrinter()
            printer.processStatements(statements)
            actual = printer.result
            expected = prog[1]
            self.assertEqual(expected, actual)

    def test_st_bool(self):
        name2var = {
            'In1' : Variable('In1', boolType, Variable.INPUT),
            'In2' : Variable('In2', boolType, Variable.INPUT),
            'In3' : Variable('In3', boolType, Variable.INPUT),
            'Out1' : Variable('Out1', boolType, Variable.OUTPUT)
        }
        programs = [
            ['Out1 := In1 AND In2;',          'Out1 := (In1 AND In2);'],
            ['Out1 := In1 OR In2;',           'Out1 := (In1 OR In2);'],
            ['Out1 := In1 XOR In2;',          'Out1 := (In1 XOR In2);'],
            ['Out1 := NOT In1;',              'Out1 := NOT(In1);'],
            ['Out1 := (In1 AND In2);',        'Out1 := (In1 AND In2);'],
            ['Out1 := (In1 AND In2) OR In3;', 'Out1 := ((In1 AND In2) OR In3);'],
        ]
        self._run_tests(programs, name2var)

    def test_st_int(self):
        name2var = {
            'In1' : Variable('In1', intType, Variable.INPUT),
            'In2' : Variable('In2', intType, Variable.INPUT),
            'In3' : Variable('In3', intType, Variable.INPUT),
            'Out1' : Variable('Out1', intType, Variable.OUTPUT)
        }
        programs = [
            ['Out1 := In1 + In2;',         'Out1 := (In1 + In2);'],
            ['Out1 := -In1;',              'Out1 := -(In1);'],
            ['Out1 := (In1 + In2) - In3;', 'Out1 := ((In1 + In2) - In3);'],
        ]
        self._run_tests(programs, name2var)

    def test_st_mixed(self):
        name2var = {
            'In1' : Variable('In1', intType, Variable.INPUT),
            'In2' : Variable('In2', intType, Variable.INPUT),
            'In3' : Variable('In3', boolType, Variable.INPUT),
            'Out1' : Variable('Out1', boolType, Variable.OUTPUT),
            'Out2' : Variable('Out2', intType, Variable.OUTPUT)
        }
        programs = [
            ['Out1 := In1 < In2;',              'Out1 := (In1 < In2);'],
            ['Out1 := In1 = In2;',              'Out1 := (In1 = In2);'],
            ['Out1 := (In1 > In2) AND In3;',    'Out1 := ((In1 > In2) AND In3);'],
            ['Out1 := INT_TO_BOOL(In1 + In2);', 'Out1 := INT_TO_BOOL((In1 + In2));'],
            ['Out2 := BOOL_TO_INT(In3) + In1;', 'Out2 := (BOOL_TO_INT(In3) + In1);'],
        ]
        self._run_tests(programs, name2var)

    def test_st_struct(self):
        myStruct = Struct('MyStruct', {
            'a': Variable('a', Primitive('INT'), Variable.FIELD),
            'b': Variable('b', Primitive('BOOL'), Variable.FIELD)
        })
        name2var = {
            'myInst' : Variable('MyStruct', myStruct, Variable.LOCAL)
        }
        programs = [
            ['myInst.a := 0;',    'myInst.a := 0;'],
            ['myInst.b := TRUE;', 'myInst.b := TRUE;']
        ]
        self._run_tests(programs, name2var)

    def test_st_if(self):
        name2var = {
            'is_IsAirInLine' : Variable('is_IsAirInLine', usintType, Variable.LOCAL),
            'rtb_Config_Timer' : Variable('rtb_Config_Timer', usintType, Variable.LOCAL),
            'b_s' : Variable('b_s', usintType, Variable.LOCAL),
            'a' : Variable('a', usintType, Variable.LOCAL),
            'b' : Variable('b', usintType, Variable.LOCAL)
        }
        programs = [
            ["IF is_IsAirInLine = 2 THEN b_s := 6; rtb_Config_Timer := 3; END_IF;",
             "IF (is_IsAirInLine = 2) THEN b_s := 6; rtb_Config_Timer := 3; END_IF;"],
            ["IF is_IsAirInLine = 2 THEN b_s := 6; ELSE rtb_Config_Timer := 3; END_IF;",
             "IF (is_IsAirInLine = 2) THEN b_s := 6; ELSIF TRUE THEN rtb_Config_Timer := 3; END_IF;"],
            ["IF a = 1 THEN b := 2; ELSIF a = 2 THEN b := 3; END_IF;",
             "IF (a = 1) THEN b := 2; ELSIF (a = 2) THEN b := 3; END_IF;"],
            ["IF a = 1 THEN b := 2; ELSIF a = 2 THEN b := 3; ELSIF a = 3 THEN b := 4; END_IF;",
             "IF (a = 1) THEN b := 2; ELSIF (a = 2) THEN b := 3; ELSIF (a = 3) THEN b := 4; END_IF;"],
            ["IF a = 1 THEN b := 2; ELSIF a = 2 THEN b := 3; ELSE b := 4; END_IF;",
             "IF (a = 1) THEN b := 2; ELSIF (a = 2) THEN b := 3; ELSIF TRUE THEN b := 4; END_IF;"]
        ]
        self._run_tests(programs, name2var)

    def test_st_case(self):
        name2var = {
            'is_Audio': Variable('is_Audio', usintType, Variable.LOCAL)
        }
        programs = [
            ["CASE is_Audio OF 1: is_Audio := 0; 2: is_Audio := 1; 3: is_Audio := 2; 4: is_Audio := 3; END_CASE;",
             "CASE is_Audio OF 1: is_Audio := 0; 2: is_Audio := 1; 3: is_Audio := 2; 4: is_Audio := 3; END_CASE;"],
            ["CASE is_Audio OF 1: is_Audio := 0; 2: is_Audio := 1; ELSE is_Audio := 2; END_CASE;",
             "CASE is_Audio OF 1: is_Audio := 0; 2: is_Audio := 1; is_Audio: is_Audio := 2; END_CASE;"]
        ]
        self._run_tests(programs, name2var)

    def test_st_conversions(self):
        name2var = {
            'varDint': Variable('varDint', dintType, Variable.LOCAL),
            'varUint': Variable('varUint', uintType, Variable.LOCAL),
            'varUsint': Variable('varUsint', usintType, Variable.LOCAL),
            'varUdint': Variable('varUdint', udintType, Variable.LOCAL),
        }
        programs = [
            ['varUint := DINT_TO_UINT(varDint);', 'varUint := DINT_TO_UINT(varDint);'],
            ['varDint := UINT_TO_DINT(varUint);', 'varDint := UINT_TO_DINT(varUint);'],
            ['varDint := USINT_TO_DINT(varUsint);', 'varDint := USINT_TO_DINT(varUsint);'],
            ['varUsint := UDINT_TO_USINT(varUdint);', 'varUsint := UDINT_TO_USINT(varUdint);'],
        ]
        self._run_tests(programs, name2var)

if __name__ == "__main__":
    unittest.main()

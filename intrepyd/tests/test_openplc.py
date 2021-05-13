import intrepyd
from intrepyd.iec611312py.plcopen import parse_plc_open_file
from intrepyd.iec611312py.stmtprinter import StmtPrinter
import unittest
from . import from_fixture_path

class TestOpenPLC(unittest.TestCase):
    def test_simple_1(self):
        pous = parse_plc_open_file(from_fixture_path('openplc/simple1.xml'))
        self.assertEqual(1, len(pous))
        printer = StmtPrinter()
        printer.processStatements(pous[0].statements)
        self.assertEqual('output1 := (local1 + input1);', printer.result)

    def test_datatype_1(self):
        pous = parse_plc_open_file(from_fixture_path('openplc/datatype1.xml'))
        self.assertEqual(1, len(pous))

    def test_if_1(self):
        pous = parse_plc_open_file(from_fixture_path('openplc/if1.xml'))
        self.assertEqual(1, len(pous))

    def test_if_2(self):
        pous = parse_plc_open_file(from_fixture_path('openplc/if2.xml'))
        self.assertEqual(1, len(pous))

    def test_if_3(self):
        pous = parse_plc_open_file(from_fixture_path('openplc/if3.xml'))
        self.assertEqual(1, len(pous))

    def test_if_4(self):
        pous = parse_plc_open_file(from_fixture_path('openplc/if4.xml'))
        self.assertEqual(1, len(pous))
        printer = StmtPrinter()
        printer.processStatements(pous[0].statements)
        self.assertEqual('IF (100 < (UDINT_TO_DINT((CONST_IN.Tolerance_Max / 100)) * UnitDelay_2_DSTATE)) THEN overInfusion := 1; END_IF;',
                         printer.result)

    # It is slow, as expected
    # def test_infusion_pump(self):
    #     pous = parsePlcOpenFile('tests/openplc/GPCA_SW_Functional_subst.xml')
    #     self.assertEqual(1, len(pous))

if __name__ == "__main__":
    unittest.main()

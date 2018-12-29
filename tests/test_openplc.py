"""
Copyright (C) 2018 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 04/11/2018
"""

import unittest
from intrepyd.iec611312py.plcopen import parsePlcOpenFile
from intrepyd.iec611312py.stmtprinter import StmtPrinter

class TestOpenPLC(unittest.TestCase):
    def test_simple_1(self):
        pous = parsePlcOpenFile('tests/openplc/simple1.xml')
        self.assertEquals(1, len(pous))
        printer = StmtPrinter()
        printer.processStatements(pous[0].statements)
        self.assertEqual('output1 := (local1 + input1);', printer.result)

    def test_datatype_1(self):
        pous = parsePlcOpenFile('tests/openplc/datatype1.xml')
        self.assertEquals(1, len(pous))

    def test_if_1(self):
        pous = parsePlcOpenFile('tests/openplc/if1.xml')
        self.assertEquals(1, len(pous))

    def test_if_2(self):
        pous = parsePlcOpenFile('tests/openplc/if2.xml')
        self.assertEquals(1, len(pous))

    def test_if_3(self):
        pous = parsePlcOpenFile('tests/openplc/if3.xml')
        self.assertEquals(1, len(pous))

    def test_if_4(self):
        pous = parsePlcOpenFile('tests/openplc/if4.xml')
        self.assertEquals(1, len(pous))
        printer = StmtPrinter()
        printer.processStatements(pous[0].statements)
        self.assertEqual('IF (100 < (UDINT_TO_DINT((CONST_IN.Tolerance_Max / 100)) * UnitDelay_2_DSTATE)) THEN overInfusion := 1; END_IF;',
                         printer.result)

    # It is slow, as expected
    # def test_infusion_pump(self):
    #     pous = parsePlcOpenFile('tests/openplc/GPCA_SW_Functional_subst.xml')
    #     self.assertEquals(1, len(pous))

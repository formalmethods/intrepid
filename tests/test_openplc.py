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

class TestOpenPLC(unittest.TestCase):
    def test_simple_1(self):
        pous = parsePlcOpenFile('tests/openplc/simple1.xml')
        self.assertEquals(1, len(pous))

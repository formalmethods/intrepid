"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017
"""
import unittest
import intrepyd
import intrepyd.engine

class TestEngine(unittest.TestCase):

    def test_engine_01(self):
        ctx = intrepyd.Context()
        bmc = ctx.mk_bmc()
        br = ctx.mk_backward_reach()
        bmcOpt = ctx.mk_optimizing_bmc()
        self.assertEqual(False, bmc.can_prove())
        self.assertEqual(False, bmc.can_optimize())
        self.assertEqual(True, br.can_prove())
        self.assertEqual(False, br.can_optimize())
        self.assertEqual(False, bmcOpt.can_prove())
        self.assertEqual(True, bmcOpt.can_optimize())

if __name__ == '__main__':
    unittest.main()

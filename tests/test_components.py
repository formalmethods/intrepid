"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017
"""
import unittest
import intrepyd as ip
import intrepyd.components

class TestComponents(unittest.TestCase):

    def test_counter_01(self):
        ctx = ip.Context()
        int8type = ctx.mk_int8_type()
        ten = ctx.mk_number("10", int8type)
        counter, Q = ip.components.mk_counter(ctx, "counter", type=int8type, limit=ten)
        simulator = ctx.mk_simulator()
        tr = ctx.mk_trace()
        simulator.add_watch(counter)
        simulator.add_watch(Q)
        simulator.simulate(tr, 12)
        self.assertEqual('9', tr.get_value(counter, 9))
        self.assertEqual('F', tr.get_value(Q, 9))
        self.assertEqual('10', tr.get_value(counter, 10))
        self.assertEqual('T', tr.get_value(Q, 10))
        self.assertEqual('10', tr.get_value(counter, 11))
        self.assertEqual('T', tr.get_value(Q, 11))

if __name__ == '__main__':
    unittest.main()

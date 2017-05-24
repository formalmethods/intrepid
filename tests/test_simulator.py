"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017
"""
import intrepyd as ip
import intrepyd.simulator
import intrepyd.trace
import unittest

class TestSimulator(unittest.TestCase):

    def test_simulator_01(self):
        ctx = ip.Context()
        bt = ctx.mk_boolean_type()
        x = ctx.mk_input('x', bt)
        y = ctx.mk_input('y', bt)
        x_and_y = ctx.mk_and(x, y)
        tr = ctx.mk_trace()
        tr.set_value(x, 0, 'true')
        tr.set_value(y, 0, 'true')
        sim = ctx.mk_simulator()
        sim.add_watch(x_and_y)
        sim.simulate(tr, 0)
        self.assertEqual(1, ip.trace.Trace.get_numeric_value(tr.get_value(x_and_y, 0)))

    def test_simulator_02(self):
        ctx = ip.Context()
        it = ctx.mk_int8_type()
        x = ctx.mk_input('x', it)
        counter = ctx.mk_latch('counter', it)
        init = ctx.mk_number('0', it) 
        next_ = ctx.mk_add(counter, x)
        ctx.set_latch_init_next(counter, init, next_)
        tr = ctx.mk_trace()
        tr.set_value(x, 0, '1')
        tr.set_value(x, 1, '3')
        sim = ctx.mk_simulator()
        sim.add_watch(counter)
        sim.simulate(tr, 2)
        self.assertEqual('0', tr.get_value(counter, 0))
        self.assertEqual('1', tr.get_value(counter, 1))
        self.assertEqual('4', tr.get_value(counter, 2))

if __name__ == '__main__':
    unittest.main()

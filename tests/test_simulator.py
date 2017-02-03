import intrepyd as ip
import intrepyd.simulator
import intrepyd.trace
import unittest

class TestSimulator(unittest.TestCase):

    def setUp(self):
        self.ctx = ip.Context()

    def test_simulator_01(self):
        ctx = self.ctx
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
        self.assertEqual('true', tr.get_value(x_and_y, 0))

if __name__ == '__main__':
    unittest.main()

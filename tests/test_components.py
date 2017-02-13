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
        self.assertEqual('false', tr.get_value(Q, 9))
        self.assertEqual('10', tr.get_value(counter, 10))
        self.assertEqual('true', tr.get_value(Q, 10))
        self.assertEqual('10', tr.get_value(counter, 11))
        self.assertEqual('true', tr.get_value(Q, 11))

if __name__ == '__main__':
    unittest.main()

import intrepyd
from intrepyd.engine import EngineResult
import intrepyd.pseudoboolean
import unittest

class TestExactlyOne(unittest.TestCase):

    def create_and_run_nets(self, n, context):
        nets = []
        bt = context.mk_boolean_type()
        for i in range(n):
            nets.append(context.mk_input("n" + str(i), bt))
        eo = intrepyd.pseudoboolean.mk_exactly_one(context, nets, "eo")
        bmc = context.mk_bmc()
        bmc.add_target(eo)
        result = bmc.reach_targets()
        self.assertEqual(EngineResult.REACHABLE, result)
        reachedNets = bmc.get_last_reached_targets()
        self.assertEqual(1, len(list(reachedNets)))

    def test_exactly_one_01(self):
        context = intrepyd.Context()
        self.create_and_run_nets(1, context)

    def test_exactly_one_02(self):
        context = intrepyd.Context()
        self.create_and_run_nets(2, context)

    def test_exactly_one_03(self):
        context = intrepyd.Context()
        self.create_and_run_nets(3, context)

    def test_exactly_one_04(self):
        context = intrepyd.Context()
        self.create_and_run_nets(4, context)

    def test_exactly_one_05(self):
        context = intrepyd.Context()
        self.create_and_run_nets(10, context)

    def test_exactly_one_06(self):
        context = intrepyd.Context()
        self.create_and_run_nets(11, context)

    def test_exactly_one_07(self):
        context = intrepyd.Context()
        self.create_and_run_nets(12, context)

    def test_exactly_one_08(self):
        context = intrepyd.Context()
        self.create_and_run_nets(43, context)

    def test_exactly_one_09(self):
        context = intrepyd.Context()
        nets = []
        bt = context.mk_boolean_type()
        i1 = context.mk_input("i1", bt)
        i2 = context.mk_input("i2", bt)
        i3 = context.mk_input("i3", bt)
        nets.append(context.mk_or(i1, i2))
        nets.append(context.mk_or(i1, i3))
        nets.append(context.mk_or(i2, i3))
        eo = intrepyd.pseudoboolean.mk_exactly_one(context, nets, "eo")
        bmc = context.mk_bmc()
        bmc.add_target(eo)
        result = bmc.reach_targets()
        self.assertEqual(EngineResult.UNKNOWN, result)

if __name__ == "__main__":
    unittest.main()

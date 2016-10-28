import unittest
import intrepid as Int

class Test_test_api(unittest.TestCase):

    def setUp(self):
        self.ctx = Int.mk_ctx()

    def tearDown(self):
        Int.del_ctx(self.ctx)

    def test_bmc(self):
        bt = Int.mk_boolean_type(self.ctx)
        x = Int.mk_input(self.ctx, "x", bt)
        y = Int.mk_input(self.ctx, "y", bt)
        gate = Int.mk_and(self.ctx, x, y)
        Int.mk_output(self.ctx, gate)
        bmc = Int.mk_engine_bmc(self.ctx, 10)
        Int.bmc_add_target(self.ctx, bmc, gate)
        Int.set_bmc_current_depth(bmc, 0)
        result = Int.bmc_reach_targets(bmc)
        self.assertEquals(Int.INT_ENGINE_RESULT_REACHABLE, result)


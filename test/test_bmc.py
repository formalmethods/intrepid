import unittest
import intrepid as ip
import intrepid.utils

class TestBmc(unittest.TestCase):

    def setUp(self):
        self.ctx = ip.mk_ctx()

    def tearDown(self):
        ip.del_ctx(self.ctx)

    def test_bmc_01(self):
        bt = ip.mk_boolean_type(self.ctx)
        x = ip.mk_input(self.ctx, "x", bt)
        y = ip.mk_input(self.ctx, "y", bt)
        gate = ip.mk_and(self.ctx, x, y)
        ip.mk_output(self.ctx, gate)
        bmc = ip.mk_engine_bmc(self.ctx)
        ip.bmc_add_target(self.ctx, bmc, gate)
        ip.set_bmc_current_depth(bmc, 0)
        result = ip.bmc_reach_targets(bmc)
        self.assertEquals(ip.INT_ENGINE_RESULT_REACHABLE, result)

    def test_bmc_02(self):
        bt = ip.mk_boolean_type(self.ctx)
        x = ip.mk_input(self.ctx, "x", bt)
        y = ip.mk_input(self.ctx, "y", bt)
        gate = ip.mk_and(self.ctx, x, y)
        ip.mk_output(self.ctx, gate)
        bmc = ip.mk_engine_bmc(self.ctx)
        ip.bmc_add_target(self.ctx, bmc, gate)
        ip.set_bmc_current_depth(bmc, 0)
        result = ip.bmc_reach_targets(bmc)
        self.assertEquals(ip.INT_ENGINE_RESULT_REACHABLE, result)
        cex = ip.bmc_get_counterexample(self.ctx, bmc, gate)
        value_x = ip.utils.counterexample_get_value_for_net(self.ctx, cex, x, 0)
        self.assertEquals('true', value_x)
        value_y = ip.utils.counterexample_get_value_for_net(self.ctx, cex, y, 0)
        self.assertEquals('true', value_y)

    def test_bmc_03(self):
        bt = ip.mk_boolean_type(self.ctx)
        x = ip.mk_input(self.ctx, "x", bt)
        y = ip.mk_input(self.ctx, "y", bt)
        gate = ip.mk_and(self.ctx, ip.mk_not(self.ctx, x), y)
        ip.mk_output(self.ctx, gate)
        ip.mk_assumption(self.ctx, x)
        bmc = ip.mk_engine_bmc(self.ctx)
        ip.bmc_add_target(self.ctx, bmc, gate)
        ip.set_bmc_current_depth(bmc, 0)
        result = ip.bmc_reach_targets(bmc)
        self.assertEquals(ip.INT_ENGINE_RESULT_UNREACHABLE, result)
    
if __name__ == '__main__':
    unittest.main()
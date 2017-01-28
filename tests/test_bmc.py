from .context import intrepyd as ip
from intrepyd.engine import EngineResult
import unittest

class TestBmc(unittest.TestCase):

    def test_bmc_01(self):
        context = ip.Context()
        bt = context.mk_boolean_type()
        x = context.mk_input("x", bt)
        y = context.mk_input("y", bt)
        gate = context.mk_and(x, y)
        context.mk_output(gate)
        bmc = context.mk_bmc()
        bmc.add_target(gate)
        bmc.set_current_depth(0)
        result = bmc.reach_targets()
        self.assertEquals(EngineResult.REACHABLE, result)

#     def test_bmc_02(self):
#         bt = ip.mk_boolean_type(self.ctx)
#         x = ip.mk_input(self.ctx, "x", bt)
#         y = ip.mk_input(self.ctx, "y", bt)
#         gate = ip.mk_and(self.ctx, x, y)
#         ip.mk_output(self.ctx, gate)
#         bmc = ip.mk_engine_bmc(self.ctx)
#         ip.bmc_add_target(self.ctx, bmc, gate)
#         ip.set_bmc_current_depth(bmc, 0)
#         result = ip.bmc_reach_targets(bmc)
#         self.assertEquals(ip.INT_ENGINE_RESULT_REACHABLE, result)
#         cex = ip.bmc_get_counterexample(self.ctx, bmc, gate)
#         value_x = ip.utils.counterexample_get_value_for_net(self.ctx, cex, x, 0)
#         self.assertEquals('true', value_x)
#         value_y = ip.utils.counterexample_get_value_for_net(self.ctx, cex, y, 0)
#         self.assertEquals('true', value_y)

#     def test_bmc_03(self):
#         bt = ip.mk_boolean_type(self.ctx)
#         x = ip.mk_input(self.ctx, "x", bt)
#         y = ip.mk_input(self.ctx, "y", bt)
#         gate = ip.mk_and(self.ctx, ip.mk_not(self.ctx, x), y)
#         ip.mk_output(self.ctx, gate)
#         ip.mk_assumption(self.ctx, x)
#         bmc = ip.mk_engine_bmc(self.ctx)
#         ip.bmc_add_target(self.ctx, bmc, gate)
#         ip.set_bmc_current_depth(bmc, 0)
#         result = ip.bmc_reach_targets(bmc)
#         self.assertEquals(ip.INT_ENGINE_RESULT_UNREACHABLE, result)

#     def test_bmc_04(self):
#         bt = ip.mk_boolean_type(self.ctx)
#         f = ip.mk_false(self.ctx)
#         t = ip.mk_true(self.ctx)
#         l1 = ip.mk_latch(self.ctx, 'l1', bt)
#         l2 = ip.mk_latch(self.ctx, 'l2', bt)
#         l3 = ip.mk_latch(self.ctx, 'l3', bt)
#         ip.set_latch_init_next(self.ctx, l1, t, l3)
#         ip.set_latch_init_next(self.ctx, l2, f, l1)
#         ip.set_latch_init_next(self.ctx, l3, f, l2)
#         bmc = ip.mk_engine_bmc(self.ctx)
#         ip.bmc_add_target(self.ctx, bmc, l3)
#         ip.bmc_add_watch(self.ctx, bmc, l1)
#         ip.bmc_add_watch(self.ctx, bmc, l2)
#         ip.bmc_add_watch(self.ctx, bmc, l3)
#         ip.set_bmc_current_depth(bmc, 0)
#         result = ip.bmc_reach_targets(bmc)
#         self.assertEquals(ip.INT_ENGINE_RESULT_UNREACHABLE, result)
#         ip.set_bmc_current_depth(bmc, 1)
#         result = ip.bmc_reach_targets(bmc)
#         self.assertEquals(ip.INT_ENGINE_RESULT_UNREACHABLE, result)
#         ip.set_bmc_current_depth(bmc, 2)
#         result = ip.bmc_reach_targets(bmc)
#         self.assertEquals(ip.INT_ENGINE_RESULT_REACHABLE, result)

    
if __name__ == '__main__':
    unittest.main()

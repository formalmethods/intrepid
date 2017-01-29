import intrepyd as ip
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

    def test_bmc_02(self):
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
        trace = bmc.get_last_trace()
        self.assertEquals(1, trace[x][0])
        self.assertEquals(1, trace[y][0])

    def test_bmc_03(self):
        context = ip.Context()
        bt = context.mk_boolean_type()
        x = context.mk_input("x", bt)
        y = context.mk_input("y", bt)
        gate = context.mk_and(context.mk_not(x), y)
        context.mk_output(gate)
        context.mk_assumption(x)
        bmc = context.mk_bmc()
        bmc.add_target(gate)
        bmc.set_current_depth(0)
        result = bmc.reach_targets()
        self.assertEquals(EngineResult.UNREACHABLE, result)

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

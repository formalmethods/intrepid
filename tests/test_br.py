import unittest
import intrepid as ip
import intrepid.utils

class TestBr(unittest.TestCase):

    def setUp(self):
        self.ctx = ip.mk_ctx()

    def tearDown(self):
        ip.del_ctx(self.ctx)

    def test_br_01(self):
        realtype = ip.mk_real_type(self.ctx)
        limit = ip.mk_number(self.ctx, "50", realtype)
        one = ip.mk_number(self.ctx, "1", realtype)
        counter1 = ip.mk_latch(self.ctx, "counter1", realtype)
        plusone = ip.mk_add(self.ctx, counter1, one)
        ip.set_latch_init_next(self.ctx, counter1, one, plusone)
        counter2 = ip.mk_latch(self.ctx, "counter2", realtype)
        plusone = ip.mk_add(self.ctx, counter2, one)
        ip.set_latch_init_next(self.ctx, counter2, one, plusone)
        mul = ip.mk_mul(self.ctx, counter1, counter2)
        ip.mk_output(self.ctx, mul)
        target = ip.mk_leq(self.ctx, limit, mul)
        br = ip.mk_engine_br(self.ctx)
        ip.br_add_target(self.ctx, br, target)
        ip.br_add_watch(self.ctx, br, counter1)
        ip.br_add_watch(self.ctx, br, counter2)
        result = ip.br_reach_targets(br)
        self.assertEquals(ip.INT_ENGINE_RESULT_REACHABLE, result)
        cex = ip.br_get_counterexample(self.ctx, br, target)
        cexDict = ip.utils.counterexample_get_as_dictionary(self.ctx, cex, {}, { 'counter1' : counter1, 'counter2' : counter2 })
        counter1lastValue = cexDict['counter1'][-1]
        counter2lastValue = cexDict['counter2'][-1]
        self.assertEquals(counter1lastValue, "8.0")
        self.assertEquals(counter2lastValue, "8.0")

if __name__ == '__main__':
    unittest.main()

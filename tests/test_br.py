import unittest
import intrepid as ip
import intrepid.utils

class TestBr(unittest.TestCase):

    def setUp(self):
        self.ctx = ip.mk_ctx()

    def tearDown(self):
        ip.del_ctx(self.ctx)

    @unittest.skip("Crashes for unknown reason")
    def test_br_01(self):
        realtype = ip.mk_real_type(self.ctx)
        limit = ip.mk_number(self.ctx, "50", realtype)
        counter = ip.mk_latch(self.ctx, "counter", realtype)
        one = ip.mk_number(self.ctx, "1", realtype)
        plusone = ip.mk_add(self.ctx, counter, one)
        ip.set_latch_init_next(self.ctx, counter, one, plusone)
        counter2 = ip.mk_mul(self.ctx, counter, counter)
        ip.mk_output(self.ctx, counter2)
        target = ip.mk_leq(self.ctx, limit, counter2)
        br = ip.mk_engine_br(self.ctx)
        ip.br_add_target(self.ctx, br, target)
        ip.br_add_watch(self.ctx, br, counter)
        ip.br_add_watch(self.ctx, br, counter2)
        result = ip.br_reach_targets(br)
        self.assertEquals(ip.INT_ENGINE_RESULT_REACHABLE, result)
        cex = ip.br_get_counterexample(self.ctx, br, target)
        cexDict = ip.utils.counterexample_get_as_dictionary(self.ctx, cex, {}, { 'counter' : counter, 'counter^2' : counter2 })
        counterlastValue = cexDict['counter'][-1]
        counter2lastValue = cexDict['counter^2'][-1]
        print cexDict
        self.assertEquals(counterlastValue, "8.0")
        self.assertEquals(counter2lastValue, "64.0")

if __name__ == '__main__':
    unittest.main()

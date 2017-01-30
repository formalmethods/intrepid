import intrepyd as ip
from intrepyd.engine import EngineResult
import unittest

@unittest.skip("Buggy br api")
class TestBr(unittest.TestCase):

    def test_br_01(self):
        context = ip.Context()
        realtype = context.mk_real_type()
        limit = context.mk_number("50", realtype)
        one = context.mk_number("1", realtype)
        counter1 = context.mk_latch("counter1", realtype)
        plusone = context.mk_add(counter1, one)
        context.set_latch_init_next(counter1, one, plusone)
        counter2 = context.mk_latch("counter2", realtype)
        plusone = context.mk_add(counter2, one)
        context.set_latch_init_next(counter2, one, plusone)
        mul = context.mk_mul(counter1, counter2)
        context.mk_output(mul)
        target = context.mk_leq(limit, mul)
        br = context.mk_backward_reach()
        br.add_target(target)
        br.add_watch(counter1)
        br.add_watch(counter2)
        result = br.reach_targets()
        self.assertEquals(EngineResult.REACHABLE, result)
        trace = br.get_last_trace()
        traceDict = trace.get_as_net_dictionary()
        counter1lastValue = traceDict[counter1][-1]
        counter2lastValue = traceDict[counter2][-1]
        self.assertEquals(counter1lastValue, "8.0")
        self.assertEquals(counter2lastValue, "8.0")

if __name__ == '__main__':
    unittest.main()

import intrepyd
import intrepyd.engine
import unittest

class TestEngine(unittest.TestCase):

    def test_engine_01(self):
        ctx = intrepyd.Context()
        bmc = ctx.mk_bmc()
        br = ctx.mk_backward_reach()
        bmcOpt = ctx.mk_optimizing_bmc()
        self.assertEqual(False, bmc.can_prove())
        self.assertEqual(False, bmc.can_optimize())
        self.assertEqual(True, br.can_prove())
        self.assertEqual(False, br.can_optimize())
        self.assertEqual(False, bmcOpt.can_prove())
        self.assertEqual(True, bmcOpt.can_optimize())

if __name__ == '__main__':
    unittest.main()

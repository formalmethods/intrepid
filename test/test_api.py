import unittest
import intrepid as Int

class Test_test_api(unittest.TestCase):

    def setUp(self):
        self.ctx = Int.mk_ctx()

    def tearDown(self):
        Int.del_ctx(self.ctx)

    def test_and(self):
        bt = Int.mk_boolean_type(self.ctx)
        x = Int.mk_input(self.ctx, "x", bt)
        y = Int.mk_input(self.ctx, "y", bt)
        gate = Int.mk_and(self.ctx, x, y)
        self.assertTrue(Int.is_and(self.ctx, gate))

    def test_or(self):
        bt = Int.mk_boolean_type(self.ctx)
        x = Int.mk_input(self.ctx, "x", bt)
        y = Int.mk_input(self.ctx, "y", bt)
        gate = Int.mk_or(self.ctx, x, y)
        self.assertTrue(Int.is_or(self.ctx, gate))

    def test_not(self):
        bt = Int.mk_boolean_type(self.ctx)
        x = Int.mk_input(self.ctx, "x", bt)
        gate = Int.mk_not(self.ctx, x)
        self.assertTrue(Int.is_not(self.ctx, gate))

    def test_xor(self):
        bt = Int.mk_boolean_type(self.ctx)
        x = Int.mk_input(self.ctx, "x", bt)
        y = Int.mk_input(self.ctx, "y", bt)
        gate = Int.mk_xor(self.ctx, x, y)
        # This is intended behavior, because of internal
        # simplifications (xor a b) is rewritten into
        # (iff (not a) b)
        self.assertTrue(Int.is_iff(self.ctx, gate))

    def test_iff(self):
        bt = Int.mk_boolean_type(self.ctx)
        x = Int.mk_input(self.ctx, "x", bt)
        y = Int.mk_input(self.ctx, "y", bt)
        gate = Int.mk_iff(self.ctx, x, y)
        self.assertTrue(Int.is_iff(self.ctx, gate))

    def test_eq(self):
        i8t = Int.mk_int8_type(self.ctx)
        x = Int.mk_input(self.ctx, "x", i8t)
        y = Int.mk_input(self.ctx, "y", i8t)
        gate = Int.mk_eq(self.ctx, x, y)
        self.assertTrue(Int.is_eq(self.ctx, gate))

    def test_leq(self):
        i8t = Int.mk_int8_type(self.ctx)
        x = Int.mk_input(self.ctx, "x", i8t)
        y = Int.mk_input(self.ctx, "y", i8t)
        gate = Int.mk_leq(self.ctx, x, y)
        self.assertTrue(Int.is_leq(self.ctx, gate))

    def test_lt(self):
        i8t = Int.mk_int8_type(self.ctx)
        x = Int.mk_input(self.ctx, "x", i8t)
        y = Int.mk_input(self.ctx, "y", i8t)
        gate = Int.mk_lt(self.ctx, x, y)
        self.assertTrue(Int.is_not(self.ctx, gate))

    def test_geq(self):
        i8t = Int.mk_int8_type(self.ctx)
        x = Int.mk_input(self.ctx, "x", i8t)
        y = Int.mk_input(self.ctx, "y", i8t)
        gate = Int.mk_geq(self.ctx, x, y)
        self.assertTrue(Int.is_leq(self.ctx, gate))

    def test_gt(self):
        i8t = Int.mk_int8_type(self.ctx)
        x = Int.mk_input(self.ctx, "x", i8t)
        y = Int.mk_input(self.ctx, "y", i8t)
        gate = Int.mk_gt(self.ctx, x, y)
        self.assertTrue(Int.is_not(self.ctx, gate))

    def test_input(self):
        bt = Int.mk_boolean_type(self.ctx)
        x = Int.mk_input(self.ctx, "x", bt)
        self.assertTrue(Int.is_input(self.ctx, x))

    def test_inputs_number(self):
        bt = Int.mk_boolean_type(self.ctx)
        x = Int.mk_input(self.ctx, "x", bt)
        y = Int.mk_input(self.ctx, "y", bt)
        self.assertEquals(2, Int.get_inputs_number(ctx))

    def test_output(self):
        bt = Int.mk_boolean_type(self.ctx)
        x = Int.mk_input(self.ctx, "x", bt)
        y = Int.mk_input(self.ctx, "y", bt)
        z = Int.mk_and(self.ctx, x, y)
        Int.mk_output(self.ctx, "z", z)
        self.assertTrue(Int.is_output(self.ctx, z))
        self.assertEquals(1, Int.get_outputs_number(ctx))

    def test_latch(self):
        bt = Int.mk_boolean_type(self.ctx)
        x = Int.mk_input(self.ctx, "x", bt)
        l = Int.mk_latch(self.ctx, "l", bt)
        t = Int.mk_true(self.ctx)
        Int.set_latch_init_next(self.ctx, l, t, x)
        self.assertTrue(Int.is_latch(self.ctx, l))

    def test_bmc(self):
        bt = Int.mk_boolean_type(self.ctx)
        x = Int.mk_input(self.ctx, "x", bt)
        y = Int.mk_input(self.ctx, "y", bt)
        gate = Int.mk_and(self.ctx, x, y)
        Int.mk_output(self.ctx, "out1", gate)
        bmc = Int.mk_engine_bmc(self.ctx, 10)
        Int.bmc_add_target(self.ctx, bmc, gate)
        Int.set_bmc_current_depth(bmc, 0)
        result = Int.bmc_reach_targets(bmc)
        self.assertEquals(Int.INT_ENGINE_RESULT_REACHABLE, result)


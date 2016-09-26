import unittest
import intrepid as Int

class Test_test_api(unittest.TestCase):

    def setUp(self):
        self.ctx = Int.mk_ctx()

    def tearDown(self):
        Int.del_ctx(self.ctx)

    def test_and(self):
        circuit = Int.mk_circuit(self.ctx, "tmp")
        bt = Int.mk_boolean_type(self.ctx)
        x = Int.mk_input(self.ctx, circuit, "x", bt)
        y = Int.mk_input(self.ctx, circuit, "y", bt)
        gate = Int.mk_and(self.ctx, x, y)
        self.assertTrue(Int.is_and(self.ctx, gate))

    def test_or(self):
        circuit = Int.mk_circuit(self.ctx, "tmp")
        bt = Int.mk_boolean_type(self.ctx)
        x = Int.mk_input(self.ctx, circuit, "x", bt)
        y = Int.mk_input(self.ctx, circuit, "y", bt)
        gate = Int.mk_or(self.ctx, x, y)
        self.assertTrue(Int.is_or(self.ctx, gate))

    def test_not(self):
        circuit = Int.mk_circuit(self.ctx, "tmp")
        bt = Int.mk_boolean_type(self.ctx)
        x = Int.mk_input(self.ctx, circuit, "x", bt)
        gate = Int.mk_not(self.ctx, x)
        self.assertTrue(Int.is_not(self.ctx, gate))

    def test_xor(self):
        circuit = Int.mk_circuit(self.ctx, "tmp")
        bt = Int.mk_boolean_type(self.ctx)
        x = Int.mk_input(self.ctx, circuit, "x", bt)
        y = Int.mk_input(self.ctx, circuit, "y", bt)
        gate = Int.mk_xor(self.ctx, x, y)
        # This is intended behavior, because of internal
        # simplifications (xor a b) is rewritten into
        # (iff (not a) b)
        self.assertTrue(Int.is_iff(self.ctx, gate))

    def test_iff(self):
        circuit = Int.mk_circuit(self.ctx, "tmp")
        bt = Int.mk_boolean_type(self.ctx)
        x = Int.mk_input(self.ctx, circuit, "x", bt)
        y = Int.mk_input(self.ctx, circuit, "y", bt)
        gate = Int.mk_iff(self.ctx, x, y)
        self.assertTrue(Int.is_iff(self.ctx, gate))

    def test_eq(self):
        circuit = Int.mk_circuit(self.ctx, "tmp")
        i8t = Int.mk_int8_type(self.ctx)
        x = Int.mk_input(self.ctx, circuit, "x", i8t)
        y = Int.mk_input(self.ctx, circuit, "y", i8t)
        gate = Int.mk_eq(self.ctx, x, y)
        self.assertTrue(Int.is_eq(self.ctx, gate))

    def test_leq(self):
        circuit = Int.mk_circuit(self.ctx, "tmp")
        i8t = Int.mk_int8_type(self.ctx)
        x = Int.mk_input(self.ctx, circuit, "x", i8t)
        y = Int.mk_input(self.ctx, circuit, "y", i8t)
        gate = Int.mk_leq(self.ctx, x, y)
        self.assertTrue(Int.is_leq(self.ctx, gate))

    def test_lt(self):
        circuit = Int.mk_circuit(self.ctx, "tmp")
        i8t = Int.mk_int8_type(self.ctx)
        x = Int.mk_input(self.ctx, circuit, "x", i8t)
        y = Int.mk_input(self.ctx, circuit, "y", i8t)
        gate = Int.mk_lt(self.ctx, x, y)
        self.assertTrue(Int.is_not(self.ctx, gate))

    def test_geq(self):
        circuit = Int.mk_circuit(self.ctx, "tmp")
        i8t = Int.mk_int8_type(self.ctx)
        x = Int.mk_input(self.ctx, circuit, "x", i8t)
        y = Int.mk_input(self.ctx, circuit, "y", i8t)
        gate = Int.mk_geq(self.ctx, x, y)
        self.assertTrue(Int.is_leq(self.ctx, gate))

    def test_gt(self):
        circuit = Int.mk_circuit(self.ctx, "tmp")
        i8t = Int.mk_int8_type(self.ctx)
        x = Int.mk_input(self.ctx, circuit, "x", i8t)
        y = Int.mk_input(self.ctx, circuit, "y", i8t)
        gate = Int.mk_gt(self.ctx, x, y)
        self.assertTrue(Int.is_not(self.ctx, gate))

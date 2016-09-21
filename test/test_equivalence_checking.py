import sys
# sys.path.append('intrepid')
import intrepid as Int
import unittest

class TestEquivalenceChecking(unittest.TestCase):

    def setUp(self):
        self.ctx = Int.mk_ctx()

    def tearDown(self):
        Int.del_ctx(self.ctx)

    def createAndCircuit(self, ctx, name):
        circ = Int.mk_circuit(ctx, name)
        tb = Int.mk_boolean_type(ctx)
        i1 = Int.mk_input(ctx, circ, "In1", tb)
        i2 = Int.mk_input(ctx, circ, "In2", tb)
        out = Int.mk_and(ctx, i1, i2)
        Int.mk_output(ctx, circ, "Out1", out)
        return circ

    def createOrCircuit(self, ctx, name):
        circ = Int.mk_circuit(ctx, name)
        tb = Int.mk_boolean_type(ctx)
        i1 = Int.mk_input(ctx, circ, "In1", tb)
        i2 = Int.mk_input(ctx, circ, "In2", tb)
        out = Int.mk_or(ctx, i1, i2)
        Int.mk_output(ctx, circ, "Out1", out)
        return circ

    def eqCheck(self, circ1, circ2):
        miter = Int.mk_circuit_miter(self.ctx, circ1, circ2)
        br = Int.mk_engine_br(self.ctx, miter)
        for output in Int.get_outputs(miter):
            Int.br_add_target(self.ctx, br, output)
        res = Int.br_reach_targets(br)
        return res

    def test_and(self):
        circ1 = self.createAndCircuit(self.ctx, "Circ1")
        circ2 = self.createAndCircuit(self.ctx, "Circ2")
        res = self.eqCheck(circ1, circ2)
        self.assertEqual(Int.INT_ENGINE_RESULT_UNREACHABLE, res)

    def test_or(self):
        circ1 = self.createOrCircuit(self.ctx, "Circ1")
        circ2 = self.createOrCircuit(self.ctx, "Circ2")
        res = self.eqCheck(circ1, circ2)
        self.assertEqual(Int.INT_ENGINE_RESULT_UNREACHABLE, res)

    def test_andor(self):
        circ1 = self.createAndCircuit(self.ctx, "Circ1")
        circ2 = self.createOrCircuit(self.ctx, "Circ2")
        res = self.eqCheck(circ1, circ2)
        self.assertEqual(Int.INT_ENGINE_RESULT_REACHABLE, res)

    def test_eq_1(self):
        circ1 = Int.mk_circuit_from_st_file(self.ctx, "test/files/fnc_1.st")
        circ2 = Int.mk_circuit_from_st_file(self.ctx, "test/files/fnc_2.st")
        res = self.eqCheck(circ1, circ2)
        self.assertEqual(Int.INT_ENGINE_RESULT_UNREACHABLE, res)

    def test_eq_2(self):
        circ1 = Int.mk_circuit_from_st_file(self.ctx, "test/files/fnc_3.st")
        circ2 = Int.mk_circuit_from_st_file(self.ctx, "test/files/fnc_4.st")
        res = self.eqCheck(circ1, circ2)
        self.assertEqual(Int.INT_ENGINE_RESULT_REACHABLE, res)

    def test_eq_3(self):
        circ1 = Int.mk_circuit_from_st_file(self.ctx, "test/files/fnc_5.st")
        circ2 = Int.mk_circuit_from_st_file(self.ctx, "test/files/fnc_6.st")
        res = self.eqCheck(circ1, circ2)
        self.assertEqual(Int.INT_ENGINE_RESULT_UNREACHABLE, res)

    def test_eq_4(self):
        circ1 = Int.mk_circuit_from_st_file(self.ctx, "test/files/fnc_7.st")
        circ2 = Int.mk_circuit_from_st_file(self.ctx, "test/files/fnc_8.st")
        res = self.eqCheck(circ1, circ2)
        self.assertEqual(Int.INT_ENGINE_RESULT_REACHABLE, res)

    def test_eq_5(self):
        circ1 = Int.mk_circuit_from_st_file(self.ctx, "test/files/fnc_9.st")
        circ2 = Int.mk_circuit_from_st_file(self.ctx, "test/files/fnc_10.st")
        res = self.eqCheck(circ1, circ2)
        self.assertEqual(Int.INT_ENGINE_RESULT_UNREACHABLE, res)

if __name__ == "__main__":
    unittest.main()

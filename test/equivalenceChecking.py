import sys
sys.path.append('.')
sys.path.append('win64')
import intrepid as Int
import utils as Utils
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

    def test_and(self):
        circ1 = self.createAndCircuit(self.ctx, "Circ1")
        circ2 = self.createAndCircuit(self.ctx, "Circ2")
        miter = Int.mk_circuit_miter(self.ctx, circ1, circ2)
        br = Int.mk_engine_br(self.ctx, miter)
        for output in Utils.getOutputs(miter):
            Int.br_add_target(self.ctx, br, output)
        res = Int.br_reach_targets(br)
        self.assertEqual(Int.INT_ENGINE_RESULT_UNREACHABLE, res)

    def test_or(self):
        circ1 = self.createOrCircuit(self.ctx, "Circ1")
        circ2 = self.createOrCircuit(self.ctx, "Circ2")
        miter = Int.mk_circuit_miter(self.ctx, circ1, circ2)
        br = Int.mk_engine_br(self.ctx, miter)
        for output in Utils.getOutputs(miter):
            Int.br_add_target(self.ctx, br, output)
        res = Int.br_reach_targets(br)
        self.assertEqual(Int.INT_ENGINE_RESULT_UNREACHABLE, res)

    def test_andor(self):
        circ1 = self.createAndCircuit(self.ctx, "Circ1")
        circ2 = self.createOrCircuit(self.ctx, "Circ2")
        miter = Int.mk_circuit_miter(self.ctx, circ1, circ2)
        br = Int.mk_engine_br(self.ctx, miter)
        for output in Utils.getOutputs(miter):
            Int.br_add_target(self.ctx, br, output)
        res = Int.br_reach_targets(br)
        self.assertEqual(Int.INT_ENGINE_RESULT_REACHABLE, res)

if __name__ == "__main__":
    unittest.main()

"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017
"""
import unittest
import intrepyd
import intrepyd.circuit
from intrepyd.engine import EngineResult

class MyCirc(intrepyd.circuit.Circuit):
    
    def __init__(self, context, name):
        intrepyd.circuit.Circuit.__init__(self, context, name)
   
    def _mk_naked_circuit_impl(self, inputs):
        inputKeys = list(inputs)
        i1 = inputs[inputKeys[0]]
        i2 = inputs[inputKeys[1]]
        output = self.context.mk_and(i1, i2)
        return output
        

class TestCircuit(unittest.TestCase):

    def test_circuit_01(self):
        ctx = intrepyd.Context()
        inst1 = MyCirc(ctx, 'mycirc1')
        inst2 = MyCirc(ctx, 'mycirc2')
        bt = ctx.mk_boolean_type()
        i1 = ctx.mk_input('i1', bt)
        i2 = ctx.mk_input('i2', bt)
        inputs = { 'i1' : i1, 'i2' : i2 }
        out1 = inst1.mk_naked_circuit(inputs, True) 
        out2 = inst2.mk_naked_circuit(inputs, True) 
        diff = ctx.mk_xor(out1, out2)
        bmc = ctx.mk_bmc()
        bmc.add_target(diff)
        result = bmc.reach_targets()   
        self.assertEqual(EngineResult.UNREACHABLE, result)

if __name__ == '__main__':
    unittest.main()

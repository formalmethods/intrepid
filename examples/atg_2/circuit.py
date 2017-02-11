import intrepyd as ip
import intrepyd.scr
import intrepyd.circuit
import collections

class SimulinkCircuit(ip.circuit.Circuit):
    def __init__(self, ctx, name):
        ip.circuit.Circuit.__init__(self, ctx, name)

    def _mk_naked_circuit_impl(self, inputs):
        input_keys = list(inputs)
        # In1 -> n1
        n1 = inputs[input_keys[0]]
        # In2 -> n2
        n2 = inputs[input_keys[1]]
        # In3 -> n3
        n3 = inputs[input_keys[2]]
        # In4 -> n4
        n4 = inputs[input_keys[3]]
        # In5 -> n5
        n5 = inputs[input_keys[4]]
        # In6 -> n6
        n6 = inputs[input_keys[5]]
        # circuit/gate3 -> n7
        n7 = self.context.mk_or(n1, n2)
        self.nets['circuit/gate3'] = n7
        # circuit/gate2 -> n8
        n8 = self.context.mk_or(n3, n4)
        self.nets['circuit/gate2'] = n8
        # circuit/gate4 -> n9
        n9 = self.context.mk_and(n7, n8)
        self.nets['circuit/gate4'] = n9
        # circuit/gate1 -> n10
        n10 = self.context.mk_and(n5, n6)
        self.nets['circuit/gate1'] = n10
        # circuit/gate5 -> n11
        n11 = self.context.mk_xor(n9, n10)
        self.nets['circuit/gate5'] = n11
        # n11 -> Out
        outputs = collections.OrderedDict()
        outputs['circuit/Out'] = n11
        self.nets['circuit/Out'] = n11
        return outputs

    def _mk_inputs(self):
        # circuit/In1 -> n1
        n1 = self.context.mk_input('In1', self.context.mk_boolean_type())
        self.inputs['In1'] = n1
        # circuit/In2 -> n2
        n2 = self.context.mk_input('In2', self.context.mk_boolean_type())
        self.inputs['In2'] = n2
        # circuit/In3 -> n3
        n3 = self.context.mk_input('In3', self.context.mk_boolean_type())
        self.inputs['In3'] = n3
        # circuit/In4 -> n4
        n4 = self.context.mk_input('In4', self.context.mk_boolean_type())
        self.inputs['In4'] = n4
        # circuit/In5 -> n5
        n5 = self.context.mk_input('In5', self.context.mk_boolean_type())
        self.inputs['In5'] = n5
        # circuit/In6 -> n6
        n6 = self.context.mk_input('In6', self.context.mk_boolean_type())
        self.inputs['In6'] = n6


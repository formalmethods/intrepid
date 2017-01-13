import intrepid as ip
import intrepid.scr
import intrepid.circuit
import collections

class SimulinkCircuit(ip.circuit.Circuit):
    def __init__(self, ctx, name):
        ip.circuit.Circuit.__init__(self, ctx, name)

    def _mk_naked_circuit_impl(self, inputs):
        input_keys = list(inputs)
        # OnOff -> n1
        n1 = inputs[input_keys[0]]
        # OnGreen -> n2
        n2 = inputs[input_keys[1]]
        # OnYellow -> n3
        n3 = inputs[input_keys[2]]
        # OnRed -> n4
        n4 = inputs[input_keys[3]]
        # Daytime -> n5
        n5 = inputs[input_keys[4]]
        n6 = ip.mk_latch(self.ctx, 'traffic_light/Past(OnOff)', ip.mk_boolean_type(self.ctx))
        n7 = ip.mk_latch(self.ctx, 'traffic_light/Past(OnRed)', ip.mk_boolean_type(self.ctx))
        n8 = ip.mk_latch(self.ctx, 'traffic_light/Past(OnYellow)', ip.mk_boolean_type(self.ctx))
        n9 = ip.mk_latch(self.ctx, 'traffic_light/Past(OnGreen)', ip.mk_boolean_type(self.ctx))
        n10 = ip.mk_latch(self.ctx, 'traffic_light/Past(Daytime)', ip.mk_boolean_type(self.ctx))
        n11 = ip.mk_latch(self.ctx, 'traffic_light/Init', ip.mk_boolean_type(self.ctx))
        n12 = ip.mk_latch(self.ctx, 'traffic_light/Past(Mode)', ip.mk_int8_type(self.ctx))
        # traffic_light/false
        n13 = ip.mk_false(self.ctx)
        self.nets['traffic_light/false'] = n13
        # traffic_light/Off
        n14 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['traffic_light/Off'] = n14
        # Bus Creator
        n15 = [n1, n2, n3, n4, n5]
        # Bus Creator1
        n16 = [n6, n9, n8, n7, n10]
        # traffic_light/Green
        n17 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        self.nets['traffic_light/Green'] = n17
        # traffic_light/Yellow
        n18 = ip.mk_number(self.ctx, '2', ip.mk_int8_type(self.ctx))
        self.nets['traffic_light/Yellow'] = n18
        # traffic_light/Red
        n19 = ip.mk_number(self.ctx, '3', ip.mk_int8_type(self.ctx))
        self.nets['traffic_light/Red'] = n19
        # Bus Creator2
        n20 = [n14, n17, n18, n19]
        # traffic_light/Mode1
        n21 = ip.mk_ite(self.ctx, n11, n14, n12)
        self.nets['traffic_light/Mode1'] = n21
        n22_1 = ip.scr.mk_scr(self.ctx, 'traffic_light', n15, n16, n20, n21)
        # traffic_light/Mode
        n23 = ip.mk_ite(self.ctx, n11, n14, n22_1)
        self.nets['traffic_light/Mode'] = n23
        in6 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n6, in6, n1)
        in7 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n7, in7, n4)
        in8 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n8, in8, n3)
        in9 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n9, in9, n2)
        in10 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n10, in10, n5)
        in11 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n11, in11, n13)
        in12 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        ip.set_latch_init_next(self.ctx, n12, in12, n23)
        # n23 -> out
        outputs = collections.OrderedDict()
        outputs['traffic_light/out'] = n23
        return outputs

    def _mk_inputs(self):
        # traffic_light/OnOff -> n1
        n1 = ip.mk_input(self.ctx, 'OnOff', ip.mk_boolean_type(self.ctx))
        self.inputs['OnOff'] = n1
        # traffic_light/OnGreen -> n2
        n2 = ip.mk_input(self.ctx, 'OnGreen', ip.mk_boolean_type(self.ctx))
        self.inputs['OnGreen'] = n2
        # traffic_light/OnYellow -> n3
        n3 = ip.mk_input(self.ctx, 'OnYellow', ip.mk_boolean_type(self.ctx))
        self.inputs['OnYellow'] = n3
        # traffic_light/OnRed -> n4
        n4 = ip.mk_input(self.ctx, 'OnRed', ip.mk_boolean_type(self.ctx))
        self.inputs['OnRed'] = n4
        # traffic_light/Daytime -> n5
        n5 = ip.mk_input(self.ctx, 'Daytime', ip.mk_boolean_type(self.ctx))
        self.inputs['Daytime'] = n5


"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017
"""
import intrepyd as ip
import intrepyd.scr
import intrepyd.circuit
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
        n6 = self.context.mk_latch('traffic_light/Past(OnOff)', self.context.mk_boolean_type())
        n7 = self.context.mk_latch('traffic_light/Past(OnRed)', self.context.mk_boolean_type())
        n8 = self.context.mk_latch('traffic_light/Past(OnYellow)', self.context.mk_boolean_type())
        n9 = self.context.mk_latch('traffic_light/Past(OnGreen)', self.context.mk_boolean_type())
        n10 = self.context.mk_latch('traffic_light/Past(Daytime)', self.context.mk_boolean_type())
        n11 = self.context.mk_latch('traffic_light/Init', self.context.mk_boolean_type())
        n12 = self.context.mk_latch('traffic_light/Past(Mode)', self.context.mk_int8_type())
        # traffic_light/false
        n13 = self.context.mk_false()
        self.nets['traffic_light/false'] = n13
        # traffic_light/Off
        n14 = self.context.mk_number('0', self.context.mk_int8_type())
        self.nets['traffic_light/Off'] = n14
        # Bus Creator
        n15 = [n1, n2, n3, n4, n5]
        # Bus Creator1
        n16 = [n6, n9, n8, n7, n10]
        # traffic_light/Green
        n17 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['traffic_light/Green'] = n17
        # traffic_light/Yellow
        n18 = self.context.mk_number('2', self.context.mk_int8_type())
        self.nets['traffic_light/Yellow'] = n18
        # traffic_light/Red
        n19 = self.context.mk_number('3', self.context.mk_int8_type())
        self.nets['traffic_light/Red'] = n19
        # Bus Creator2
        n20 = [n14, n17, n18, n19]
        # traffic_light/Mode1
        n21 = self.context.mk_ite(n11, n14, n12)
        self.nets['traffic_light/Mode1'] = n21
        n22_1 = ip.scr.mk_scr(self.context, 'tests/traffic_light', n15, n16, n20, n21)
        # traffic_light/Mode
        n23 = self.context.mk_ite(n11, n14, n22_1)
        self.nets['traffic_light/Mode'] = n23
        in6 = self.context.mk_true()
        self.context.set_latch_init_next(n6, in6, n1)
        in7 = self.context.mk_true()
        self.context.set_latch_init_next(n7, in7, n4)
        in8 = self.context.mk_true()
        self.context.set_latch_init_next(n8, in8, n3)
        in9 = self.context.mk_true()
        self.context.set_latch_init_next(n9, in9, n2)
        in10 = self.context.mk_true()
        self.context.set_latch_init_next(n10, in10, n5)
        in11 = self.context.mk_true()
        self.context.set_latch_init_next(n11, in11, n13)
        in12 = self.context.mk_number('1', self.context.mk_int8_type())
        self.context.set_latch_init_next(n12, in12, n23)
        # n23 -> out
        outputs = collections.OrderedDict()
        outputs['traffic_light/out'] = n23
        self.nets['traffic_light/out'] = n23
        return outputs

    def _mk_inputs(self):
        # traffic_light/OnOff -> n1
        n1 = self.context.mk_input('OnOff', self.context.mk_boolean_type())
        self.inputs['OnOff'] = n1
        # traffic_light/OnGreen -> n2
        n2 = self.context.mk_input('OnGreen', self.context.mk_boolean_type())
        self.inputs['OnGreen'] = n2
        # traffic_light/OnYellow -> n3
        n3 = self.context.mk_input('OnYellow', self.context.mk_boolean_type())
        self.inputs['OnYellow'] = n3
        # traffic_light/OnRed -> n4
        n4 = self.context.mk_input('OnRed', self.context.mk_boolean_type())
        self.inputs['OnRed'] = n4
        # traffic_light/Daytime -> n5
        n5 = self.context.mk_input('Daytime', self.context.mk_boolean_type())
        self.inputs['Daytime'] = n5


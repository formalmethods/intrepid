"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017
"""

import unittest
import collections
import intrepyd as ip
import intrepyd.atg.mcdc as mcdc
import intrepyd.circuit as circuit

class CircAnd(circuit.Circuit):
    def __init__(self, ctx, name):
        ip.circuit.Circuit.__init__(self, ctx, name)

    def _mk_inputs(self):
        self.inputs['A'] = self.context.mk_input('A', self.context.mk_boolean_type())
        self.inputs['B'] = self.context.mk_input('B', self.context.mk_boolean_type())

    def _mk_naked_circuit_impl(self, inputs):
        n1 = self.inputs['A']
        n2 = self.inputs['B']
        outputs = collections.OrderedDict()
        out = self.context.mk_and(n1, n2)
        outputs['O'] = out
        self.nets['A'] = n1
        self.nets['B'] = n2
        self.nets['O'] = out
        return outputs

class TestAtg(unittest.TestCase):

    def test_atg_01(self):
        ctx = ip.Context()
        decisions = { 'O' : ['A', 'B'] }
        tables, indpairs, decision2unreachable = mcdc.compute_mcdc(ctx, CircAnd, decisions, max_depth=10)
        decision2dataframe = ip.atg.mcdc.get_tables_as_dataframe(tables)
        self.assertEqual(3, len(decision2dataframe['O']))
        self.assertEqual(2, len(indpairs['O']))
        self.assertEqual(0, len(decision2unreachable['O']))
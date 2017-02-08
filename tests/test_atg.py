import unittest
import intrepyd as ip
import intrepyd.atg
import intrepyd.circuit
import collections
import pandas as pd

class CircAnd(ip.circuit.Circuit):
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
        tables = ip.atg.compute_mcdc(ctx, CircAnd, decisions, maxDepth=10)
        decision2dataframe = ip.atg.get_tables_as_dataframe(tables)
        self.assertEqual(3, len(decision2dataframe['O']))
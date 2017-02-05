import intrepyd as ip
import intrepyd.atg
import intrepyd.circuit
import collections
import pandas as pd

class CircAnd(ip.circuit.Circuit):
    def __init__(self, ctx, name):
        ip.circuit.Circuit.__init__(self, ctx, name)

    def _mk_inputs(self):
        self.inputs['A'] = ctx.mk_input('A', ctx.mk_boolean_type())
        self.inputs['B'] = ctx.mk_input('B', ctx.mk_boolean_type())

    def _mk_naked_circuit_impl(self, inputs):
        n1 = self.inputs['A']
        n2 = self.inputs['B']
        outputs = collections.OrderedDict()
        out = ctx.mk_and(n1, n2)
        outputs['O'] = out
        self.nets['A'] = n1
        self.nets['B'] = n2
        self.nets['O'] = out
        return outputs

if __name__ == "__main__":
    ctx = ip.Context()
    decisions = { 'O' : ['A', 'B'] }
    tables = ip.atg.compute_mcdc(ctx, CircAnd, decisions, maxDepth=10)
    decision2dataframe = ip.atg.get_tables_as_dataframe(tables)
    if len(decision2dataframe) != 0:
        print '\nGenerated tests:'
        print decision2dataframe['O']
import intrepid as ip
import intrepid.atg
import intrepid.circuit
import intrepid.utils
import collections
import pprint
import pandas as pd

class CircAnd(ip.circuit.Circuit):
    def __init__(self, ctx, name):
        ip.circuit.Circuit.__init__(self, ctx, name)

    def _mk_inputs(self):
        self.inputs['A'] = ip.mk_input(self.ctx, 'A', ip.mk_boolean_type(self.ctx))
        self.inputs['B'] = ip.mk_input(self.ctx, 'B', ip.mk_boolean_type(self.ctx))

    def _mk_naked_circuit_impl(self, inputs):
        n1 = self.inputs['A']
        n2 = self.inputs['B']
        outputs = collections.OrderedDict()
        out = ip.mk_and(self.ctx, n1, n2)
        outputs['O'] = out
        self.nets['A'] = n1
        self.nets['B'] = n2
        self.nets['O'] = out
        return outputs

if __name__ == "__main__":
    ctx = ip.mk_ctx()
    decisions = { 'O' : ['A', 'B'] }
    tables = ip.atg.compute_mcdc(ctx, CircAnd, decisions, maxDepth=10)
    decision2dataframe = ip.atg.get_tables_as_dataframe(tables)
    print '\nGenerated tests:'
    print decision2dataframe['O']
    ip.del_ctx(ctx)
import intrepyd
from intrepyd.atg import mcdc, circuit
import unittest

class TestAtg(unittest.TestCase):
    def test_atg_01(self):
        ctx = intrepyd.Context()
        decisions = { 'O' : ['A', 'B'] }
        tables, indpairs, decision2unreachable = mcdc.compute_mcdc(ctx, CircAnd, decisions, max_depth=10)
        decision2dataframe = mcdc.get_tables_as_dataframe(tables)
        self.assertEqual(3, len(decision2dataframe['O']))
        self.assertEqual(2, len(indpairs['O']))
        self.assertEqual(0, len(decision2unreachable['O']))

    def test_atg_02(self):
        ctx = intrepyd.Context()
        decisions = { 'Out' : ['In1', 'In2', 'In3', 'In4', 'In5', 'In6'] }
        tables, indpairs, decision2unreachable = mcdc.compute_mcdc(ctx, CircFmics2021, decisions, max_depth=10)
        decision2dataframe = intrepyd.atg.mcdc.get_tables_as_dataframe(tables)
        self.assertEqual(8, len(decision2dataframe['Out']))
        self.assertEqual(6, len(indpairs['Out']))
        self.assertEqual(0, len(decision2unreachable['Out']))
        # tables, _, _ = mcdc.compute_mcdc(ctx, CircFmics2021, decisions, max_depth=10)
        # decision2dataframe = mcdc.get_tables_as_dataframe(tables)
        # if len(decision2dataframe) != 0:
        #     print('\nGenerated tests:')
        #     print(decision2dataframe['Out'])

class CircAnd(circuit.Circuit):
    def __init__(self, ctx, name):
        super().__init__(ctx, name)
        self._nets = {}
        self._inputs = {}

    def _mk_circuit_impl(self):
        bt = self._ctx.mk_boolean_type()
        self._nets['A'] = self._ctx.mk_input('A', bt)
        self._nets['B'] = self._ctx.mk_input('B', bt)
        self._inputs['A'] = self._nets['A']
        self._inputs['B'] = self._nets['B']
        out = self._ctx.mk_and(self._nets['A'], self._nets['B'])
        self._nets['O'] = out

    def inputs(self):
        return self._inputs

    def nets(self):
        return self._nets

class CircFmics2021(circuit.Circuit):
    def __init__(self, ctx, name):
        super().__init__(ctx, name)

    def _mk_circuit_impl(self):
        bt = self._ctx.mk_boolean_type()
        self._nets = {}
        self._inputs = {}
        for i in range(1, 7):
            name = 'In{}'.format(i)
            self._inputs[name] = self._ctx.mk_input(name, bt)
            self._nets[name] = self._inputs[name]
        self._nets['gate1'] = self._ctx.mk_or(self._nets['In1'], self._nets['In2'])
        self._nets['gate2'] = self._ctx.mk_or(self._nets['In3'], self._nets['In4'])
        self._nets['gate3'] = self._ctx.mk_and(self._nets['In5'], self._nets['In6'])
        self._nets['gate4'] = self._ctx.mk_and(self._nets['gate1'], self._nets['gate2'])
        self._nets['gate5'] = self._ctx.mk_or(self._nets['gate3'], self._nets['gate4'])
        self._nets['Out'] = self._nets['gate5']

    def inputs(self):
        return self._inputs

    def nets(self):
        return self._nets

if __name__ == '__main__':
    unittest.main()

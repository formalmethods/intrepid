"""
Tests that the formula encoder works correctly
"""

import unittest
from intrepyd.engine import EngineResult
from intrepyd.formula2py.encoder import parse_string, compute_pre_depth, encode_formula
from intrepyd.context import Context
# from intrepyd.api import apitrace_dump_to_file

def _cp(formula):
    return compute_pre_depth(parse_string(formula))

class TestFormulaEncoder(unittest.TestCase):
    """
    Tests for the formula encoder
    """

    def _compute_trace(self, formula, expected_depth):
        ctx = Context()
        a = ctx.mk_input('a', ctx.mk_boolean_type())
        b = ctx.mk_latch('b', ctx.mk_boolean_type())
        ctx.set_latch_init_next(b, ctx.mk_true(), a)
        target = encode_formula(ctx, formula)
        # apitrace_dump_to_file('debug.cpp')
        br = ctx.mk_backward_reach()
        br.add_target(target)
        br.add_watch(b)
        res = br.reach_targets()
        self.assertEqual(EngineResult.REACHABLE, res)
        trace = br.get_last_trace()
        self.assertEqual(expected_depth, trace.get_max_depth())

    def test_it_computes_pre_depth(self):
        """
        Compute pre depth correctly
        """
        self.assertEqual(0, _cp('a and b'))
        self.assertEqual(0, _cp('a or b'))
        self.assertEqual(0, _cp('not a'))
        self.assertEqual(1, _cp('pre a'))
        self.assertEqual(0, _cp('a'))
        self.assertEqual(1, _cp('a and (pre b or not c)'))
        self.assertEqual(2, _cp('pre pre b'))
        self.assertEqual(3, _cp('pre (not (pre (not (pre a))))'))
        self.assertEqual(3, _cp('(pre b) and (pre (not (pre (not (pre a)))))'))

    def test_it_encodes_formula(self):
        """
        Encodes a formula correctly
        """
        self._compute_trace('a and b', 0)
        self._compute_trace('a or b', 0)
        self._compute_trace('(pre a) and b', 1)
        self._compute_trace('(pre (pre a)) and b', 2)
        self._compute_trace('(pre (pre a)) and (pre b)', 2)
        self._compute_trace('(pre (a and b)) or (pre (not b))', 1)
        self._compute_trace('(pre (pre (a and b)) or (pre (not b)))', 2)
        self._compute_trace('(pre b) and (pre (not (pre (not (pre a)))))', 3)

if __name__ == '__main__':
    unittest.main()

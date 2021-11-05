"""
Parses a formula
"""

from antlr4 import InputStream, CommonTokenStream
from intrepyd.formula2py.FormulaLexer import FormulaLexer
from intrepyd.formula2py.FormulaParser import FormulaParser
from intrepyd.formula2py.formulabuilder import FormulaBuilder


def parse_string(input_string):
    """
    Parse the provided string and create it in the provided
    intrepyd context. Returns the produced net or aborts with
    an error
    """
    lexer = FormulaLexer(InputStream(input_string))
    stream = CommonTokenStream(lexer)
    parser = FormulaParser(stream)
    tree = parser.formula()
    builder = FormulaBuilder()
    builder.visit(tree)
    return builder.formula


def compute_pre_depth(formula):
    """
    Computes the depth of nesting of pres in the formula
    """
    if isinstance(formula, str):
        return 0
    for operator in formula:
        args = formula[operator]
        if operator in ('AND', 'OR'):
            depth_args = 0
            for arg in args:
                depth_arg = compute_pre_depth(arg)
                depth_args = max(depth_args, depth_arg)
            return depth_args
        if operator == 'NOT':
            return compute_pre_depth(args)
        if operator == 'PRE':
            return 1 + compute_pre_depth(args)
    raise RuntimeError('Unhandled formula')


def _make_trigger_encoding(ctx, depth):
    result = ctx.mk_true()
    for d in range(depth):
        latch = ctx.mk_latch(f'__t_{d}', ctx.mk_boolean_type())
        ctx.set_latch_init_next(latch, ctx.mk_false(), result)
        result = latch
    return result


def _make_formula_encoding(ctx, formula):
    if isinstance(formula, str):
        if formula not in ctx.nets:
            raise RuntimeError(f"Could not find '{formula}'")
        return ctx.nets[formula]
    for operator in formula:
        args = formula[operator]
        if operator in ('AND', 'OR'):
            enc_args = []
            for arg in args:
                enc_args.append(_make_formula_encoding(ctx, arg))
            result = None
            if operator == 'AND':
                result = ctx.mk_true()
            else:
                assert operator == 'OR'
                result = ctx.mk_false()
            for enc_arg in enc_args:
                if operator == 'AND':
                    result = ctx.mk_and(result, enc_arg)
                else:
                    assert operator == 'OR'
                    result = ctx.mk_or(result, enc_arg)
            return result
        if operator == 'NOT':
            return ctx.mk_not(_make_formula_encoding(ctx, args))
        if operator == 'PRE':
            nxt = _make_formula_encoding(ctx, args)
            latch = ctx.mk_latch(f'__pre_{nxt}', ctx.mk_boolean_type())
            ctx.set_latch_init_next(latch, ctx.mk_false(), nxt)
            return latch
    raise RuntimeError('Unhandled formula')


def encode_formula(ctx, input_string):
    """
    Encodes the formula passed as input into the context
    The context must contain the symbols mentioned in the
    input string
    """
    formula = parse_string(input_string)
    depth = compute_pre_depth(formula)
    trigger = _make_trigger_encoding(ctx, depth)
    itp_formula = _make_formula_encoding(ctx, formula)
    return ctx.mk_and(trigger, itp_formula)

"""
Implementation of REST API for nets creation
"""
from flask import Blueprint, request
from .utils import typename_to_type
from .contexts import contexts

nr = Blueprint('nets', __name__)

def _create_bool_constant(func):
    context = request.get_json()['context']
    if context is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    net = func(ctx)
    return {'result': ctx.net2name[net]}, 201

def _create_unary_gate(func):
    context = request.get_json()['context']
    x = request.get_json()['x']
    if context is None or x is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    x = ctx.nets[x]
    assert x is not None
    net = func(ctx, x)
    return {'result': ctx.net2name[net]}, 201

def _create_binary_gate(func):
    context = request.get_json()['context']
    x = request.get_json()['x']
    y = request.get_json()['y']
    if context is None or x is None or y is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    x = ctx.nets[x]
    y = ctx.nets[y]
    assert x is not None
    assert y is not None
    net = func(ctx, x, y)
    return {'result': ctx.net2name[net]}, 201

@nr.route('', methods=['GET'])
def list_nets():
    """
    Gets the list of the available nets
    """
    context = request.args.get('context')
    ctx = contexts[context]['context']
    return {'nets': [key for key, _ in ctx.nets.items()]}, 200

@nr.route('/true', methods=['POST'])
def create_true():
    """
    Creates the net true
    """
    return _create_bool_constant(lambda ctx : ctx.mk_true())

@nr.route('/false', methods=['POST'])
def create_false():
    """
    Creates the net false
    """
    return _create_bool_constant(lambda ctx : ctx.mk_false())

@nr.route('/numbers/create', methods=['POST'])
def create_number():
    """
    Creates a number
    """
    context = request.get_json()['context']
    value = request.get_json()['value']
    typ = request.get_json()['type']
    if context is None or value is None or typ is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    assert value is not None
    assert typ is not None
    net = ctx.mk_number(value, typename_to_type(ctx, typ))
    return {'result': ctx.net2name[net]}, 201

@nr.route('/nots/create', methods=['POST'])
def create_not():
    """
    Creates a logical not
    """
    return _create_unary_gate(lambda ctx, x : ctx.mk_not(x))

@nr.route('/minuses/create', methods=['POST'])
def create_minus():
    """
    Creates an arithmetic minus
    """
    return _create_unary_gate(lambda ctx, x : ctx.mk_minus(x))

@nr.route('/ands/create', methods=['POST'])
def create_and():
    """
    Creates a logical and
    """
    return _create_binary_gate(lambda ctx, x, y : ctx.mk_and(x, y))

@nr.route('/ors/create', methods=['POST'])
def create_or():
    """
    Creates a logical or
    """
    return _create_binary_gate(lambda ctx, x, y : ctx.mk_or(x, y))

@nr.route('/implieses/create', methods=['POST'])
def create_implies():
    """
    Creates a logical implies
    """
    return _create_binary_gate(lambda ctx, x, y : ctx.mk_implies(x, y))

@nr.route('/xors/create', methods=['POST'])
def create_xor():
    """
    Creates a logical xor
    """
    return _create_binary_gate(lambda ctx, x, y : ctx.mk_xor(x, y))

@nr.route('/iffs/create', methods=['POST'])
def create_iff():
    """
    Creates a logical iff
    """
    return _create_binary_gate(lambda ctx, x, y : ctx.mk_iff(x, y))

@nr.route('/adds/create', methods=['POST'])
def create_add():
    """
    Creates an addition
    """
    return _create_binary_gate(lambda ctx, x, y : ctx.mk_add(x, y))

@nr.route('/muls/create', methods=['POST'])
def create_mul():
    """
    Creates a multiplication
    """
    return _create_binary_gate(lambda ctx, x, y : ctx.mk_mul(x, y))

@nr.route('/divs/create', methods=['POST'])
def create_div():
    """
    Creates a division
    """
    return _create_binary_gate(lambda ctx, x, y : ctx.mk_div(x, y))

@nr.route('/mods/create', methods=['POST'])
def create_mod():
    """
    Creates a modulus
    """
    return _create_binary_gate(lambda ctx, x, y : ctx.mk_mod(x, y))

@nr.route('/subs/create', methods=['POST'])
def create_sub():
    """
    Creates a subtraction
    """
    return _create_binary_gate(lambda ctx, x, y : ctx.mk_sub(x, y))

@nr.route('/eqs/create', methods=['POST'])
def create_eq():
    """
    Creates an equality
    """
    return _create_binary_gate(lambda ctx, x, y : ctx.mk_eq(x, y))

@nr.route('/leqs/create', methods=['POST'])
def create_leq():
    """
    Creates an less or equal
    """
    return _create_binary_gate(lambda ctx, x, y : ctx.mk_leq(x, y))

@nr.route('/geqs/create', methods=['POST'])
def create_geq():
    """
    Creates a greater or equal
    """
    return _create_binary_gate(lambda ctx, x, y : ctx.mk_geq(x, y))

@nr.route('/lts/create', methods=['POST'])
def create_lt():
    """
    Creates a less than
    """
    return _create_binary_gate(lambda ctx, x, y : ctx.mk_lt(x, y))

@nr.route('/gts/create', methods=['POST'])
def create_gt():
    """
    Creates a greater than
    """
    return _create_binary_gate(lambda ctx, x, y : ctx.mk_gt(x, y))

@nr.route('/neqs/create', methods=['POST'])
def create_neq():
    """
    Creates a not equal
    """
    return _create_binary_gate(lambda ctx, x, y : ctx.mk_neq(x, y))

@nr.route('/ites/create', methods=['POST'])
def create_ite():
    """
    Creates an if then else
    """
    context = request.get_json()['context']
    x = request.get_json()['x']
    y = request.get_json()['y']
    z = request.get_json()['z']
    if context is None or x is None or y is None or z is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    i = ctx.nets[x]
    t = ctx.nets[y]
    e = ctx.nets[z]
    assert i is not None
    assert t is not None
    assert e is not None
    net = ctx.mk_ite(i, t, e)
    return {'result': ctx.net2name[net]}, 201

@nr.route('/casts/create', methods=['POST'])
def create_cast():
    """
    Creates a type cast
    """
    context = request.get_json()['context']
    x = request.get_json()['x']
    t = request.get_json()['type']
    if context is None or x is None or t is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    x = ctx.nets[x]
    assert ctx is not None
    assert x is not None
    net = None
    if t == 'int8':
        net = ctx.mk_cast_to_int8(x)
    elif t == 'int16':
        net = ctx.mk_cast_to_int16(x)
    elif t == 'int32':
        net = ctx.mk_cast_to_int32(x)
    elif t == 'int64':
        net = ctx.mk_cast_to_int64(x)
    elif t == 'uint8':
        net = ctx.mk_cast_to_uint8(x)
    elif t == 'uint16':
        net = ctx.mk_cast_to_uint16(x)
    elif t == 'uint32':
        net = ctx.mk_cast_to_uint32(x)
    elif t == 'uint64':
        net = ctx.mk_cast_to_uint64(x)
    else:
        return {'result': 'unhandled type {}'.format(t)}, 400
    assert net is not None
    return {'result': ctx.net2name[net]}, 201

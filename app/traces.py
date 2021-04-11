from flask import Blueprint, request, jsonify

from intrepyd.trace import Trace

tr = Blueprint('traces', __name__)

from .contexts import contexts

@tr.route('/create', methods=['POST'])
def create_trace():
    context = request.get_json()['context']
    if context is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    assert(ctx is not None)
    name = 't{}'.format(len(contexts[context]['traces']))
    contexts[context]['traces'][name] = ctx.mk_trace()
    return {'result': name}, 201

def on_trace(request, func):
    context = request.args.get('context')
    trace = request.args.get('trace')
    if context is None or trace is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    tr = contexts[context]['traces'][trace]
    assert(ctx is not None)
    assert(tr is not None)
    return func(ctx, tr)

@tr.route('/maxdepth', methods=['GET'])
def get_max_depth():
    return on_trace(request,
                    lambda _, tr : ({'result': tr.get_max_depth()}, 200))

def get_values_helper(ctx, tr):
    tracedict = tr.get_as_net_dictionary()
    return {'result': {ctx.net2name[net]: tracedict[net] for net in tracedict}}, 200

@tr.route('/values', methods=['GET'])
def get_values():
    return on_trace(request, get_values_helper)

@tr.route('/value', methods=['GET'])
def get_value():
    context = request.args.get('context')
    trace = request.args.get('trace')
    depth = request.args.get('depth')
    net = request.args.get('net')
    if context is None or trace is None or depth is None or net is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    assert(ctx is not None)
    tr = contexts[context]['traces'][trace]
    ne = ctx.nets[net]
    assert(tr is not None)
    assert(ne is not None)
    de = int(depth)
    result = tr.get_value(ne, de)
    return {'result': result}, 200

@tr.route('/setvalue', methods=['PUT'])
def set_value():
    context = request.get_json()['context']
    trace = request.get_json()['trace']
    depth = request.get_json()['depth']
    net = request.get_json()['net']
    value = request.get_json()['value']
    if context is None or trace is None or depth is None or net is None or value is None:
        return {'result': 'error'}, 400
    tr = contexts[context]['traces'][trace]
    ne = contexts[context]['nets'][net]
    assert(tr is not None)
    assert(ne is not None)
    de = int(depth)
    tr.set_value(ne, de, value)
    return {'result': 'ok'}, 200
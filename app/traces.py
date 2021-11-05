"""
Implementation of REST API for traces
"""
from flask import Blueprint, request
from .contexts import contexts

tr = Blueprint('traces', __name__)

@tr.route('/create', methods=['POST'])
def create_trace():
    """
    Creates an empty trace given a context
    """
    context = request.get_json()['context']
    if context is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    assert ctx is not None
    name = 't{}'.format(len(contexts[context]['traces']))
    contexts[context]['traces'][name] = ctx.mk_trace()
    return {'result': name}, 201

def _on_trace(req, func):
    context = req.args.get('context')
    trace = req.args.get('trace')
    if context is None or trace is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    trace = contexts[context]['traces'][trace]
    assert ctx is not None
    assert trace is not None
    return func(ctx, trace)

@tr.route('/maxdepth', methods=['GET'])
def get_max_depth():
    """
    Gets the max depth of the trace
    """
    return _on_trace(request,
                    lambda _, tr : ({'result': tr.get_max_depth()}, 200))

def _get_values_helper(ctx, trace):
    tracedict = trace.get_as_net_dictionary()
    return {'result': {ctx.net2name[net]: tracedict[net] for net in tracedict}}, 200

@tr.route('/values', methods=['GET'])
def get_values():
    """
    Gets the values for the trace
    """
    return _on_trace(request, _get_values_helper)

@tr.route('/value', methods=['GET'])
def get_value():
    """
    Gets a value for the trace, at a given depth
    """
    context = request.args.get('context')
    trace = request.args.get('trace')
    depth = request.args.get('depth')
    net = request.args.get('net')
    if context is None or trace is None or depth is None or net is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    assert ctx is not None
    trace = contexts[context]['traces'][trace]
    net = ctx.nets[net]
    assert trace is not None
    assert net is not None
    depth = int(depth)
    result = trace.get_value(net, depth)
    return {'result': result}, 200

@tr.route('/setvalue', methods=['PUT'])
def set_value():
    """
    Sets a value for a net at a given depth
    """
    context = request.get_json()['context']
    trace = request.get_json()['trace']
    depth = request.get_json()['depth']
    net = request.get_json()['net']
    value = request.get_json()['value']
    if context is None or trace is None or depth is None or net is None or value is None:
        return {'result': 'error'}, 400
    trace = contexts[context]['traces'][trace]
    net = contexts[context]['nets'][net]
    assert trace is not None
    assert net is not None
    depth = int(depth)
    trace.set_value(net, depth, value)
    return {'result': 'ok'}, 200

"""
Implementation of REST API for simulation
"""
from flask import Blueprint, request
from .contexts import contexts

sr = Blueprint('simulators', __name__)

@sr.route('/create', methods=['POST'])
def create_simulator():
    """
    Creates a simulator, given a context
    Method POST
    """
    context = request.get_json()['context']
    if context is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    assert ctx is not None
    name = 's{}'.format(len(contexts[context]['simulators']))
    contexts[context]['simulators'][name] = ctx.mk_simulator()
    return {'result': name}, 201

@sr.route('/simulate', methods=['PUT'])
def simulate():
    """
    Runs a simulation given a context, a simulator, a trace, and a depth
    Method PUT
    """
    context = request.get_json()['context']
    simulator = request.get_json()['simulator']
    trace = request.get_json()['trace']
    depth = request.get_json()['depth']
    if context is None or simulator is None or trace is None or depth is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    sim = contexts[context]['simulators'][simulator]
    tra = contexts[context]['traces'][trace]
    dep = int(depth)
    assert ctx is not None
    assert sim is not None
    assert tra is not None
    sim.simulate(tra, dep)
    return {'result': 'ok'}, 200

@sr.route('/watch', methods=['PUT'])
def add_value():
    """
    Adds a value to watch
    Method PUT
    """
    context = request.get_json()['context']
    simulator = request.get_json()['simulator']
    net = request.get_json()['net']
    if context is None or simulator is None or net is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    sim = contexts[context]['simulators'][simulator]
    assert ctx is not None
    assert sim is not None
    assert net is not None
    net = ctx.nets[net]
    sim.add_watch(net)
    return {'result': 'ok'}, 200

from flask import Blueprint, request, jsonify, session

lr = Blueprint('latches', __name__)

from .utils import typename_to_type
from .contexts import contexts

@lr.route('', methods=['GET'])
def list_latches():
    context = request.args.get('context')
    if context is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    return {'latches': [key for key, _ in ctx.latches.items()]}, 200

@lr.route('/create', methods=['POST'])
def create_latch():
    context = request.get_json()['context']
    typ = request.get_json()['type']
    if context is None or typ is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    name = '__l{}'.format(len(ctx.latches.items()))
    ctx.mk_latch(name, typename_to_type(ctx, typ))
    return {'result': name}, 201

@lr.route('/initnext', methods=['PUT'])
def set_latch_init_next():
    context = request.get_json()['context']
    latch = request.get_json()['latch']
    init = request.get_json()['init']
    nex = request.get_json()['next']
    if context is None or latch is None or init is None or nex is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    latch_net = ctx.nets[latch]
    init_net = ctx.nets[init]
    next_net = ctx.nets[nex]
    ctx.set_latch_init_next(latch_net, init_net, next_net)
    return {'result': 'ok'}, 200


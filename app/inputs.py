"""
APIs for inputs
"""

from flask import Blueprint, request

ir = Blueprint('inputs', __name__)

from .utils import typename_to_type
from .contexts import contexts

@ir.route('', methods=['GET'])
def list_inputs():
    context = request.args.get('context')
    if context is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    return {'inputs': [key for key, _ in ctx.inputs.items()]}, 200

@ir.route('/create', methods=['POST'])
def create_input():
    context = request.get_json()['context']
    typ = request.get_json()['type']
    if context is None or typ is None:
        return {'result': 'error'}, 400
    ctx = contexts[context]['context']
    assert(ctx is not None)
    name = '__i{}'.format(len(ctx.inputs.items()))
    ctx.mk_input(name, typename_to_type(ctx, typ))
    return {'result': name}, 201

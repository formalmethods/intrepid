from flask import Blueprint, request
from intrepyd import Context

cr = Blueprint('contexts', __name__)

contexts = {}

@cr.route('', methods=['GET'])
def list_contexts():
    return {'contexts': [name for name in contexts]}, 200

@cr.route('/create', methods=['POST'])
def create_context():
    name = request.get_json()['name']
    if name is None:
        return {'result': 'error'}, 400
    ctx = Context()
    if name in contexts:
        return {'result': 'error'}, 400
    contexts[name] = {'context': ctx,
                      'engines': {},
                      'traces': {},
                      'simulators': {}}
    return {'result': name}, 201

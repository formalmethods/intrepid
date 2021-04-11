from flask import Blueprint, request
from intrepyd.api import apitrace_dump_to_file

dr = Blueprint('debug', __name__)

@dr.route('/apitracedump', methods=['POST'])
def apitracedump():
    filepath = request.get_json()['filepath']
    if filepath is None:
        return {'result': 'error'}, 400
    apitrace_dump_to_file(filepath)
    return {'result': 'ok'}, 201

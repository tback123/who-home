'''
    Auth Routes Flask Blueprint
'''
from json import dumps
from flask import Blueprint, request
from auth import register

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def auth_register_root():
    '''
        Auth register wrapper
    '''
    payload = request.get_json()
    return dumps(register.register(payload['email'], payload['password'], payload['name_first'], payload['name_last']))

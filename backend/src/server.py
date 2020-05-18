'''
    Main Server Run File

    How our backend is structured
        On startup
            - Load the 'store' file
              into global dictionary
      Periodically
            - Every 1 seconds
            - Pickle dictionary into file
'''

import sys
from json import dumps
from flask import Flask, request
from flask_cors import CORS

def default_handler(err):
    ''' Default Handle '''
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response


APP = Flask(__name__)
CORS(APP)

APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, default_handler)

################## AUTH ROUTES ##################

@APP.route("/auth/register", methods=['POST'])
def auth_register_root():
    ''' Register User '''
    payload = request.get_json()
    email = payload['email']
    password = payload['password']
    name_first = payload['name_first']
    name_last = payload['name_last']
    return dumps(
        auth_register(email, password, name_first, name_last)
    )

@APP.route("/auth/login", methods=['POST'])
def auth_login_root():
    ''' Login a user '''
    payload = request.get_json()
    return dumps(auth_login(payload['email'], payload['password']))

@APP.route("/auth/logout", methods=['POST'])
def auth_logout_root():
    ''' Logs out a user '''
    payload = request.get_json()
    return dumps(auth_logout(payload['token']))

@APP.route("/auth/passwordreset/request", methods=['POST'])
def auth_passwordreset_request_root():
    ''' Request password reset '''
    payload = request.get_json()
    return dumps(auth_passwordreset_request(payload['email']))

@APP.route("/auth/passwordreset/reset", methods=['POST'])
def auth_passwordreset_reset_root():
    ''' Changes a users password '''
    payload = request.get_json()
    return dumps(auth_passwordreset_reset(payload['reset_code'], payload['new_password']))

################# END AUTH ROUTES ###############

if __name__ == "__main__":
    APP.run(port=(int(sys.argv[1]) if len(sys.argv) == 2 else 8080))

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
from routes.auth_routes import auth_bp

APP = Flask(__name__)
CORS(APP)

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

APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, default_handler)

APP.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == "__main__":
    APP.run(port=(int(sys.argv[1]) if len(sys.argv) == 2 else 8080))

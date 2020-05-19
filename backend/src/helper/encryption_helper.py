''' Functions for encryption '''

import hashlib
import random
import string
from datetime import datetime
from secrets import TOKEN_SECRET
import jwt

def hash_password(password):
    ''' Returns a hash of tha password as a string '''
    return str(hashlib.sha256(password.encode()).hexdigest())

def generate_token():
    ''' Returns a random token string '''

    random_data = {
        "datetime" : str(datetime.now()),
        "randomnumber" : str(random.random())
    }

    token = str(jwt.encode(random_data, TOKEN_SECRET, algorithm='HS256'))
    return str(token)

def generate_random_string(len_of_str=10):
    '''
        Returns a random alphanumeric string with a fixed count of letters and digits

        This code taken from https://pynative.com/python-generate-random-string/
    '''
    char_possibilities = string.ascii_letters + string.digits
    return ''.join((random.choice(char_possibilities) for i in range(len_of_str)))

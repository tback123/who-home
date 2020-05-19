'''
    Helper functions for generating and checking IDs
'''

import random
from datetime import datetime
from store import get_store

def is_u_id_in_use(u_id):
    '''
        Checks if the user id is in use
        Returns True or False
    '''

    for user in get_store().get_users_list():
        if u_id == user['u_id']:
            return True

    return False

def new_u_id():
    '''
        Returns a new unique u_id int.
        This u_id will never have been previosuly used
    '''
    u_id = None
    while is_u_id_in_use(u_id) or u_id is None:
        u_id = int(datetime.now().timestamp() + random.randint(0, 10000))

    return u_id

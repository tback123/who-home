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

def is_h_id_in_use(h_id):
    '''
        Checks if the household id is in use
        Returns True or False
    '''

    for household in get_store().get_households_list():
        if h_id == household['h_id']:
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

def new_h_id():
    '''
        Returns a new unique h_id int.
        This h_id will never have been previosuly used
    '''
    h_id = None
    while is_h_id_in_use(h_id) or h_id is None:
        h_id = int(datetime.now().timestamp() + random.randint(0, 10000))

    return h_id


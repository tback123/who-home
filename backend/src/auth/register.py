'''
    Auth register function
'''
from store import get_store
from helper import encryption_helper

def register(email, password, name_first, name_last):
    '''
        Registers a new user

        Input: Email, password, first name, last name
        Returns: Dictionary of User ID and a current session token
    '''
    store = get_store()

    # Error Checking

    # Generate a u_id
    u_id = 1

    # Generate a token
    token = encryption_helper.generate_token()

    store.add_user(u_id, email, password, name_first, name_last, token)
    return {
        'u_id': u_id,
        'token': token
    }

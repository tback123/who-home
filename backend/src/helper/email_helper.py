'''Contains email related functions'''

import re
from error import InputError
from store import get_store

def is_correct_email_format(email):
    '''
        Returns True or False if email in correct format

        Code taken from
        https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
        As surgested by assignment spec, under auth/register Errors
    '''
    # Make a regular expression for validating an Email
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    if not re.search(regex, email):
        return False

    return True

def is_email_in_use(email):
    '''
        Returns True or False if email is already in use
    '''

    store = get_store()
    users = store.get_all_users()
    for user in users:
        if user.get_email() == email:
            return True

    return False

def validate_email(email):
    '''
        Raises error is invalid email or inuse
        Else does nothing
     '''
    if not is_correct_email_format(email):
        raise InputError(description="Wrong Email Format")

    if is_email_in_use(email):
        raise InputError(description="Email Already In Use")
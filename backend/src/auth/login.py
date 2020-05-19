'''
    Auth login function
'''

from store import get_store
from helper import email_helper, arg_helper

def auth_login(email, password):
    
    ''' Login a user'''

    store = get_store()

    email, password = arg_helper.strip_all_args((email, password))
    arg_helper.check_no_white_space((email,password))

    email_helper.validate_new_email(email)

    




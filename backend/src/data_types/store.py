'''
    Defines a class structue for the data store
    Creates a data store and
    Syncs it every second to a file
'''

class Store:
    ''' Defines the Store Class '''
    def __init__(self):
        self.__users = []
        self.__channels = []

    def get_all_users(self):
        ''' Returns list of all users'''
        return self.__users

    def add_user(self, new_user):
        ''' Adds User Object to list of users'''
        self.__users.append(new_user)

    def remove_user_by_id(self, user_id):
        ''' Removes user from list of users by id '''
        user_to_remove = next((user for user in self.__users if user.get_u_id() == user_id), None)
        self.__users.remove(user_to_remove)

    def get_user_by_id(self, user_id):
        ''' Returns a User object given a u_id '''
        return next((user for user in self.__users if user.get_u_id() == user_id), None)

    def reset_store(self):
        ''' Clears store '''
        self.__users = []


STORE = Store()

def get_store():
    ''' Return the global store '''
    global STORE
    return STORE
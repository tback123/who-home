'''
    Defines a class structue for the data store
    Creates a data store and
    Syncs it every second to a file
'''

from secrets import MONGODB_URL, MONGODB_NAME
import pymongo

class Store:
    ''' Defines the Store Class '''

    def __init__(self):
        __db = pymongo.MongoClient(MONGODB_URL)[MONGODB_NAME]
        self.__users = __db["users"]
        self.__households = __db["households"]

    def get_user_collection(self):
        ''' Returns mongoDB user collection'''
        return self.__users

    def get_household_collection(self):
        ''' Returns mongoDB household collection'''
        return self.__households

    def get_users_list(self):
        ''' Returns list of dictionaries of users '''
        return_lst = []
        for usr in self.__users.find():
            return_lst.append(usr)

        return return_lst

    def get_household_list(self):
        ''' Returns list of dictionaries of household '''
        return_lst = []
        for house in self.__households.find():
            return_lst.append(house)

        return return_lst

    def update_one_user(self, u_id, new_attribute_dict):
        '''
            Given a user_id, will update that specific user's attribute, 
            as assigned in the second argument
        '''
        self.__users.update_one({u_id: u_id}, new_attribute_dict)

    def update_one_household(self, h_id, new_attribute_dict):
        '''
            Given a user_id, will update that specific user's attribute, 
            as assigned in the second argument
        '''
        self.__households.update_one({h_id: h_id}, new_attribute_dict)

STORE = Store()

def get_store():
    ''' Return the global store '''
    global STORE
    return STORE

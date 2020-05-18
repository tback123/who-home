''' Defines the householdd class '''

class household:
    ''' The class for each household '''

    def __init__(self, household_name, h_id, owner_u_id):
        self.__household_name = household_name
        self.__h_id = h_id
        self.__owner_ids = []
        self.__owner_ids.append(owner_u_id)
    
    
        
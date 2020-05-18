''' Defines a user class '''

class User:
    ''' Defines a new User type '''

    def __init__(self, u_id, email, password, name_first, name_last,
                 token):
        self.__u_id = u_id
        self.__email = email
        self.__password = password
        self.__name_first = name_first
        self.__name_last = name_last
        self.__token = token
        self.__password_reset_code = None

    def get_u_id(self):
        ''' Returns u_id of user '''
        return self.__u_id

    def get_email(self):
        ''' Returns email of user '''
        return self.__email

    def set_email(self, new_email):
        ''' Sets email of user '''
        self.__email = new_email

    def get_password(self):
        ''' Returns the password for user '''
        return self.__password

    def set_password(self, new_password):
        ''' Sets the password for the user '''
        self.__password = new_password

    def get_name_first(self):
        ''' Returns the first name of the user '''
        return self.__name_first

    def set_name_first(self, new_name):
        ''' Sets the first name of the user '''
        self.__name_first = new_name

    def get_name_last(self):
        ''' Returns the last name of the user '''
        return self.__name_last

    def set_name_last(self, new_name):
        ''' Sets the last name of the user '''
        self.__name_last = new_name

    def get_token(self):
        ''' Returns the token of the user '''
        return self.__token

    def set_token(self, new_token):
        ''' Sets the token of the user '''
        self.__token = new_token

    def get_password_reset_code(self):
        ''' Returns the current password reset code '''
        return self.__password_reset_code

    def set_password_reset_code(self, new_code):
        ''' Sets a new password reset code '''
        self.__password_reset_code = new_code

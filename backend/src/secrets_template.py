'''
    Stores all encryption secrets

    Rename this file "secrets.py" to use this file
    Fill in the required config elements

'''

# The External URL of the backend, used for testing
BACKEND_URL = 'http://127.0.0.1:8080'

'''
Data Base settings
'''
# Server Address
MONGODB_URL = 'mongodb://localhost:27017'
# Name of Database to use within server
MONGODB_NAME = 'who-home'

'''
Config used for the service emails
'''
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_EMAIL = ""
SMTP_PASSWORD = ""

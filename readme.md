# Who's Home

Who's home is a family managemnt tool for managing and seeing who will be home for dinner each night.

The following user stories define the functionality of the system

## Technology stack

### Frontend 

- Javascript
- React
- Material UI

### Backend

- Django (Currently)
- Flask (In transition)

- MongoDB (In Plans)

## User stories

- As a parent, I want to see who will be home each night in advance, so that I can arrange dinner.
- As a member of the house hold, I want to tell people If I will be home for dinner tonight, So that I am accounted for.
- As a parent, I want to choose a specific time by which people have to choose if they're home, so that i am able to do the shopping for dinner.
- As a memeber of the house hold, I want to be able to choose who my plus one is, so that other know what to expect.
- As a family orginiser, I want to be able to say whats for dinner, So that people can decide if they want to come.
- As a forgetful person, I want to be able to automate the process of checking and unchecking my status at home through our home Wi-Fi.

## Functional Requirements

- Ability for each member of the family to login with a username and password

## API 

|HTTP Route|HTTP Method|Parameters|Return type|Exceptions|Description|
|------------|-------------|-------------|----------|-----------|----------|
|auth/login|POST|(email, password)|{ u_id, token }|**InputError** when any of:<ul><li>Email entered is not a valid email using the method provided [here](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/) (unless you feel you have a better method)</li><li>Email entered does not belong to a user</li><li>Password is not correct</li></ul> | Given a registered users' email and password and generates a valid token for the user to remain authenticated |
|auth/logout|POST|(token)|{ is_success }|N/A|Given an active token, invalidates the taken to log the user out. If a valid token is given, and the user is successfully logged out, it returns true, otherwise false. |
|auth/register|POST|(email, password, name_first, name_last)|{ u_id, token }|**InputError** when any of:<ul><li>Email entered is not a valid email using the method provided [here](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/) (unless you feel you have a better method).</li><li>Email address is already being used by another user</li><li>Password entered is less than 6 characters long</li><li>name_first not is between 1 and 50 characters inclusive in length</li><li>name_last is not between 1 and 50 characters inclusive in length</ul>|Given a user's first and last name, email address, and password, create a new account for them and return a new token for authentication in their session. A handle is generated that is the concatentation of a lowercase-only first name and last name. If the concatenation is longer than 20 characters, it is cutoff at 20 characters. If the handle is already taken, you may modify the handle in any way you see fit to make it unique. |
|auth/passwordreset/request|POST|(email)|{}|N/A|Given an email address, if the user is a registered user, send's them a an email containing a specific secret code, that when entered in auth_passwordreset_reset, shows that the user trying to reset the password is the one who got sent this email.|
|auth/passwordreset/reset|POST|(reset_code, new_password)|{}|**InputError** when any of:<ul><li>reset_code is not a valid reset code</li><li>Password entered is not a valid password</li>|Given a reset code for a user, set that user's new password to the password provided|
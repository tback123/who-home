# Who's Home

Who's home is a family managemnt tool for managing and seeing who will be home for dinner each night.

The following user stories define the functionality of the system

## Technology stack

### Frontend

- Javascript
- React
- Material UI

### Backend

- Django (Previously)
- Flask (Currently)
- MongoDB (In Plans)

## How to use 
### First time setup
In the `backend` folder, rename the `secrets_temple.py` to `secrets.py`.
Fill in the config as documented in that file.

### Start the frontend
Change in the frontend folder:  
`cd frontend/`

Install Packages:  
`npm install'

Run the frontend server:  
`npm start`

### Start the backend
in a new terminal, navigate to the root directory then change into the backend folder:  
`cd backend/`

Install Requirements  
`pip3 install -r requirements.txt`

Run Server:  
`python3 server.py`


## User stories

- As a parent, I want to see who will be home each night in advance, so that I can arrange dinner.
- As a member of the house hold, I want to tell people If I will be home for dinner tonight, So that I am accounted for.
- As a parent, I want to choose a specific time by which people have to choose if they're home, so that i am able to do the shopping for dinner.
- As a memeber of the house hold, I want to be able to choose who my plus one is, so that other know what to expect.
- As a family orginiser, I want to be able to say whats for dinner, So that people can decide if they want to come.
- As a forgetful person, I want to be able to automate the process of checking and unchecking my status at home through our home Wi-Fi.
- As a member, I want to be able to set my status as away, so that I'm not reminded to set my status while I'm away

### Potential out of scope ideas

- Admin users (Ability to set other members status)
- Short description of where you are if you're away
- Set curfuee for time to answer survey
- Multiple house holds, ability to toggle between them
- Daily Message board for family
- Recurrant reminders e.g. bins every thursday

## Functional Requirements

- Ability for each member of the family to login with a username and password

## API

|HTTP Route|HTTP Method|Parameters|Return type|Exceptions|Description|
|------------|-------------|-------------|----------|-----------|----------|
|auth/login|POST|(email, password)|{ u_id, token }|**InputError** when any of:<ul><li>Email entered is not a valid email using the method provided [here](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/) (unless you feel you have a better method)</li><li>Email entered does not belong to a user</li><li>Password is not correct</li></ul> | Given a registered users' email and password and generates a valid token for the user to remain authenticated |
|auth/register|POST|(email, password, name_first, name_last)|{ u_id, token }|**InputError** when any of:<ul><li>Email entered is not a valid email using the method provided [here](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/) (unless you feel you have a better method).</li><li>Email address is already being used by another user</li><li>Password entered is less than 6 characters long</li><li>name_first not is between 1 and 50 characters inclusive in length</li><li>name_last is not between 1 and 50 characters inclusive in length</ul>|Given a user's first and last name, email address, and password, create a new account for them and return a new token for authentication in their session. A handle is generated that is the concatentation of a lowercase-only first name and last name. If the concatenation is longer than 20 characters, it is cutoff at 20 characters. If the handle is already taken, you may modify the handle in any way you see fit to make it unique. |
| auth/logout | POST | (token) |{ is_success } | No exceptions | Given an active token, invalidates to log user out. If a valid token is given and the user is sucessfully logged out, it returns true, otherwise, false.|
|auth/passwordreset/request|POST|(email)|{}|N/A|Given an email address, if the user is a registered user, send's them a an email containing a specific secret code, that when entered in auth_passwordreset_reset, shows that the user trying to reset the password is the one who got sent this email.|
|auth/passwordreset/reset|POST|(reset_code, new_password)|{}|**InputError** when any of:<ul><li>reset_code is not a valid reset code</li><li>Password entered is not a valid password</li></ul>|Given a reset code for a user, set that user's new password to the password provided|
|status/set| PUT | (token, u_id, house_id, new_status) | {is_success} | **InputError** when any of: <ul><li>Token is invalid</li><li>u_id is invalid</li><li>Status is not valid</li><li>User doesn't exist within the house</li></ul> **Access Error** <ul><li>If token doesn't match assigned u_id and not family admin (So a user can only set their own home status)</li> </ul> | Sets status for given u_id |
| status/get_all | GET | (token, house_id) | {members} | **InputError** <ul><li>Invalid Token</li><li>Invalid House id</li> </ul> **AccessError** <ul><li>Token is not authorised in specified house_id</li> </ul> | Returns all the members in the house hold and their current statuses|
|household/create|POST| (token, household_name)| {is_success} |  **InputError** <ul><li>Invalid Token</li></ul> | Creates a new household |
|household/add_member| PUT | (token, house_id, email)| {is_success} | **InputError** <ul><li>Invalid Token</li><li>Invalid House id</li><li>Not a registered email</li></ul>| Adds registered memeber to existing household. User that creates the household, is an admin of that househould.|
|household/remove_member| DELETE | (token, house_id, email)| {is_success} | **InputError** <ul><li>Invalid Token</li><li>Invalid House id</li><li>Requesting user is not in that household</li><li>Not an email in the current household</li></ul>| Removed registered memeber to existiing household|
|household/add_admin| PUT | (token, house_id, email_to_add)  | {is_success} | **InputError** <ul><li>Invalid Token</li><li>Invalid House id</li><li>Requesting user is not an admin of that household</li><li>Requesting user is not in that household</li><li>email_to_add is not in the current household</li></ul> | Adds an admin to an existing household |
|household/remove_admin| DELETE | (token, house_id, email_to_remove)  | {is_success} | **InputError** <ul><li>Invalid Token</li><li>Invalid House id</li><li>Requesting user is not an admin of that household</li><li>Requesting user is not in that household</li><li>email_to_add is not in the current household</li></ul> | Adds an admin to an existing household |


### Data Stuctures

| Named | Type |
| ----- | ---- |
| "status"| "home" OR "not_home" OR "home_with_extras" |
| "members"| A list of dictionaries of each member where each dictionary contains {name_first, status}|
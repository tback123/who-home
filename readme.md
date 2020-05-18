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
| auth/logout | POST | (token) |{ is_success } | No exceptions | Given an active token, invalidates to log user out. If a valid token is given and the user is sucessfully logged out, it returns true, otherwise, false.|

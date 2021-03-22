import re
import jwt
from random import randrange
from errors import AccessError, ValueError

JWTSECRET = 'myjwtsecret'
PASS_MIN_LENGTH = 6
NAME_MIN_LENGTH = 1
NAME_MAX_LENGTH = 50
HANDLE_MAX_LENGTH = 20
EMAIL_MAX_LENGTH = 50

def checkEmail(email):
    if len(email) > EMAIL_MAX_LENGTH:
        raise ValueError ('Email cannot be more than 50 characters')
    
    regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    if(re.search(regex,email)):  
        return True
    else:  
        raise ValueError ('Email entered is not a valid')

def emailExists(email, data):
    for user in data['users']:
        if email == user['email']:
            return True
    return False

def checkPassword(password):
    if len(password) < PASS_MIN_LENGTH:
        raise ValueError ('Password entered is less than 6 characters long')

def checkName(nameFirst, nameLast):
    if len(nameFirst) > NAME_MAX_LENGTH or len(nameFirst) < NAME_MIN_LENGTH:
        raise ValueError ('First name is not between 1 and 50 characters in length')

    if len(nameLast) > NAME_MAX_LENGTH or len(nameLast) < NAME_MIN_LENGTH:
        raise ValueError ('Last name is not between 1 and 50 characters in length')

def createHandle(nameFirst, nameLast):
    # Assuming nameFirst and nameLast are strings
    newHandle = nameFirst.lower() + nameLast.lower()
    if len(newHandle) > HANDLE_MAX_LENGTH:
        newHandle = newHandle[0:HANDLE_MAX_LENGTH]
    return newHandle
    
def randomHandle(handle):
    # Assuming there are less than 300 people with the same name
    newHandle = handle + str(randrange(300))
    if len(newHandle) > HANDLE_MAX_LENGTH:
        newHandle = handle[0:HANDLE_MAX_LENGTH-3] + str(randrange(300))
    return newHandle    

def uniqueHandle(data, handle):
    for users in data['users']:
        while handle == users['handle']:
            handle = randomHandle(handle)
    return handle

def createU_ID(data):
	# Creating u_id that resembles: U123456
	u_id = randrange(100000)
	for users in data['users']:
		while u_id == users['u_id']:
			u_id = randrange(100000)
	return int(u_id)

def getUserFromToken(token):
    try:
        decoded = jwt.decode(token, JWTSECRET, algorithms=['HS256'])
        return int(decoded['u_id'])
    except:
        raise ValueError("Token is invaild")

def validUser(data, u_id):
    for user in data['users']:
        if u_id == user['u_id']:
            return True
    return False

def createUser(data, email, hashedPassword, nameFirst, nameLast, handle, u_id, permission):
    newUser = {
        'email': email,
        'password': hashedPassword,
        'name_first': nameFirst,
        'name_last': nameLast,
        'handle': handle, 
        'u_id': u_id,
        'resetCode': None,
        'is_admin': permission,
        'img_url': None,
    }
    data['users'].append(newUser)
    return newUser

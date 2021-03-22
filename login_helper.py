from hash_password import hashPassword
from errors import ValueError, AccessError

def loginFunc(data, email, password):
    for user in data['users']:
        if user['email'] == email and user['password'] == hashPassword(password):  
            return user
        elif user['email'] == email and user['password'] != hashPassword(password):
            raise ValueError('Password is incorrect.')
    raise ValueError('Email does not belong to a user.')
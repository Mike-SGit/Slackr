from hash_password import hashPassword
from errors import AccessError, ValueError

def resetPasswordFunc(data, resetCode, newPassword):
    for user in data['users']:
        if user['resetCode'] == resetCode:
            user['password'] = hashPassword(newPassword)
            user['resetCode'] = None
            return None
    raise ValueError ('Reset code is not valid.')
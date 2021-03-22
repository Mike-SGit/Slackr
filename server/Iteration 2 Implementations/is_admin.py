PERMISSION1 = 1
PERMISSION2 = 2

def isServerOwner(data, u_id):
    for user in data['users']:
        if u_id in user['u_id']:
            if user['is_admin'] == PERMISSION1:
                return True
    return False

def isAdmin(data, u_id):
    for user in data['users']:
        if u_id in user['u_id']:
            if user['is_admin'] == PERMISSION1 or user['is_admin'] == PERMISSION2:
                return True
    return False

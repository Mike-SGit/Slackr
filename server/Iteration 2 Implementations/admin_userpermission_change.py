from auth_register_helper import getUserFromToken
from errors import AccessError, ValueError

PERMISSION1 = 1
PERMISSION2 = 2
PERMISSION3 = 3

def admin_userpermission_change(data, token, u_id, permission_id):
    # Decode token to match user
    auth_u_id = getUserFromToken(token)

    # Check whether auth_u_id has the permission to change
    for auth_user in data['users']:
        if auth_user['u_id'] == auth_u_id:
            if not auth_user['is_admin'] == PERMISSION1 and \
                not auth_user['is_admin'] == PERMISSION2:

                raise AccessError('The authorised user is not an admin or owner')

    # Check permission_id
    if permission_id != PERMISSION1 and \
        permission_id != PERMISSION2 and \
        permission_id != PERMISSION3:

        raise ValueError('permission_id does not refer to a value permission')


    # Check if u_id (the one that needs to be modified) exists
    exist = False
    for user in data['users']:
        if user['u_id'] == u_id:
            exist = True
            user['is_admin'] = permission_id

    # Raise error if u_id does not exist
    if exist == False:
        raise ValueError("u_id does not refer to a valid user")


from auth_register_helper import getUserFromToken
from errors import AccessError, ValueError
from json import dumps

def user_profile(data, token, u_id):
    profile = {}

    # Check if u_id exists
    exist = False
    for user in data['users']:
        if user['u_id'] == u_id:
            exist = True
            profile['email'] = user['email']
            profile['name_first'] = user['name_first']
            profile['name_last'] = user['name_last']
            profile['handle_str'] = user['handle']

    # Raise error u_id if not exist
    if exist == False:
        raise ValueError("u_id does not refer to a valid user")

    return profile

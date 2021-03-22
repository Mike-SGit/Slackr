from auth_register_helper import getUserFromToken
from errors import AccessError, ValueError


def user_profile_setname(data, token, name_first, name_last):

    # Check if the names are valid
    # Error will arise if vaild
    if not name_first.isalpha() or not name_last.isalpha():
        raise ValueError("Should contain alpha letters only")

    elif len(name_first) > 50:
        raise ValueError("First name can not be more than 50 characters")

    elif len(name_last) > 50:
        raise ValueError("Last name can not be more than 50 characters")


    # Decode token to match user
    u_id = getUserFromToken(token)
    # Reset
    for user in data['users']:
        if user['u_id'] == u_id:
            user['name_last'] = name_last
            user['name_first'] = name_first

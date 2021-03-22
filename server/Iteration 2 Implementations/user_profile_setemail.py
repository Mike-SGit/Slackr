from auth_register_helper import checkEmail, getUserFromToken
from errors import AccessError, ValueError

def user_profile_setemail(data, token, email):
    # Decode token to match user
    u_id = getUserFromToken(token)

    # Check email is vaild, use function in auth_register_helper
    checkEmail(email)

    # Reset
    for user in data['users']:
        if email in user['email']:
            raise ValueError("Email address is already being used")
        elif user['u_id'] == u_id:
            user['email'] = email

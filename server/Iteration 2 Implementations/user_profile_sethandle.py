from auth_register_helper import getUserFromToken
from errors import AccessError, ValueError

def user_profile_sethandle(data, token, handle_str):

    # Check if the handle is valid
    letter_number = True

    # Assumption: Has to be letter or number
    for i in handle_str:
        if not (i.isdigit() or i.isalpha()):
            letter_number = False

    if len(handle_str) > 20:
        raise ValueError("Should be no more than 20 characters")

    elif letter_number == False:
        raise ValueError("Handle can only be letters and digits")

    elif not handle_str:
        raise ValueError("Handle cannot be empty")


    # Reset it
    # Decode token to match user
    u_id = getUserFromToken(token)

    for user in data['users']:
        if user['handle'] == handle_str:
            raise ValueError("Handle is already being used")
        elif user['u_id'] == u_id:
            user['handle'] = handle_str

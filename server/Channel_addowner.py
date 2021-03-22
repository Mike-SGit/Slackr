from Channel_leave import is_channel
from Channel_leave import in_channel
from Error import AccessError

def channel_addowner (token, channel_id, u_id):
    curr_u_id = auth_login
    if is_not_owner(token, channel_id):
        raise AccessError ("current user is not owner within target channel")
    if is_channel (channel_id):
        if in_channel (token, channel_id):
            if is_not_owner(u_id, channel_id):
                #do something
                pass
            else:
                raise ValueError ("target user already owner")
        else:
            raise AccessError ("current user is not within target channel")
    else:
        raise ValueError ("channel is invalid")
    pass

def is_not_owner(token, channel_id):
    pass
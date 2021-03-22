from Channel_leave import is_channel
from Channel_leave import in_channel

def Channel_invite (token, channel_id, u_id):    
    if is_channel (token, channel_id):
        if in_channel (token, channel_id) and u_id not in channels_list():
            if is_valid_user (token, u_id):
                pass
            else: 
                raise ValueError ("u_id does not refer to a valid user")
        elif in_channel (token, channel_id) == False:
            raise ValueError ("user is not in channel")
        else:
            raise ValueError ("user to be invited is already in channel")
    else:
        raise ValueError ("channel_id is not a valid channel")

def is_valid_user (token, u_id):
    pass
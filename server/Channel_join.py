from Channels_list import channels_list
from Channel_leave import is_channel
from Channel_leave import in_channel
from Error import AccessError

def Channel_join (token, channel_id):
    if is_channel (token, channel_id):
        if in_channel (token, channel_id):
            return ValueError ("user already in target channel")
        elif is_private (token, channel_id) == False:
            #do something
            pass
        elif is_private (token, channel_id):
            return AccessError ("target channel is private")
    else:
        return ValueError("Channel is invalid")

def is_private (token, channel_id):
    pass

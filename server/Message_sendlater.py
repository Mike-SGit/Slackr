from Channels_list import invalid_token
from Channel_leave import is_channel
from Channel_leave import in_channel
from Error import AccessError
import time
def Message_sendlater(token, channel_id, message, time_sent):
    if invalid_token (token):
        raise ValueError ("invalid token")
    elif is_channel(token, channel_id):
        if in_channel (token, channel_id):
            if len(message) > 1000:
                return ValueError ("Message length > 1000 chars")
            elif time_sent < time.clock():
                return ValueError ("Invalid message send time")
            elif len(message) < 1000 and time_sent > time.clock():
                #do something
                pass
        else:
            return AccessError ("Not in channel")
    else:
        return ValueError ("Channel id invalid")
    

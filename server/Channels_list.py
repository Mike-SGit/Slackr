import Channels_listall
import Channel_details

def channels_list (token):
    if invalid_token(token):
        return ValueError ("Invalid token")
    else:
        user_channels = {}
        all_channels = Channels_listall(token)
        for channel in all_channels:
            if token in Channel_details['all_members'](channel):
                user_channels.append(channel)
        return user_channels

def invalid_token (token):
    pass
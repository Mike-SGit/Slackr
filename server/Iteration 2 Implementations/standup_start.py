import datetime
from channels_helper import standupActive
from channels_helper import channelExists
from channels_helper import userIsInChannel
import standup_helper

from auth_register_helper import getUserFromToken
import errors


def standup_start(data, token, channel_id):
    
    now = datetime.datetime.now()
    finish = now + datetime.timedelta(minutes = 15)

    if channelExists(data, channel_id) is False:
        return ValueError("Channel ID is not a valid channel.")
    if userIsInChannel(data, channel_id, u_id) is False:
        return AccessError
    if standupActive(data, channel_id, u_id) is False:
        data['channel_id']['standup_active'] = True
        data['channel_id']['standup_end'] = finish
    else:
        raise ValueError ("A standup is already running in this channel.")

    ##sets timer to end standup at 'finish' time/posts the standup message    
    standupEnd (data, channel_id, u_id, finish)
    return {
        'time_finish': finish,
    }



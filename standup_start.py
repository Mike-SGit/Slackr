import datetime
from channels_helper import channelExists
from channels_helper import userIsInChannel
from standup_helper import standupEnd
from standup_helper import standupNotActive
from standup_helper import checkTokenValidity
import errors

from auth_register_helper import getUserFromToken
from errors import AccessError, ValueError

def standupStartFunc(data, token, channel_id):
    u_id = getUserFromToken(token)
    now = datetime.datetime.now()
    finish = now + datetime.timedelta(minutes = 15)

    checkTokenValidity(token, data)
    userIsInChannel(data, channel_id, u_id)

    if channelExists(data, channel_id) is False:
        raise ValueError('Channel ID is not a valid channel.')
    if standupNotActive(data, channel_id, u_id) is True:
        for channel in data['channels']:
            if str(channel_id) == channel['channel_id']:
                channel['standup_active'] = True
                channel['standup_end'] = finish
    else:
        raise ValueError ('A standup is already running in this channel.')

    ##sets timer to end standup at 'finish' time/posts the standup message    
    standupEnd (data, channel_id, token, finish)
    return {
        'time_finish': finish,
    }



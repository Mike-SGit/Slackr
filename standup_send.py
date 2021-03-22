from channels_helper import channelExists
from channels_helper import userIsInChannel
from auth_register_helper import getUserFromToken
from standup_helper import standupStillActive
from errors import AccessError, ValueError

def standupSendFunc(data, token, channel_id, message):
    u_id = getUserFromToken(token)
    if channelExists(data, channel_id) is False:
        raise ValueError("Channel ID is not a valid channel.")
    if userIsInChannel(data, channel_id, u_id) is False:
        return AccessError("User is not in the channel.")
    if len(message) > 1000:
        raise ValueError ("Message exceeds 1000 char limit.")
    if standupStillActive(data, channel_id, u_id):
        alteredMessage = str(u_id) + ":" + message
        for channel in data['channels']:
            if channel == channel_id:
                channel['standup_message'].append(alteredMessage)
    else:
        raise ValueError ("An active standup is not currently running in this channel.")
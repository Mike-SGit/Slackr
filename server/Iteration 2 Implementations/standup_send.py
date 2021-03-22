from channels_helper import standupActive
from channels_helper import channelExists
from channels_helper import userIsInChannel
from auth_register_helper import getUserFromToken
import errors

def standup_send(data, token, channel_id, message):
    u_id = getUserFromToken(token)
    if channelExists(data, channel_id) is False:
        return ValueError("Channel ID is not a valid channel.")
    if userIsInChannel(data, channel_id, u_id) is False:
        return AccessError
    if len(message) > 1000:
        return ValueError ("Message exceeds 1000 char limit.")
    if standupStillActive(data, channel_id, u_id):
        alteredMessage = u_id + ":" + message
        data['channels']['channel_id']['standup_messages'] += alteredMessage
    else:
        raise ValueError ("An active standup is not currently running in this channel.")
from random import randrange
from errors import AccessError, ValueError
from is_admin import isServerOwner, isAdmin
CHANNEL_NAME_MAX_LEN = 20

def channelNameCheck(channelName):
    if len(channelName) > CHANNEL_NAME_MAX_LEN:
        raise ValueError ('Channel name exceeds the character limit of 20!')
    else:
        return True

def userIsInChannel(data, channel_id, auth_u_id):
    for channel in data['channels']:
        if channel_id == channel['channel_id']:
            if auth_u_id in channel['members']:
                return True
            else:
                raise AccessError ('Requesting user is not an authorised  member of the channel')
    return ValueError ('Channel does not exist.')

def addUserToChannel(data, channel_id, u_id):
    for channel in data['channels']:
        if channel_id == channel['channel_id']:
            if u_id in channel['members']:
                raise ValueError ('User is already a member of the channel!')
            else:
                channel['members'].append(u_id)
                return True
        
def addOwnerToChannel(data, channel_id, auth_u_id, u_id):
    for channel in data['channels']:
        if channel_id == channel['channel_id']:
            if u_id in channel['owners']:
                raise ValueError ('User is already an owner of the channel!')
            elif auth_u_id not in channel['owners'] or isServerOwner(data, auth_u_id):
                raise AccessError ('Invalid permission level; you are not an owner of this channel or server.')
            else:
                channel['owners'].append(u_id)
                return True
    return ValueError ('Channel does not exist.') 

def removeOwnerFromChannel(data, channel_id, auth_u_id, target_u_id):
    for channel in data['channels']:
        if channel_id == channel['channel_id']:
            if target_u_id not in channel['owners']:
                raise ValueError ('User is not an owner of the channel!')
            elif auth_u_id not in channel['owners'] or isServerOwner(data, auth_u_id):
                raise AccessError ('Invalid permission level; you are not an owner of this channel or server.')
            else:
                channel['owners'].remove(target_u_id)
                return True
    return ValueError ('Channel does not exist.') 

def channelExists(data, channel_id):
    for channel in data['channels']:
        if channel_id == channel['channel_id']:
            return True
    return False

def removeUserFromChannel(data, channel_id, u_id):
    for channel in data['channels']:
        if channel_id == channel['channel_id']:
            if u_id not in channel['members']:
                raise ValueError ('User is not a member of the channel!')
            else:
                channel['members'].remove(u_id)
                return True
    return ValueError ('Channel does not exist.') 

def joinChannel(data, channel_id, u_id):
    for channel in data['channels']:
        if channel_id == channel['channel_id']:
            if u_id in channel['members']:
                raise ValueError ('User is already a member of the channel!')
            elif channel['is_public'] is False and isAdmin(data, u_id) is False:
                raise AccessError ('Channel is private and you do not have admin permission access.')
            else:
                channel['members'].add(u_id)
                return True
    return ValueError ('Channel does not exist.') 

def standupActive (data, channel_id, u_id):
    for channel in data['channels']:
        if channel_id == channel['channel_id']:
            return channel['standup_active']
    return False
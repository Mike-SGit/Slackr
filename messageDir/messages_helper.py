import datetime
import time
from random import randrange

from auth_register_helper import getUserFromToken
from channels_helper import userIsInChannel

def editMessage(data, messageId, newMessage):
    for channel in data['channels']:
        for message in channel['messages']:
            if message['message_id'] == messageId:
                message['message'] = newMessage

def remove_message(data, messageId):
    for channel in data['channels']:
        for message in channel['messages']:
            if message['message_id'] == messageId:
                del message

def message_send(data, message, channelid, token):
    u_id = getUserFromToken(token)
    validate_message(data, message, channel_id, token, u_id)
    messageId = randrange(99999)
    for channel in data['channels']:
        while messageId in channel['messages']['message_id']:
            messageId = randrange(99999)
    data['channels']['messages'].append({
        'message_id': messageId,
        'u_id': u_id,
        'message': message,
        'time_created': time,
        'reacts': [{
            'react_id': 0,
            'u_id': u_id,
            'is_this_user_reacted': 0,
        }],
        'is_pinned': 0,
    })
    return messageId

def validate_remove(data, token, messageId):
    if token in data['tokens']:
        pass
    else:
        raise ValueError("invalid token")
    u_id = getUserFromToken(token)
    userIsInChannel(data, channel_id, getUserFromToken(token))
    exists = False
    for channel in data['channels']:
        for message in channel['messages']:
            if message['u_id'] == u_id:
                if message['message_id'] == messageId:
                    exists = True
    if exists == False:
        raise ValueError("Invalid IDs")

def validate_message(data, message, channelid, token, u_id):
    if channelid in data['channels']:
        pass
    else:
        raise ValueError("invalid token")
    u_id = getUserFromToken(token)
    userIsInChannel(data, channelid, u_id)
    if len(message) > 1000:
        raise ValueError("ValueError when:Message is more than 1000 characters")
    
        
def validate_messageLater(data, message, channelid, token, timeSend, Realtime):
    if channelid in data['channels']:
        pass
    else:
        raise ValueError("invalid token")
    u_id = getUserFromToken(token)
    userIsInChannel(data, channelid, u_id)

    
    #value error: Time sent is a time in the past
    #Value Error time sent is in past
    if len(message) > 1000:
        raise ValueError("ValueError when:Message is more than 1000 characters")

def messageExists(data, messageId):
    valid = False
    for channel in data['channels']:
        for message in channel['messages']:
            if message['message_id'] == messageId:
                if channel['members'].contains(u_id):
                    valid == True
    return valid

def isPinned(data, messageId):
    pinned = False
    for channels in data['channels']:
        for message in channels['messages']:
            if message['message_id'] == messageId:
                if not message['is_pinned'] == '0':
                    pinned = True

def pinMessage(data, token, messageId):
    if not messageExists(data, messageId):
        raise ValueError("That message does not exist")
    u_id = getUserFromToken(token)
    # Check whether user has the permission to pin
    for user in data['users']:
        if user['u_id'] == u_id:
            if not auth_user['is_admin'] == 2:
                raise ValueError('The authorised user is not an admin or owner')
    if isPinned(data, messageId):
        raise ValueError('That message is already pinned')
    #get the channels id
    for channel in data['channels']:
        for message in channel['messages']:
            if messageId == message['message_id']:
                cId = channel['channel_id']
                userIsInChannel(data, cId, u_id)
                #end of error checking
                message['is_pinned'] = 1

def unpinMessage(data, token, messageId):
    if not messageExists(data, messageId):
        raise ValueError("That message does not exist")
    u_id = getUserFromToken(token)
    # Check whether user has the permission to pin
    for user in data['users']:
        if user['u_id'] == u_id:
            if not auth_user['is_admin'] == 2:
                raise ValueError('The authorised user is not an admin or owner')
    if not isPinned(data, messageId):
        raise ValueError('That message is not yet pinned')
    #get the channels id
    for channel in data['channels']:
        for message in channel['messages']:
            if messageId == message['message_id']:
                cId = channel['channel_id']
                userIsInChannel(data, cId, u_id)
                #end of error checking
                message['is_pinned'] = 0



    
    
    
    


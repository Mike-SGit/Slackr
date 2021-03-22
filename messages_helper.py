import datetime
import time
from random import randrange
from errors import AccessError, ValueError
from auth_register_helper import getUserFromToken
from channels_helper import userIsInChannel



#editMessage(data, messageId, newMessagem token, channel_id)
def editMessage(data, messageId, newMessage, token):
    for channel in data['channels']:
        for message in channel['messages']:
            if message['message_id'] == messageId:
                channel_id = channel['channel_id']
    u_id = getUserFromToken(token)
    validate_message(data, newMessage, channel_id, token, u_id)
    validate_remove(data, token, messageId)
    for channel in data['channels']:
        for message in channel['messages']:
            if message['message_id'] == messageId:
                message['message'] = newMessage

def remove_message(data, messageId, token):
    validate_remove(data, token, messageId)
    mindex = 0
    cindex = 0
    foundm = 0
    foundc = 0
    for channel in data['channels']:
        for message in channel['messages']:
            if message['message_id'] == messageId:
                foundc = cindex
                foundm = mindex
                #print("we tried")
            mindex = mindex + 1
        cindex = cindex + 1
    del data['channels'][foundc]['messages'][foundm]

def message_send(data, message, channel_id, token):
    u_id = getUserFromToken(token)
    validate_message(data, message, channel_id, token, u_id)
    messageId = randrange(9999)
    time = datetime.datetime.now
    for channel in data['channels']:
        while messageId in channel['messages']:
            messageId = randrange(99999)
    for channel in data['channels']:
        if channel['channel_id'] == channel_id:
            channel['messages'].append({
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
            'is_reacted': 0,
    })
    return messageId


#message_send_later(data, message, channel_id, time_send, token)
def message_send_later(data, message, channel_id, time_send, token):
    time_now = datetime.datetime.now()
    if time_send > time_now:
        raise ValueError("time send is in the past")
    
    u_id = getUserFromToken(token)
    validate_message(data, message, channel_id, token, u_id)
    messageId = randrange(9999)

    #Sleep
    timeUntilThen = time_send - time_now
    seconds = timeUntilThen.seconds
    time.sleep(seconds)
    for channel in data['channels']:
        while messageId in channel['messages']:
            messageId = randrange(99999)
    for channel in data['channels']:
        if channel['channel_id'] == channel_id:
            channel['messages'].append({
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
            'is_reacted': 0,
    })
    return messageId


# data['users'].append({
#         'email': email,
#         'password': hashPassword(password),
#         'name_first': nameFirst,
#         'name_last': nameLast,
#         'handle': handle, 
#         'u_id': u_id,
#         'resetCode': None,
#         'is_admin': PERMISSION3,
#     })
def isAdminOrOwner(data, u_id):
    val = False
    for user in data['users']:
        if user['u_id'] == str(u_id):
            if user['is_admin'] == 1:
                val = True
            if user['is_admin'] == 2:
                val = True
    return val

def validate_remove(data, token, messageId):
    if token in data['tokens']:
        pass
    else:
        raise ValueError("invalid token")
    channel_id = 0
    messagereal = False
    for channel in data['channels']:
        for message in channel['messages']:
            if message['message_id'] == messageId:
                channel_id = channel['channel_id']
                messagereal = True
    if messagereal == False:
         raise ValueError("cant find message")
    u_id = getUserFromToken(token)
    #userIsInChannel(data, channel_id, getUserFromToken(token))
    if isUserinChannelbool(data, channel_id, u_id) == False:
        raise AccessError("User is not in that channel 184msg helper")
    exists = False
    ownmessage = False
    #adminCalling = False
    adminCalling = isAdminOrOwner(data, u_id)
    for channel in data['channels']:
        for message in channel['messages']:
            if message['message_id'] == messageId:
                exists = True
                if message['u_id'] == u_id:
                    ownmessage = True
    if exists == False:
        raise ValueError("Invalid IDs")
    if ownmessage == False:
        if adminCalling == False:
            raise AccessError("Not an admin or owner or own message")
    

def isUserinChannelbool(data, cid, u_id):
    arethey = False
    for channel in data['channels']:
        if str(channel['channel_id']) == str(cid):
            for members in channel['members']:
                if str(members) == str(u_id):
                    arethey = True
    return arethey



def validate_message(data, message, channelid, token, u_id):
    exists = False
    for channel in data['channels']:
        if str(channel['channel_id']) == str(channelid):
            exists = True
    if exists == False:
        raise ValueError("bad channel Id")
    u_id = getUserFromToken(token)
    #userIsInChannel(data, channelid, u_id)
    if isUserinChannelbool(data, channelid, u_id) == False:
        raise AccessError("User is not in that channel 184msg helper")
    if len(message) > 1000:
        raise ValueError("ValueError when:Message is more than 1000 characters")
    
        
def validate_messageLater(data, message, channelid, token, timeSend, Realtime):
    if channelid in data['channels']:
        pass
    else:
        raise ValueError("invalid token")
    u_id = getUserFromToken(token)
    #userIsInChannel(data, channelid, u_id)
    if isUserinChannelbool(data, channelid, u_id) == False:
        raise AccessError("User is not in that channel 184msg helper")
    
    #value error: Time sent is a time in the past
    #Value Error time sent is in past
    if len(message) > 1000:
        raise ValueError("ValueError when:Message is more than 1000 characters")

def messageExists(data, messageId):
    valid = False
    for channel in data['channels']:
        for message in channel['messages']:
            if message['message_id'] == messageId:
                valid = True
    return valid

def isPinned(data, messageId):
    pinned = False
    for channels in data['channels']:
        for message in channels['messages']:
            if message['message_id'] == messageId:
                #print(message)
                if message['is_pinned'] == 1:
                    pinned = True
    return pinned

def pinMessage(data, token, messageId):
    if not messageExists(data, messageId):
        raise ValueError("That message does not exist")
    u_id = str(getUserFromToken(token))
    # Check whether user has the permission to pin
    #print("PINNN THISSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    useradmin = False
    #print(u_id)
    for user in data['users']:
        #print(user['u_id'])
        #print("compared to")
        #print(u_id)
        if str(user['u_id']) == str(u_id):
            #print("how'd we get in here lol")
            #print(user['is_admin'])
            if user['is_admin'] == 1:
                useradmin = True
                #print("you're a wizard harry")
            if user['is_admin'] == 2:
                useradmin = True 
    #print(useradmin)
    if useradmin == False:
        raise ValueError('user is not an admin')
    ipinned = isPinned(data, messageId)
    if ipinned == True:
        raise ValueError('That message is already pinned')
    #print(ipinned)
    #get the channels id
    for channel in data['channels']:
        for message in channel['messages']:
            if messageId == message['message_id']:
                cId = channel['channel_id']
                #userIsInChannel(data, cId, u_id)
                if isUserinChannelbool(data, cId, u_id) == False:
                    raise AccessError("User is not in that channel 184msg helper")
                #end of error checking
                message['is_pinned'] = 1

def unpinMessage(data, token, messageId):
    if not messageExists(data, messageId):
        raise ValueError("That message does not exist")
    u_id = getUserFromToken(token)
    # Check whether user has the permission to pin
    for channels in data['channels']:
        for message in channels['messages']:
            if message['message_id'] == messageId:
                cid = channels['channel_id']
    present = False
    for channels in data['channels']:
        #if channels['channel_id'] == cid:
            #print(channels['members'])
            #print("and we have")
            #print(u_id)
        for members in channels['members']:
            if members == str(u_id):
                #print("found him")
                present = True
            #print(members)
    if present == False:
        raise AccessError("user is not a part of that channel")
    for user in data['users']:
        if user['u_id'] == u_id:
            if user['is_admin'] == 3:
                raise ValueError('The authorised user is not an admin or owner')
    ispinned = isPinned(data, messageId)
    if ispinned == False:
        raise ValueError('That message is not yet pinned')
    #get the channels id
    for channel in data['channels']:
        for message in channel['messages']:
            if messageId == message['message_id']:
                cId = channel['channel_id']
                #userIsInChannel(data, cId, u_id)
                if isUserinChannelbool(data, cId, u_id) == False:
                    raise AccessError("User is not in that channel 184msg helper")
                #end of error checking
                message['is_pinned'] = 0
    


def reactToMessage(data, messageId, reactId, token):
    valid = False
    # channelId = "what the fuck"
    # for channel in data['channels']:
    #     for message in channel['messages']:
    #         if message['message_id'] == messageId:
    #             channelId = channel['channel_id']
    for channel in data['channels']:
        for message in channel['messages']:
            # print("comparing..")
            # print(messageId)
            # print(" ...and ... ")
            # print(message['message_id'])
            if messageId == message['message_id']:
                cId = channel['channel_id']
                valid = True
    if valid == False:
        raise ValueError("Didnt find message")
    u_id = getUserFromToken(token)
    #userIsInChannel(data, cId, u_id)
    if isUserinChannelbool(data, cId, u_id) == False:
        raise AccessError("User is not in that channel 184msg helper")

    #print("AFTER THE DUMB THING ===============================")
    #print(cId)
    if valid == False:
        raise ValueError("Invalid IDs")
    if reactId != 1:
        raise ValueError("invalid reactId")
    # reacted = False
    for channel in data['channels']:
        for message in channel['messages']:
            if message['message_id'] == messageId:
                if message['is_reacted'] == 1:
                    raise ValueError("Already reacted")
                message['is_reacted'] = 1

    # for channel in data['channels']:
    #     for message in channel['messages']:
    #         if message['message_id'] == messageId:
    #             for reacts in ['reacts']:
    #                 if reacts['react_id'] == reactId:
    #                     raise ValueError("Already reacted")
    #             message['reacts'].append({
    #                 'react_id': reactId,
    #                 'u_ids': u_id,
    #                 'is_this_user_reacted': 1,
    #             })

def unreactMessage(data, messageId, reactId, token):
    valid = False
    for channel in data['channels']:
        for message in channel['messages']:
            if messageId == message['message_id']:
                cId = channel['channel_id']
                valid = True
    if valid == False:
        raise ValueError("Didnt find message")
    u_id = getUserFromToken(token)
    #userIsInChannel(data, cId, u_id)
    if isUserinChannelbool(data, cId, u_id) == False:
        raise AccessError("User is not in that channel 184msg helper")
    if reactId != 1:
        raise ValueError("invalid reactId")
    # reacted = False
    for channel in data['channels']:
        for message in channel['messages']:
            if message['message_id'] == messageId:
                if message['is_reacted'] != reactId:
                    raise ValueError("does not have that react id")
                message['is_reacted'] = 0

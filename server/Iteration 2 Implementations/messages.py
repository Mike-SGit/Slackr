import datetime
import time



def editMessage(messageId, newMessage):
    for channel in data['channels']:
        for message in ['messages']:
            if message['message_id'] == messageId:
                message['message'] = newMessage



def remove_message(messageId):
    for channel in data['channels']:
        for message in ['messages']:
            if message['message_id'] == messageId:
                del message

    
    
#   'channels': [{
#         'messages': [{
#             'message_id': message_id,
#             'u_id': u_id,
#             'message': message,
#             'time_created': time, 
#             'reacts': [{
#                 'react_id': react_id, 
#                 'u_ids': u_id, 
#                 'is_this_user_reacted': is_this_user_reacted'
#                 }], 
#             'is_pinned': is_pinned, 
#         }]
#     }],





def message_send(token, channelid, message):
    data = getData()
    time_now = time.ctime(seconds)
    u_id = getUserFromToken(token)
    messageId = u_id+time_now
    data['channels']['messages'].append({
        'message_id': messageId,
        'u_id': u_id,
        'message': message,
        'time_created': time,
        'reacts': [{
            'react_id': 0,
            'u_id': u_id,
            'is_this_user_reacted': 0
        }],
        'is_pinned': 0,
    })




# def createM_ID():
#     data = getData()
# 	# Creating channel_id that resembles: C123456
# 	message_id = "M" + str(randrange(100000))
# 	for channels in data['channels']:
# 		while channel_id in channels['channel_id']:
# 			channel_id = "C" + str(randrange(100000))
# 	return channel_id


# sage': message,
#         'time_created': time,
#         'reacts': [{
#             'react_id': 0,
#             'u_id': u_id,
#             'is_this_user_reacted': 0
#         }],
#         'is_pinned': 0,
#     })




def validate_remove(token, messageId):
    data = getData()
    if token in data['tokens']:
        pass
    else:
        raise ValueError("invalid token")
    u_id = getUserFromToken(token)
    exists = False
    for channel in data['channels']:
        for message in ['messages']:
            if message['u_id'] == u_id:
                if message[message_id] == messageId:
                    exists = True
    if exists == False:
        raise ValueError("Invalid IDs")





def validate_message(message, channelid, token):
    getData()
    if channelid in data['channels']:
        pass
    else:
        raise ValueError("invalid token")
    u_id = getUserFromToken(token)
    userIsInChannel(data, channelid, u_id)
    if len(message) > 1000:
        raise ValueError("ValueError when:Message is more than 1000 characters")
    
        
def validate_messageLater(message, channelid, token, timeSend, Realtime):
    getData()
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


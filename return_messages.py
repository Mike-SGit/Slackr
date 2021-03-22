def returnMessages(messageArray, start):
    returnMessages = []
    for message in messageArray[start:start+50]:
        returnMessages.append({
            'message_id': message['message_id'],
            'u_id': message['u_id'],
            'time_created': message['time_created'],
            'reacts': message['reacts'],
            'is_pinned': message['is_pinned'],
        })
    return returnMessages
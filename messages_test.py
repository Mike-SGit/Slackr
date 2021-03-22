from messages_helper import message_send, validate_message, remove_message, editMessage, reactToMessage, unreactMessage, pinMessage, unpinMessage, isUserinChannelbool
from channels_helper import userIsInChannel
from errors import AccessError, ValueError
import pytest
#from test_data_user_profile import *

#SETUP
data = {
    'users': [],
    'channels': [],
    'tokens': [],
}

data['channels'].append({
    'is_public': '0', 
    'channel_id': 'C123456',
    'name': 'onamaewa',
    'channel_owners': {
        'original_owner': '57946', # A variable containing only one u_id, that being the owner's. 
        'owners': '57946', # A list of u_id's that correspond to channel owners, this includes the originalOwner.
    },
    'members': ['57946', '33530'],
    'standup_active' : False,
    'standup_end': 0,
    'standup_messages': [],
    'messages': [],
})


data['users'].append({
    'email': 'sherry@gmail.com',
    'password': 'sherry123',
    'name_first': 'Sherry',
    'name_last': 'Birkin',
    'handle': 'sherrybirkin', 
    'u_id': '57946',
    'is_admin': 1,
})

data['users'].append({
    'email': 'chris123@gmail.com',
    'password': 'chris123321',
    'name_first': 'Chris',
    'name_last': 'Birkin',
    'handle': 'chrisbirkin', 
    'u_id': '77935',
    'is_admin': 3,
})

data['users'].append({
    'email': 'handson@gmail.com',
    'password': 'hansen2123',
    'name_first': 'theman',
    'name_last': 'themith',
    'handle': 'thelegend', 
    'u_id': '33530',
    'is_admin': 3,
})

data['tokens'].append('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjo1Nzk0Nn0.InDtp3eE5c9VPsYLV3LzISlh6P7YTphz9utyqeKLKK0')
data['tokens'].append('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjo3NzkzNX0.Ei3Nco5HO3C43BvXNT428hllnl5d0ODJbN1aNDPuJ8I')
data['tokens'].append('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjozMzUzMH0.A9lgfHLFiqFMclX0AmubSpW8nBL6VXTE0CKELxPKQd0')

u_id = '57946'
u_id2 = '77935'
u_id3 = '33530'

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjo1Nzk0Nn0.InDtp3eE5c9VPsYLV3LzISlh6P7YTphz9utyqeKLKK0'
token2 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjo3NzkzNX0.Ei3Nco5HO3C43BvXNT428hllnl5d0ODJbN1aNDPuJ8I'
token3 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjozMzUzMH0.A9lgfHLFiqFMclX0AmubSpW8nBL6VXTE0CKELxPKQd0'


# TESTS
#def message_send(data, message, channelid, token):
def test_message_send():
    global data
    global token
    global token2
    a = message_send(data, "a short message", "C123456", token)
    print(data)
    print("===========================================================================")
    print(isUserinChannelbool(data, "33530", "C123456"))
    print("===========================================================================")

    # with pytest.raises(AccessError, match=r"*"):
    #     b = message_send(data, "a short message", "C123456", token2)
    # with pytest.raises(ValueError, match=r"*"):
    #     message_send(data, "a short asdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessageasdasdsasdasdadsdasdmessage", "C123456", "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoiVTY0NTY3In0.7S6sbsXK5U-_inS3L3gr-W2TURad9qEcpYS3nBWbMMA")
    # with pytest.raises(AccessError, match=r"*"):
    #     message_send(data, "a short message", "C123456", token2)
    # print(data)

#def remove_message(data, messageId, token):
def test_message_remove():
    global data
    global token
    global token2
    global token3
    a = message_send(data, "a short message", "C123456", token)
    b = message_send(data, "a short message", "C123456", token)
    c = message_send(data, "a short message", "C123456", token3)
    remove_message(data, a, token)
    with pytest.raises(ValueError, match=r"*"):
        remove_message(data, a, token)
    with pytest.raises(AccessError, match=r"*"):
        remove_message(data, b, token2)
    remove_message(data, c, token)
    


#def editMessage(data, messageId, newMessage, token):
def test_message_edit():
    global data
    global token
    global token2
    global token3
    sherrysmes = message_send(data, "a message to be edited", "C123456", token)
    sherrymessage = False
    for channels in data['channels']:
        for message in channels['messages']:
            if message['message_id'] == sherrysmes:
                sherrymessage = True
    assert (sherrymessage == True)
    hansonsmes = message_send(data, "hansons message to be edited", "C123456", token3)
    sherrysfinal = message_send(data, "sherrys final message to be edited", "C123456", token)
    editMessage(data, sherrysmes, "an edited message", token)
    editMessage(data, hansonsmes, "sherry was here", token)
    with pytest.raises(AccessError, match=r"*"):
        editMessage(data, sherrysfinal, "hanson was here", token3)

#def reactToMessage(data, messageId, reactId, token):
def test_react_message():
    global data
    global token
    global token2
    global token3
    unreactedmessage = message_send(data, "a mess to react to", "C123456", token)
    unreactedmessage2 = message_send(data, "a mess to react to", "C123456", token)
    # for channels in data['channels']:
    #     for message in channels['messages']:
    #         print(message)
    reactToMessage(data, unreactedmessage, 1, token)
    #print(data)
    with pytest.raises(ValueError, match=r"*"):
        reactToMessage(data, "a12313", 1, token)
    with pytest.raises(ValueError, match=r"*"):
        reactToMessage(data, unreactedmessage2, 2, token)
    with pytest.raises(ValueError, match=r"*"):
        reactToMessage(data, unreactedmessage, 1, token)   


def test_unreact_message():
    global data
    global token
    global token2
    global token3
    unreadtedmessage3 = message_send(data, "a mess to not IIIIIIIIIIIIIIIIIIIIIIIIII reacted to", "C123456", token)
    with pytest.raises(ValueError, match=r"*"):
        unreactMessage(data, unreadtedmessage3, 1, token)
    reactToMessage(data, unreadtedmessage3, 1, token)
    with pytest.raises(ValueError, match=r"*"):
        unreactMessage(data, unreadtedmessage3, 43, token)
    unreactMessage(data, unreadtedmessage3, 1, token)
    with pytest.raises(ValueError, match=r"*"):
        unreactMessage(data, 'memeid', 1, token)
    

#pinMessage(data, token, messageId)
def test_pin_message():
    unpinned = message_send(data, "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN", "C123456", token)
    unpinned1 = message_send(data, "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN", "C123456", token)
    #print(data['channels'][0])
    pinMessage(data, token, unpinned)
    #print(data['channels'][0])
    #print(data['users'])
    with pytest.raises(ValueError, match=r"*"):
        pinMessage(data, token, 'memeid')
    with pytest.raises(ValueError, match=r"*"):
        pinMessage(data, token3, unpinned1)
    with pytest.raises(ValueError, match=r"*"):
        pinMessage(data, token, unpinned)

# def test_unpin_message():
#     pinnit = message_send(data, "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN", "C123456", token)
#     pinMessage(data, token, pinnit)

def test_unpin_message():
    pinthis = message_send(data, "asds", "C123456", token)
    apinthis = message_send(data, "00000000000000000000000000000000000000000000000000000000", "C123456", token)
    pinMessage(data, token, apinthis)
    #print(data)
    unpinMessage(data, token, apinthis)
    #print(data)
    with pytest.raises(ValueError, match=r"*"):
        unpinMessage(data, token, 's23123')
    with pytest.raises(ValueError, match=r"*"):
        unpinMessage(data, token3, pinthis)
    #print(data)
    with pytest.raises(ValueError, match=r"*"):
        unpinMessage(data, token, apinthis)
    pinMessage(data, token, apinthis)
    # with pytest.raises(AccessError, match=r"*"):
    #     unpinMessage(data, token2, apinthis)
    



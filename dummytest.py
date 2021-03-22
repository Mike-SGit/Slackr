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
    #a = message_send(data, "a short message", "C123456", token)
    print(data)
    print("===========================================================================")
    print(isUserinChannelbool(data, "C123456", "331530"))
    print("===========================================================================")

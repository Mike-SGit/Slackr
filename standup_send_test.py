from standup_send import standupSendFunc
from invalidate_token import invalidateToken
from standup_start import standupStartFunc
from channels_create import channelsCreate
from channels_helper import joinChannel
from channels_helper import removeUserFromChannel
from standup_helper import standupNotActive

import pytest
import errors

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

# Value Error

def test_standup_send_channel_not_exist():
    # SETUP BEGIN    
    channel_id = "1234"
    # SETUP END
    
    # Channel does not exist
    with pytest.raises(errors.ValueError):
        standupSendFunc(data, token, channel_id, "Hello!!")

def test_standup_send_long_message():
    # SETUP BEGIN
    channel_id = "C123456" 
    # SETUP END
    
    with pytest.raises(errors.ValueError):
        standupSendFunc(data, token, channel_id, 'a'*1000)

# Access Error

def test_standup_send_not_member():
    # SETUP BEGIN
    channel_id = "C123456"  
    # SETUP END
    
    with pytest.raises(errors.AccessError):
        standupSendFunc(data, token2, channel_id, "Hello!")
    with pytest.raises(errors.AccessError):
        standupSendFunc(data, token2, channel_id, "I'm Chris")

def test_standup_send_invaild_token():
    # SETUP BEGIN
    invalidateToken(token, data['tokens'])
    channel_id = "C123456" 
    # SETUP END
    
    with pytest.raises(errors.ValueError):
        standupSendFunc(data, token, channel_id, "Hello!!")


def test_standup_send_correct():
    # SETUP BEGIN
    channel_id = "C123456" 
    standupStartFunc(data, token3, channel_id)
    # SETUP END
    
    standupSendFunc(data, token3, channel_id, "Hello!!")
    for channel in data['channels']:
        if str(channel_id == channel['channel_id']):
            print(channel['standup_message'])
    
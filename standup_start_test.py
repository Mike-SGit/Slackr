from invalidate_token import invalidateToken
from standup_start import standupStartFunc
from standup_helper import standupStillActive
from channels_create import channelsCreate
from channels_helper import joinChannel
from channels_helper import removeUserFromChannel
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

def test_standup_start_channel_not_exist():
    # SETUP BEGIN
    channel_id2 = "C123457"
    # SETUP END 

    # Channel does not exist
    with pytest.raises(errors.ValueError): 
        standupStartFunc(data, token, channel_id2)

# Access Error

def test_standup_start_not_member():
    # SETUP BEGIN
    channel_id = "C123456"  
    # SETUP END
    
    with pytest.raises(errors.AccessError):
        standupStartFunc(data, token2, channel_id)

def test_standup_start_invaild_token():
    # SETUP BEGIN
    channel_id = "C123456"
    invalidateToken(token2, data['tokens'])
    # SETUP END
    
    with pytest.raises(errors.AccessError):
        standupStartFunc(data, token2, channel_id)

def test_standup_start_correct():
    # SETUP BEGIN
    channel_id = "C123456"
    # SETUP END  

    standupStartFunc(data, token, channel_id)

    assert(standupStillActive (data, channel_id, token) is True)
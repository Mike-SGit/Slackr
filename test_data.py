# SETUP
data = {
    'users': [],
    'channels': [],
    'tokens': [],
}

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

######################################################################
######################################################################

# data['channels'][0]
data['channels'].append({
    'is_public': '0', 
    'channel_id': 'C123456',
    'name': 'onamaewa',
    'channel_owners': {
        'original_owner': '57946', # A variable containing only one u_id, that being the owner's. 
        'owners': '57946', # A list of u_id's that correspond to channel owners, this includes the originalOwner.
    },
    'members': ['57946', '77935'],
    'standup_active': False,
    'standup_end': 0,
    'standup_messages': [],
    'messages': [],
})

# data['channels'][0]['messages'][0]
data['channels'][0]['messages'].append({
    'message_id': 'M0001',
    'u_id': '57946',
    'message': 'Hello my name is Sherry!',
    'time_created': None,
    'reacts': [{
        'react_id': 0,
        'u_id': None,
        'is_this_user_reacted': 0,
    }],
    'is_pinned': 0,
})

# data['channels'][0]['messages'][1]
data['channels'][0]['messages'].append({
    'message_id': 'M0002',
    'u_id': '77935',
    'message': 'Hello my name is Chris!',
    'time_created': None,
    'reacts': [{
        'react_id': 0,
        'u_id': None,
        'is_this_user_reacted': 0,
    }],
    'is_pinned': 0,
})

# data['channels'][0]['messages'][2]
data['channels'][0]['messages'].append({
    'message_id': 'M0001',
    'u_id': '57946',
    'message': 'I love u',
    'time_created': None,
    'reacts': [{
        'react_id': 0,
        'u_id': None,
        'is_this_user_reacted': 0,
    }],
    'is_pinned': 0,
})

######################################################################
######################################################################

# data['channels'][1]
data['channels'].append({
    'is_public': '0', 
    'channel_id': 'C123457',
    'name': 'onamaewa',
    'channel_owners': {
        'original_owner': '77935',
        'owners': '77935',
    },
    'members': ['57946', '77935'],
    'standup_active': False,
    'standup_end': 0,
    'standup_messages': [],
    'messages': [],
})

# data['channels'][1]['messages'][0]
data['channels'][0]['messages'].append({
    'message_id': 'M0001',
    'u_id': '57946',
    'message': 'Hello again Im Sherry!',
    'time_created': None,
    'reacts': [{
        'react_id': 0,
        'u_id': None,
        'is_this_user_reacted': 0,
    }],
    'is_pinned': 0,
})

######################################################################
######################################################################

u_id = '57946'
u_id2 = '77935'

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjo1Nzk0Nn0.InDtp3eE5c9VPsYLV3LzISlh6P7YTphz9utyqeKLKK0'
token2 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjo3NzkzNX0.Ei3Nco5HO3C43BvXNT428hllnl5d0ODJbN1aNDPuJ8I'

data['tokens'].append('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjo1Nzk0Nn0.InDtp3eE5c9VPsYLV3LzISlh6P7YTphz9utyqeKLKK0')
data['tokens'].append('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjo3NzkzNX0.Ei3Nco5HO3C43BvXNT428hllnl5d0ODJbN1aNDPuJ8I')


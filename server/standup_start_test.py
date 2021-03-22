from standup_start import standup_start
import channels_create
import pytest

data = {
    'users': []
}

data['users'].append({
    'email': 'sherry@gmail.com',
    'password': 'sherry123',
    'name_first': 'Sherry',
    'name_last': 'Birkin',
    'handle': 'sherrybirkin', 
    'u_id': 'U64567',
    'is_admin': 1,
})

data['users'].append({
    'email': 'chris123@gmail.com',
    'password': 'chris123321',
    'name_first': 'Chris',
    'name_last': 'Birkin',
    'handle': 'chrisbirkin', 
    'u_id': 'U7049',
    'is_admin': 3,
})
u_id = 'U64567'
u_id2 = 'U7049'

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoiVTY0NTY3In0.7S6sbsXK5U-_inS3L3gr-W2TURad9qEcpYS3nBWbMMA'
token2 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoiVTcwNDkifQ.mGjYa4Pb2tpw9LbwAqE2m6y7MhXcpBtq8H-d6xwkbQ8'


def test_standup_start_correct():
    # SETUP BEGIN

    channel = channels_create(data, token, "Private_Channel", True)
    channel_id = channel['channel_id']
    # SETUP END
    
    standup_start(data, token, channel_id)

# Value Error
###
def test_standup_start_channel_not_exist():
    # SETUP BEGIN
    
    channel_id = "1234"
    # SETUP END
    
    # Channel does not exist
    with pytest.raises(ValueError, match=r"*"):
        standup_start(data, token, channel_id)

# Access Error

def test_standup_start_not_member():
    # SETUP BEGIN

    channel = channels_create(token, "Private_Channel", True)
    channel_id = channel['channel_id']
    
    # SETUP END
    
    with pytest.raises(AccessError , match=r"*"):
        standup_start(data, token2, channel_id)
    with pytest.raises(AccessError , match=r"*"):
        standup_start(data, token2, channel_id)

def test_standup_start_invaild_token():
    # SETUP BEGIN
    invaildToken = "abcde"
    # SETUP END
    
    with pytest.raises(ValueError, match=r"*"):
        standup_start(data, invalidToken, channel_id)

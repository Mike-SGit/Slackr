from messages import message_send
from errors import AccessError, ValueError
import pytest

# SETUP
data = {
    'users': [],
    'channels': [],
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

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoiVTY0NTY3In0.7S6sbsXK5U-_inS3L3gr-W2TURad9qEcpYS3nBWbMMA'
token2 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoiVTcwNDkifQ.mGjYa4Pb2tpw9LbwAqE2m6y7MhXcpBtq8H-d6xwkbQ8'

data['channels'].append({
    'is_public': True, 
    'channel_id': 'C120001',
    'name': 'my_channel',
    'channel_owners': {
		'original_owner': 'U64567',
		'owners': ['U64567'],
    },
    'members': ['U64567'],
    'messages': [{
		'message_id': 'U64567M0001',
		'u_id': 'U64567',
		'message': 'Hi Im Sherry!',
		'time_created': 'time',
		'reacts': [{
			'react_id': 0,
			'u_ids': 'U64567',
		}],
	'is_pinned': 'is_pinned',
	}]
})




# TESTS
def test_message_send_toPublic():
	message_send(token, 'C120001', 'Hello')

def test_message_send_toPublicFAILFakeToken():
    with pytest.raises(AccessError, match=r"*"):
        message_send('fakeToken', 'C120001', 'Hello')

def test_message_send_toPublicFAILmessageLength():
    with pytest.raises(AccessError, match=r"*"):
        message_send(token, 'C120001', "hello publicccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc")

def test_message_send_not_in_channel():
	message_send(token2, 'C120001', 'Hello')

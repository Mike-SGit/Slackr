from Error import AccessError
from Channel_removeowner import is_owner
import pytest
import Channels_create

def test_Channel_removeowner():
    #setup
    user1 = auth_register("dummy@gmail.com", "pass", "userfirst", "userlast")
    user1_token = user1['token']

    user2 = auth_register("dummy2@gmail.com", "pass", "user2first", "user2last")
    user2_token = user2['token']

    user3 = auth_register("dummy3@gmail.com", "pass", "user3first", "user3last")
    user3_token = user3['token']

    user4 = auth_register("dummy4@gmail.com", "pass", "user4first", "user4last")
    user4_token = user4['token']

    channel_id = channels_create (user2_token, 'test', False)
    #end setup

    #standard remove owner procedure
    channel_addowner (user2_token, channel_id, user4['u_id'])
    channel_removeowner (user2_token, channel_id, user4['u_id'] 
    assert is_owner (user4['u_id'], channel_id) == False

    #invalid channel id
    with pytest.raises(ValueError, match = r"*"):
        channel_addowner (user2_token, 'invalid channel_id', user1['u_id'])

    #user is not owner
    with pytest.raises(AccessError, match =r"*"):
        channel_addowner (user3_token, channel_id, user1['u_id'])

    #target user is already not an owner
    with pytest.raises (ValueError, match = r"*"):
        channel_removeowner (user2_token, channel_id, user1['u_id'])
    pass

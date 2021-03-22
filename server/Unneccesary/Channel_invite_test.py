from auth_register import auth_register
import Channels_create
import pytest

def Channel_invite_test ():
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

    #expected invite procedure
    Channel_invite (user2_token, channel_id, user1['u_id'])
    assert in_channel (user1_token, channel_id) == True

    #invalid channel id
    with pytest.raises(ValueError, match = r"*"):
        Channel_invite (user2_token, 'invalid channel id', user3['u_id'])

    #user is not in channel 
    with pytest.raises(ValueError, match = r"*"):
        Channel_invite (user4_token, channel_id, user3['u_id'])

    #inviting a user with an invalid u_id
    with pytest.raises(ValueError, match = r"*"):
        Channel_invite (user4_token, channel_id, 'invalid u_id')
    
    #user to be invited is already in channel
    with pytest.raises(ValueError, match = r"*"):
        Channel_invite (user2_token, channel_id, user1['u_id'])


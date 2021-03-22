import Channel_leave
import Channels_create
import Channel_join
from auth_register import auth_register
import pytest

def test_channel_join():
    # Begin setup
    auth_user1_dict = auth_register("random@gmail.com", "user1", "random", "rand")
    user1_token = auth_user1['token']

    auth_user2_dict = auth_register ("random2@gmail.com", "user2", "random2", "rand2")
    user2_token = auth_user2['token']

    channel_id = channels_create (user2_token, 'test', True)
    # End setup

    #standard join procedure
    channel_join (user1_token, channel_id)
    assert channel_id in channels_list (user1_token)

    #user is already in channel
    with pytest.raises(ValueError, match=r"*"):
        channel_join (user1_token, channel_id)

    #invalid channel id
    user3_token = 'invalid token'
    with pytest.raises(ValueError, match = r"*"):
        channel_join (user2_token, 'invalid channel id')    

    #attempting to join private channel
    channel_id2 = channels_create (user2_token, 'test2', False)
    with pytest.raises(ValueError, match = r"*"):
        channel_join (user1_token, channel_id2) 

    #invalid token
    with pytest.raises(ValueError, match = r"*"):
        channel_join ('invalid token', channel_id)   
    pass

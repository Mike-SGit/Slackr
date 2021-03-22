import Channel_leave
import Channel_join
from auth_register import auth_register
import pytest
import Channels_create

def test_channel_create():
    # Begin setup
    auth_user1_dict = auth_register("random@gmail.com", "user1", "random", "rand")
    user1_token = auth_user1['token']

    auth_user2_dict = auth_register ("random2@gmail.com", "user2", "random2", "rand2")
    user2_token = auth_user2['token']
    # End setup

    #standard create procedure
    channel_join (user1_token, channel_id)
    assert channel_id in channels_list (user1_token)
   
    #invalid token
    user3_token = 'invalid token'
    with pytest.raises(ValueError, match = r"*"):
        channel_create ('invalid token', 'name', True)
    
    #name too long
    with pytest.raises(ValueError, match = r"*"):
        channel_create (user1_token, 123456789123456789123, True)
        
    #attempting to join new private channel
    channel_id2 = channels_create (user2_token, 'test2', False)
    channel_join (user1_token, channel_id2) 
    assert channel_id not in channels_list (user1_token)

    #attempting to join new public channel
    channel_id3 = channels_create (user2_token, 'test3', True)
    channel_join (user1_token, channel_id3) 
    assert channel_id in channels_list (user1_token)
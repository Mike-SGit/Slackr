import Channel_leave
import Channels_create
import Channel_join
from auth_register import auth_register
import pytest

def channel_leave_test():
    # Begin setup
    auth_user1_dict = auth_register("random@gmail.com", "user1", "random", "rand")
    user1_token = auth_user1['token']

    auth_user2_dict = auth_register ("random2@gmail.com", "user2", "random2", "rand2")
    user2_token = auth_user2['token']

    channel_id = channels_create (user2_token, 'test', True)
    channel_join (user1_token, channel_id)
    # End setup

    #standard leave procedure
    channel_leave (user1_token, channel_id)
    assert channel_id not in channels_list (user1_token)

    #user is not in channel
    with pytest.raises(ValueError, match=r"*"):
        channel_leave (user1_token, channel_id)

    #invalid channel id
    user3_token = 'invalid token'
    with pytest.raises(ValueError, match = r"*"):
        channel_leave (user2_token, 'invalid channel id')    
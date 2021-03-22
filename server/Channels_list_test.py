from auth_register import auth_register
import Channels_create
import pytest

def test_Channels_list():
    #setup
    user = auth_register("dummy@gmail.com", "pass", "userfirst", "userlast")
    user_token = user1['token']

    channel_id = channels_create (user_token, 'test', False)
    channel_id2 = channels_create (user_token, 'test2', False)
    #end setup

    #invalid token call
    with pytest.raises (ValueError, match =r"*"):
        channels_list ('invalid token')

    #standard channel list call
    assert channels_list(user_token) == {'test','test2'}

    pass
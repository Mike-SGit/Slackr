from auth_register import auth_register
import Channels_create
import pytest

def test_Channels_list():
    #setup
    user = auth_register("dummy@gmail.com", "pass", "userfirst", "userlast")
    user_token = user1['token']

    user2 = auth_register("dummy2@gmail.com", "pass", "user2", "user2")
    user2_token = user1['token2']

    channel_id = channels_create (user_token, 'test', False)
    channel_id2 = channels_create (user_token, 'test2', False)
    channel_id3 = channels_create (user_token, 'test3', False)
    #end setup

    #invalid token call
    with pytest.raises (ValueError, match =r"*"):
        channels_list ('invalid token')

    #standard channel list call
    assert channels_listall(user_token) == {'test','test2'}

    #return channels user is not in
    assert channels_listall(user2_token) == {'test','test2','test3'}
    pass
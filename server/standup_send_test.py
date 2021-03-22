from standup_send import standup_send
from auth_register import auth_register
from channels_create import channels_create
import pytest

def test_standup_send_correct():
    # SETUP BEGIN
    authRegDict = auth_register("sherry@gmail.com", "Abcd1234", "Sherry", "Birkin")
    token = authRegDict['token']
    channel = channels_create(token, "Private_Channel", True)
    channel_id = channel['channel_id']
    # SETUP END
    
    standup_send(token, channel_id, "Hello!!")
    standup_send(token, channel_id, "Just created a channel")
    
# Value Error

def test_standup_send_channel_not_exist():
    # SETUP BEGIN
    authRegDict = auth_register("sherry@gmail.com", "Abcd1234", "Sherry", "Birkin")
    token = authRegDict['token']
    
    channel_id = "1234"
    # SETUP END
    
    # Channel does not exist
    with pytest.raises(ValueError, match=r"*"):
        standup_send(token, channel_id, "Hello!!")

def test_standup_send_long_message():
    # SETUP BEGIN
    authRegDict = auth_register("sherry@gmail.com", "Abcd1234", "Sherry", "Birkin")
    token = authRegDict['token']
    channel = channels_create(token, "Private_Channel", True)
    channel_id = channel['channel_id']
    # SETUP END
    
    with pytest.raises(ValueError, match=r"*"):
        standup_send(token, channel_id, "Hellooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo!!")

# Access Error

def test_standup_send_not_member():
    # SETUP BEGIN
    authRegDict = auth_register("sherry@gmail.com", "Abcd1234", "Sherry", "Birkin")
    token = authRegDict['token']
    channel = channels_create(token, "Private_Channel", True)
    channel_id = channel['channel_id']
    
    authRegDict2 = auth_register("chris@gmail.com", "Abcd1234", "Chris", "Smith")
    token2 = authRegDict2['token']
    # SETUP END
    
    with pytest.raises(AccessError , match=r"*"):
        standup_send(token2, channel_id, "Hello")
    with pytest.raises(AccessError , match=r"*"):
        standup_send(token2, channel_id, "I'm Chris")

def test_standup_send_invaild_token():
    # SETUP BEGIN
    invaildToken = "abcde"
    channel_id = "1234"
    # SETUP END
    
    with pytest.raises(ValueError, match=r"*"):
        standup_send(invaildToken, channel_id, "Hello!!")
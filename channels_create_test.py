import pytest
import errors

from channels_helper import channelNameCheck
from channels_create import channelsCreate 
from hash_password import hashPassword

def test_valid_channel_create():

    '''
    Testing if channel_create functions return expected outputs 
    if passed correct name, u_id and is_public.
    '''

    data = {
        "users": [{
            "email": "valid@email.com", 
            "password": hashPassword("validPassword"), 
            "name_first": "validFirst", 
            "name_last": "validLast", 
            "handle": "validFirstvalidLast", 
            "u_id": 1234, 
            "resetCode": None, 
            "is_admin": 1, 
            "img_url": None}],
        "tokens": ["validToken"], 
        "channels": [],
        }

    assert channelNameCheck("validChannelName") is True
    assert channelsCreate(data, 1234, "validChannelName", True) == data['channels'][0]['channel_id']

def test_invalid_channel_name_create():

    '''
    Testing if channel_create functions return expected outputs 
    if passed an incorrect name, u_id and is_public.
    '''

    with pytest.raises(errors.ValueError): 
        channelNameCheck("invalidChannelNameTooLong") 

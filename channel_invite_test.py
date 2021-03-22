import pytest
import errors

from channels_helper import userIsInChannel, addUserToChannel
from auth_register_helper import validUser
from hash_password import hashPassword

def test_valid_channel_invite():

    '''
    Testing if channel_invite functions return expected outputs 
    if passed correct u_id and channel_id.
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
        "channels": [{
            "channel_id": 5000,
            "members": [1234],
        }],
        }

    assert userIsInChannel(data, 5000, 1234)
    assert validUser(data, 1234)
    
    with pytest.raises(errors.ValueError):
        addUserToChannel(data, 5000, 1234)
    
def test_invalid_channel_invite():

    '''
    Testing if channel_invite functions return expected outputs 
    if an incorrect u_id and channel_id.
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
            "img_url": None},
            {"u_id": 5678}],
        "tokens": ["validToken"], 
        "channels": [{
            "channel_id": 5000,
            "members": [1234],
        }],
        }

    with pytest.raises(errors.AccessError):
        userIsInChannel(data, 5000, 5678)

def test_invalid_channel_invite_already_member():

    '''
    Testing if channel_invite functions return expected outputs 
    if passed correct u_id that is already in the channel.
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
            "img_url": None},
            {"u_id": 5678}],
        "tokens": ["validToken"], 
        "channels": [{
            "channel_id": 5000,
            "members": [1234],
        }],
        }

    with pytest.raises(errors.ValueError):
        addUserToChannel(data, 5000, 1234)




    

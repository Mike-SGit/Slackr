import pytest
import errors

from channels_helper import removeUserFromChannel
from hash_password import hashPassword

def test_valid_channel_remove():

    '''
    Testing if channel_leave functions return expected outputs 
    if passed correct channel_id and u_id.
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
            "name": "validChannelName",
            "owners": [1234],
            "members": [1234, 5678],
        }],
        }

    assert removeUserFromChannel(data, 5000, 5678) 

def test_invalid_channel_remove():

    '''
    Testing if channel_leave functions return expected outputs 
    if passed correct channel_id and incorrect u_id.
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
            "name": "validChannelName",
            "owners": [1234],
            "members": [1234],
        }],
        }

    with pytest.raises(errors.ValueError): 
        removeUserFromChannel(data, 5000, 5678) 

def test_invalid_channel_remove_user_not_member():

    '''
    Testing if channel_leave functions return expected outputs 
    if passed an valid channel_id and incorrect u_id.
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
            "name": "validChannelName",
            "owners": [1234],
            "members": [1234],
        }],
        }

    with pytest.raises(errors.ValueError): 
        removeUserFromChannel(data, 5000, 5678) 
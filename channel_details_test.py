import pytest
import errors

from channel_details import getDetails
from hash_password import hashPassword

def test_valid_channel_details():

    '''
    Testing if channel_details functions return expected outputs 
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
        "channels": [{
            "channel_id": 5000,
            "name": "validChannelName",
            "owners": [1234],
            "members": [1234],
        }],
        }

    channelReturn = getDetails(data, 5000)
    assert channelReturn['name'] == data['channels'][0]['name']
    assert channelReturn['owner_members'] == data['channels'][0]['owners']
    assert channelReturn['all_members'] == data['channels'][0]['members']

    
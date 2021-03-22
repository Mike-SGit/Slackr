import pytest

class AccessError(Exception):
    pass

def channel_details (token, channel_id):
    pass

def test_valid_channel_details ():
    
    '''
    Testing if auth_logout correctly returns a list containing channel details
    (name, owner_members, all_members) if passed a valid token and channel id.
    '''

    # BEGIN SET UP
    validToken = "validToken"
    validChannel = "validChannel"
    name = "name"
    owner_members = ["ownerMembers"]
    all_members = ["allMembers"]
    # END SET UP

    assert channel_details (validToken, validChannel) \
        == {name, owner_members, all_members}

def test_invalidchannel_channel_details ():
    
    '''
    Testing if auth_logout correctly raises a ValueError if
    passed an invalid channel id and valid token.
    '''

    # BEGIN SET UP
    validToken = "validToken"
    invalidChannel = "validChannel"
    # END SET UP

    with pytest.raises(ValueError):
        channel_details (validToken, invalidChannel)

def test_invalid_member_channel_details ():
    
    '''
    Testing if auth_logout correctly raises an AccessError if
    passed an invalid token and (in)valid channel id.
    '''

    # BEGIN SET UP
    invalidToken = "invalidToken"
    validChannel = "validChannel"
    # END SET UP

    with pytest.raises(AccessError):
        channel_details (invalidToken, validChannel)
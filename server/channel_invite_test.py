import pytest

validToken = "validToken"
invalidToken = "invalidToken"
validChannel = "validChannel"
invalidChannel = "invalidChannel"
validID = "validID"
invalidID = "invalidID"

def channel_invite (token, channel_id, u_id):
    pass

def test_return_valid_channel_invite():
    
    '''
    Testing if auth_logout correctly returns None if passed a valid
    token, channel_id and u_id.
    '''

    assert channel_invite (validToken, validChannel, validID) == None

def test_invalidchannel_channel_invite():
    
    '''
    Testing if auth_logout correctly raises a ValueError if passed an invalid
    channel_id and (in)valid token and u_id.
    '''

    with pytest.raises(ValueError):
        channel_invite (validToken, invalidChannel, validID)

    with pytest.raises(ValueError):
        channel_invite (invalidToken, invalidChannel, validID)
    
    with pytest.raises(ValueError):
        channel_invite (validToken, invalidChannel, invalidID)

def test_invalid_token_channel_invite():
    
    '''
    Testing if auth_logout correctly raises a ValueError if passed an invalid
    token and (in)valid channel and u_id.
    '''

    with pytest.raises(ValueError):
        channel_invite (invalidToken, validChannel, validID)

    with pytest.raises(ValueError):
        channel_invite (invalidToken, invalidChannel, validID)
    
    with pytest.raises(ValueError):
        channel_invite (invalidToken, validChannel, invalidID)

def test_invalid_ID_channel_invite():
    
    '''
    Testing if auth_logout correctly raises a ValueError if passed an invalid
    u_id and (in)valid channel and token.
    '''

    with pytest.raises(ValueError):
        channel_invite (validToken, validChannel, invalidID)

    with pytest.raises(ValueError):
        channel_invite (invalidToken, validChannel, invalidID)
    
    with pytest.raises(ValueError):
        channel_invite (validToken, invalidChannel, invalidID)


import pytest

class AccessError(Exception):
    pass

def channel_messages (token, channel_id, start):
    pass

def test_reached_end_channel_messages ():
    
    '''
    Testing if 'channel_messages', when passed a valid channel id, correctly 
    returns up to 50 messages between 'start' and 'start + 50' 
    and a new index 'end' = '-1' since it would have returned the least recent message.
    '''

    # BEGIN SET UP
    validToken = "validToken"
    validChannel = "validChannel"
    validStart = 0
    end = -1
    messages = ["Hello", "Goodbye"]
    # END SET UP

    assert channel_messages (validToken, validChannel, validStart) \
        == {messages, validStart, end}

def test_valid_channel_messages ():
    
    '''
    Testing if 'channel_messages', when passed a valid channel id, correctly 
    returns up to 50 messages between 'start' and 'start + 50' 
    and a new index 'end' = 'start + 50'.
    '''

    # BEGIN SET UP
    validToken = "validToken"
    validChannel = "validChannel"
    validStart = 0
    end = validStart + 50
    messages = []
    for i in range (0, 50):
        messages[i] = i += 1
    # END SET UP

    assert channel_messages (validToken, validChannel, validStart) \
        == {messages, validStart, end}

def test_invalid_channel_messages ():

    ''' 
    Testing if 'channel_messages', when passed an invalid channel id, 
    correctly raises a ValueError.
    '''

    # BEGIN SET UP
    validToken = "validToken"
    invalidChannel = "validChannel"
    validStart = 0
    # END SET UP

    with pytest.raises(ValueError):
        channel_messages (validToken, invalidChannel, validStart)

def test_invalid_start_channel_messages ():

    ''' 
    Testing if 'channel_messages', when passed an invalid start, 
    correctly raises a ValueError.
    '''

    # BEGIN SET UP
    validToken = "validToken"
    validChannel = "validChannel"
    invalidStart = 50
    messages = ["Hello"]
    # END SET UP

    with pytest.raises(ValueError):
        channel_messages (validToken, validChannel, invalidStart)

    with pytest.raises(ValueError):
        invalidStart = -1
        channel_messages (validToken, validChannel, invalidStart)

def test_invalid_token_channel_messages ():

    ''' 
    Testing if 'channel_messages', when passed an invalid token, 
    correctly raises an AccessError.
    '''

    # BEGIN SET UP
    invalidToken = "invalidToken"
    validChannel = "validChannel"
    validStart = 0
    # END SET UP

    with pytest.raises(AccessError):
        channel_messages (invalidToken, validChannel, validStart)

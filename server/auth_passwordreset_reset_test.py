import pytest

def auth_passwordreset_reset(reset_code, new_password):
    pass

def test_valid_return_auth_passwordreset_reset():
    
    '''
    Testing if auth_passwordreset_reset correctly returns None if 
    passed a valid reset code and valid password.
    '''

    # BEGIN SET UP
    validCode = "validCode"
    validPassword = "validPassword"
    # END SET UP

    assert auth_passwordreset_reset (validCode, validPassword) == None

def test_invalid_code_auth_passwordreset_reset():
    
    '''
    Testing if auth_passwordreset_reset correctly raises a ValueError if 
    passed an invalid reset code and (in)valid password.
    '''

    # BEGIN SET UP
    invalidCode = "validCode"
    validPassword = "validPassword"
    invalidPassword = "validPassword"
    # END SET UP

    with pytest.raises(ValueError):
        auth_passwordreset_reset (invalidCode, validPassword)

    with pytest.raises(ValueError):
        auth_passwordreset_reset (invalidCode, invalidPassword)

def test_invalid_password_auth_passwordreset_reset():
    
    '''
    Testing if auth_passwordreset_reset correctly raises a ValueError if 
    passed an invalid password and (in)valid reset code.
    '''

    # BEGIN SET UP
    validCode = "validCode"
    invalidCode = "validCode"
    invalidPassword = "validPassword"
    # END SET UP

    with pytest.raises(ValueError):
        auth_passwordreset_reset (validCode, invalidPassword)

    with pytest.raises(ValueError):
        auth_passwordreset_reset (invalidCode, invalidPassword)

def test_valid_auth_passwordreset_reset():
    
    '''
    Testing if auth_passwordreset_reset correctly returns None if 
    passed a valid reset code and valid password.
    '''

    # BEGIN SET UP
    currentPassword = "currentPassword"
    validCode = "validCode"
    validPassword = "validPassword"
    # END SET UP

    auth_passwordreset_reset (validCode, validPassword)
    assert currentPassword == validPassword
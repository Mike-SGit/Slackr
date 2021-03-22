import pytest

def test_valid_auth_login ():

    '''
    Testing if auth_login correctly returns a valid user id and valid token when 
    passed a valid email and valid password.
    '''
    
    # BEGIN SET UP
    validEmail = "valid@email.com"
    validPassword = "validPassword"
    # END SET UP

    assert auth_login (validEmail, validPassword) == {"valid u_id", "validToken"}

def test_invalid_email_auth_login ():

    '''
    Testing if auth_login correctly raises a ValueError when the email 
    entered is invalid despite the password being valid (or invalid).
    '''

    # BEGIN SET UP
    invalidEmail = "invalid@email.com"
    validPassword = "validPassword"
    invalidPassword = "invalidPassword"
    # END SET UP

    with pytest.raises(ValueError):
        auth_login (invalidEmail, validPassword)

    with pytest.raises(ValueError):
        auth_login (invalidEmail, invalidPassword)

def test_email_dne_auth_login ():

    '''
    Testing if auth_login correctly raises a ValueError when the email 
    entered does not belong to a user (i.e. does not exist, dne), despite the
    password being valid (or invalid).
    '''

    # BEGIN SET UP
    dneEmail = "dne@email.com"
    validPassword = "validPassword"
    invalidPassword = "invalidPassword"
    # END SET UP

    with pytest.raises(ValueError):
        auth_login (dneEmail, validPassword)

    with pytest.raises(ValueError):
        auth_login (dneEmail, invalidPassword)

def test_invalid_password_auth_login ():

    '''
    Testing if auth_login correctly raises a ValueError when the password 
    entered is invalid despite the email being valid (or invalid).
    '''

    # BEGIN SET UP
    validEmail = "valid@email.com"
    invalidEmail = "invalid@email.com"
    invalidPassword = "invalidPassword"
    # END SET UP

    with pytest.raises(ValueError):
        auth_login (validEmail, invalidPassword)

    with pytest.raises(ValueError):
        auth_login (invalidEmail, invalidPassword)
import pytest

createHandle
createU_ID
emailExists
uniqueHandle
checkEmail
checkPassword
checkName
createUser

email, password, nameFirst, nameLast

def test_valid_auth_register ():

    '''
    Testing if auth_register returns a new valid token and valid user id
    if passed a valid email, first name, last name and password.
    '''

    assert auth_register (validEmail, validPassword, validFirst, validLast) \
        == {"valid u_id", "validToken"}

def test_invalid_email_auth_register ():

    '''
    Testing if auth_register raises a ValueError
    if passed an invalid email and (in)valid first name, last name and password.
    '''

    with pytest.raises(ValueError): 
        auth_register (invalidEmail, validPassword, validFirst, validLast)
        
    with pytest.raises(ValueError): 
        auth_register (invalidEmail, invalidPassword, validFirst, validLast)
        
    with pytest.raises(ValueError): 
        auth_register (invalidEmail, validPassword, invalidFirst, validLast)
        
    with pytest.raises(ValueError): 
        auth_register (invalidEmail, validPassword, validFirst, invalidLast)

def test_taken_email_auth_register ():

    '''
    Testing if auth_register raises a ValueError
    if passed an email which has been taken by another user
    regardless of also being passed an (in)valid password, first name or last name.
    '''

    # BEGIN SET UP
    takenEmail = "taken@email.com"
    # END SET UP

    with pytest.raises(ValueError):
        auth_register (takenEmail, validPassword, validFirst, validLast)

    with pytest.raises(ValueError): 
        auth_register (takenEmail, invalidPassword, validFirst, validLast)
        
    with pytest.raises(ValueError): 
        auth_register (takenEmail, validPassword, invalidFirst, validLast)
        
    with pytest.raises(ValueError): 
        auth_register (takenEmail, validPassword, validFirst, invalidLast)

def test_invalid_password_auth_register ():

    '''
    Testing if auth_register raises a ValueError
    if passed an invalid password and (in)valid email, first name and last name.
    '''

    with pytest.raises(ValueError): 
        auth_register (validEmail, invalidPassword, validFirst, validLast)
        
    with pytest.raises(ValueError): 
        auth_register (invalidEmail, invalidPassword, validFirst, validLast)
        
    with pytest.raises(ValueError): 
        auth_register (validEmail, invalidPassword, invalidFirst, validLast)
        
    with pytest.raises(ValueError): 
        auth_register (validEmail, invalidPassword, validFirst, invalidLast)

def test_invalid_first_auth_register ():

    '''
    Testing if auth_register raises a ValueError
    if passed an invalid first name (i.e. > 50 characters) and (in)valid email,
    last name and password.
    '''

    with pytest.raises(ValueError):
        auth_register (validEmail, validPassword, invalidFirst, validLast)

    with pytest.raises(ValueError):
        auth_register (invalidEmail, validPassword, invalidFirst, validLast)

    with pytest.raises(ValueError):
        auth_register (validEmail, invalidPassword, invalidFirst, validLast)

    with pytest.raises(ValueError):
        auth_register (validEmail, validPassword, invalidFirst, invalidLast)

def test_invalid_last_auth_register ():

    '''
    Testing if auth_register raises a ValueError
    if passed an invalid last name (i.e. > 50 characters) and (in)valid email,
    first name and password.
    '''

    with pytest.raises(ValueError):
        auth_register (validEmail, validPassword, validFirst, invalidLast)

    with pytest.raises(ValueError):
        auth_register (invalidEmail, validPassword, validFirst, invalidLast)

    with pytest.raises(ValueError):
        auth_register (validEmail, invalidPassword, validFirst, invalidLast)

    with pytest.raises(ValueError):
        auth_register (validEmail, validPassword, invalidFirst, invalidLast)

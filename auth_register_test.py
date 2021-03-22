import pytest

import errors
from auth_register_helper import createHandle, createU_ID, emailExists, uniqueHandle, checkEmail, checkPassword, checkName, createUser

def test_valid_auth_register():

    '''
    Testing if auth_register functions return expected outputs 
    if passed a valid email, first name, last name and password for the very first user.
    '''

    data = {
        'users': [],
        'tokens': [],
        'channels': [],
    }

    email, nameFirst, nameLast = 'valid@email.com', 'validFirst', 'validLast' 

    newHandle = createHandle(nameFirst, nameLast)
    assert newHandle == f"{nameFirst.lower()}{nameLast.lower()}"
    assert type(createU_ID(data)) is int
    assert emailExists(email, data) is False
    assert uniqueHandle(data, newHandle) == f"{nameFirst.lower()}{nameLast.lower()}"
    assert checkEmail(email) is True

def test_invalid_email_auth_register ():

    '''
    Testing if auth_register raises a ValueError
    if passed an invalid email.
    '''
    email1 = "invalidEmail"
    email2 = ""
    email3 = ".com"

    with pytest.raises(errors.ValueError): 
        checkEmail(email1)

    with pytest.raises(errors.ValueError): 
        checkEmail(email2)

    with pytest.raises(errors.ValueError): 
        checkEmail(email3)

def test_taken_email_auth_register ():

    '''
    Testing if auth_register raises a ValueError
    if passed an email which has been taken by another user.
    '''

    data = {
        "users": [{
            "email": "valid@email.com", 
            "password": "validPassword", 
            "name_first": "validFirst", 
            "name_last": "validLast", 
            "handle": "validFirstvalidLast", 
            "u_id": 8501, 
            "resetCode": None, 
            "is_admin": 1, 
            "img_url": None}],
        "tokens": [], 
        "channels": [],
        }

    assert emailExists("valid@email.com", data)

def test_invalid_password_auth_register ():

    '''
    Testing if auth_register raises a ValueError
    if passed an invalid password.
    '''

    password1 = "short"
    password2 = ""
    password3 = "123"

    with pytest.raises(errors.ValueError): 
        checkPassword(password1)

    with pytest.raises(errors.ValueError): 
        checkPassword(password2)    

    with pytest.raises(errors.ValueError): 
        checkPassword(password3)    
        
def test_invalid_first_auth_register ():

    '''
    Testing if auth_register raises a ValueError
    if passed an invalid first and last name (i.e. > 50 or < 1 characters)
    '''

    nameFirst1, nameLast1 = "", ""
    nameFirst2, nameLast2 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

    with pytest.raises(errors.ValueError):
        checkName(nameFirst1, nameLast1)

    with pytest.raises(errors.ValueError):
        checkName(nameFirst2, nameLast2)


def test_taken_u_id ():

    '''
    Testing if auth_register creates a new u_id if already taken
    '''

    data = {
        "users": [{
            "email": "valid@email.com", 
            "password": "validPassword", 
            "name_first": "validFirst", 
            "name_last": "validLast", 
            "handle": "validFirstvalidLast", 
            "u_id": 1234, 
            "resetCode": None, 
            "is_admin": 1, 
            "img_url": None}],
        "tokens": [], 
        "channels": []
    }

    for x in range(0, 10000):
        assert createU_ID(data) != 1234

    assert len(str(createU_ID(data))) <= 6

def test_taken_email ():

    '''
    Testing if auth_register is altered if the email is already taken
    '''

    data = {
        "users": [{
            "email": "valid@email.com", 
            "password": "validPassword", 
            "name_first": "validFirst", 
            "name_last": "validLast", 
            "handle": "validFirstvalidLast", 
            "u_id": 1234, 
            "resetCode": None, 
            "is_admin": 1, 
            "img_url": None}],
        "tokens": [], 
        "channels": []
    }

    assert emailExists("valid@email.com", data)
    assert emailExists("new@email.com", data) is False

def test_unique_handle ():

    '''
    Testing if auth_register creates a new handle if it has already been taken
    '''

    data = {
        "users": [{
            "email": "valid@email.com", 
            "password": "validPassword", 
            "name_first": "validFirst", 
            "name_last": "validLast", 
            "handle": "validFirstvalidLast", 
            "u_id": 1234, 
            "resetCode": None, 
            "is_admin": 1, 
            "img_url": None}],
        "tokens": [], 
        "channels": []
    }

    newHandle = uniqueHandle(data, "validFirstvalidLast")
    assert newHandle != "validFirstvalidLast"
    assert len(newHandle) <= 20
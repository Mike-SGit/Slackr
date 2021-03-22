import pytest
import errors

from auth_register_helper import checkPassword
from password_reset import resetPasswordFunc
from hash_password import hashPassword

def test_valid_reset():

    '''
    Testing if auth_passwordreset functions return expected outputs 
    if passed the correct password and reset code.
    '''

    data = {
        "users": [{
            "email": "valid@email.com", 
            "password": hashPassword("validPassword"), 
            "name_first": "validFirst", 
            "name_last": "validLast", 
            "handle": "validFirstvalidLast", 
            "u_id": 8501, 
            "resetCode": 1234, 
            "is_admin": 1, 
            "img_url": None}],
        "tokens": [], 
        "channels": [],
        }

    checkPassword("validNewPassword")
    assert resetPasswordFunc(data, 1234, "validNewPassword") is None
    assert data['users'][0]['password'] == hashPassword("validNewPassword")
    assert data['users'][0]['resetCode'] is None

def test_invalid_reset():

    '''
    Testing if auth_passwordreset functions return expected outputs 
    if passed an incorrect password and reset code.
    '''

    invalidNewPassword = "123"

    with pytest.raises(errors.ValueError): 
        checkPassword(invalidNewPassword)

def test_invalid_code():

    '''
    Testing if auth_passwordreset functions return expected outputs 
    if passed a correct password but an invalid reset code.
    '''

    data = {
        "users": [{
            "email": "valid@email.com", 
            "password": hashPassword("validPassword"), 
            "name_first": "validFirst", 
            "name_last": "validLast", 
            "handle": "validFirstvalidLast", 
            "u_id": 8501, 
            "resetCode": 1234, 
            "is_admin": 1, 
            "img_url": None}],
        "tokens": [], 
        "channels": [],
        }

    checkPassword("validNewPassword")
    with pytest.raises(errors.ValueError): 
        resetPasswordFunc(data, 4321, "validNewPassword")
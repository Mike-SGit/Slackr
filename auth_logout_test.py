import pytest
import errors

from logout_helper import logoutFunc
from hash_password import hashPassword

def test_valid_logout():

    '''
    Testing if auth_logout functions return expected outputs 
    if passed the correct password and email.
    '''

    data = {
        "users": [{
            "email": "valid@email.com", 
            "password": hashPassword("validPassword"), 
            "name_first": "validFirst", 
            "name_last": "validLast", 
            "handle": "validFirstvalidLast", 
            "u_id": 8501, 
            "resetCode": None, 
            "is_admin": 1, 
            "img_url": None}],
        "tokens": ["validToken"], 
        "channels": [],
        }

    assert logoutFunc(data, "validToken")

def test_invalid_logout():

    '''
    Testing if auth_logout functions return expected outputs 
    if passed an incorrect password and email.
    '''

    data = {
        "users": [{
            "email": "valid@email.com", 
            "password": hashPassword("validPassword"), 
            "name_first": "validFirst", 
            "name_last": "validLast", 
            "handle": "validFirstvalidLast", 
            "u_id": 8501, 
            "resetCode": None, 
            "is_admin": 1, 
            "img_url": None}],
        "tokens": ["validToken"], 
        "channels": [],
        }

    assert logoutFunc(data, "invalidToken") is False
    assert logoutFunc(data, "") is False
    assert logoutFunc(data, None) is False
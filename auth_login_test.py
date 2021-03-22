import pytest
import errors

from login_helper import loginFunc 
from hash_password import hashPassword

def test_valid_login():

    '''
    Testing if auth_login functions return expected outputs 
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
        "tokens": [], 
        "channels": [],
        }

    assert loginFunc(data, "valid@email.com", "validPassword") == data['users'][0]

def test_invalid_login_password():

    '''
    Testing if auth_login functions raises a Value Error if 
    if passed the correct email but incorrect password.
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
        "tokens": [], 
        "channels": [],
        }    

    with pytest.raises(errors.ValueError): 
        loginFunc(data, "valid@email.com", "invalidPassword")

def test_invalid_login_email():
    
    '''
    Testing if auth_login functions raises a Value Error if 
    if passed an incorrect email and incorrect password.
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
        "tokens": [], 
        "channels": [],
        }    

    with pytest.raises(errors.ValueError): 
        loginFunc(data, "invalid@email.com", "invalidPassword")

def test_invalid_login_email_correct_password():
    
    '''
    Testing if auth_login functions raises a Value Error if 
    if passed an incorrect email and correct password.
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
        "tokens": [], 
        "channels": [],
        }    

    with pytest.raises(errors.ValueError): 
        loginFunc(data, "invalid@email.com", "validPassword")

    
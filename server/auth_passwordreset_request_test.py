import pytest

def auth_passwordreset_request(email):
    pass

def test_return_auth_passwordreset_request():
    
    '''
    Testing if auth_passwordreset_request correctly returns None regardless of being 
    passed an invalid or valid email.
    '''

    # BEGIN SET UP
    validEmail = "valid@email.com"
    invalidEmail = "invalid@email.com"
    # END SET UP

    assert auth_passwordreset_request (validEmail) == None
    assert auth_passwordreset_request (invalidEmail) == None
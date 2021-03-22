import pytest

def auth_logout (token):
    pass

def test_valid_auth_logout ():
    
    '''
    Testing if auth_logout correctly returns None regardless of being 
    passed an invalid or valid token.
    '''

    # BEGIN SET UP
    validToken = "validToken"
    invalidToken = "invalidToken"
    # END SET UP

    assert auth_logout (validToken) == None
    assert auth_logout (invalidToken) == None 

def test_token_change_auth_logout ():

    '''
    Testing if auth_logout correctly changes the passed token to become
    invalidated
    '''

    # BEGIN SET UP
    validToken = "validToken"
    invalidToken = "invalidToken"
    # END SET UP

    auth_logout (validToken)
    assert validToken == invalidToken
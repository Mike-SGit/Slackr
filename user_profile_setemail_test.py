from user_helper import user_profile_setemail
import errors
from test_data import *
import pytest



# TESTS
def test_user_profile_setemail_correct():
    
    user_profile_setemail(data, token, "sherryb@gmail.com")
    user_profile_setemail(data, token, "sherrybirkin@gmail.com")

def test_user_profile_setemail_invalid_01():
    with pytest.raises(errors.ValueError):
        user_profile_setemail(data, token, "sherryb")

def test_user_profile_setemail_invalid_02():    
    with pytest.raises(errors.ValueError):
        user_profile_setemail(data, token, "sherryb@gmailcom")

def test_user_profile_setemail_invalid_03():
    with pytest.raises(errors.ValueError):
        user_profile_setemail(data, token, "sherrybgmail.com")

def test_user_profile_setemail_invalid_04():
    with pytest.raises(errors.ValueError):
        user_profile_setemail(data, token, "")

def test_user_profile_setemail_invalid_05():
    with pytest.raises(errors.ValueError):
        user_profile_setemail(data, token, "123")


# Can only contain letter or number before @
def test_user_profile_setemail_invalid_06():
    with pytest.raises(errors.ValueError):
        user_profile_setemail(data, token, "sherry!@gmailcom")

def test_user_profile_setemail_invalid_07():
    with pytest.raises(errors.ValueError):
        user_profile_setemail(data, token, "sherry_birkin@gmailcom")

def test_user_profile_setemail_invalid_08():
    with pytest.raises(errors.ValueError):
        user_profile_setemail(data, token, "sherry birkin@gmailcom")

def test_user_profile_setemail_invalid_09():
    with pytest.raises(errors.ValueError):
        user_profile_setemail(data, token, "she\/?rry@gmailcom")
    
    

# Email address is already being used by another user
def test_user_profile_setemail_used():
    with pytest.raises(errors.ValueError):
        user_profile_setemail(data, token2, "sherry@gmail.com")


# Email address that is too long
def test_user_profile_setemail_long():
    with pytest.raises(errors.ValueError):
        user_profile_setemail(data, token, "sherrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrry@gmail.com")



def test_user_profile_setemail_invaild_token():
    with pytest.raises(errors.ValueError):
        user_profile_setemail(data, 'invalidToken' , "sherry@gmail.com")


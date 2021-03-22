from user_helper import user_profile_sethandle
from test_data import *
import errors
import pytest



# TESTS
def test_user_profile_sethandle_correct():
    
    user_profile_sethandle(data, token, "Sherry")
    user_profile_sethandle(data, token, "SherryBirkin")
    user_profile_sethandle(data, token, "sherry1234")
    user_profile_sethandle(data, token, "MissSherry")
    user_profile_sethandle(data, token, "1234")
    user_profile_sethandle(data, token, "Sherry12345678912345")
    


# Too long
def test_user_profile_sethandle_long_01():
    with pytest.raises(errors.ValueError):
        user_profile_sethandle(data, token, "Sherry123456789123456")

def test_user_profile_sethandle_long_02():
    with pytest.raises(errors.ValueError):
        user_profile_sethandle(data, token, "Sherry123456789123456789sdfsgsgfgdsds")
        

# Cannot contain space and punctuations
# Handle can only by letters and digits
def test_user_profile_sethandle_invalid_01():
    with pytest.raises(errors.ValueError):
        user_profile_sethandle(data, token, "Sherry Birkin")

def test_user_profile_sethandle_invalid_02():
    with pytest.raises(errors.ValueError):
        user_profile_sethandle(data, token, "Sherry_Birkin")

def test_user_profile_sethandle_invalid_03():
    with pytest.raises(errors.ValueError):
        user_profile_sethandle(data, token, "Sherry_Birkin_")

def test_user_profile_sethandle_invalid_04():
    with pytest.raises(errors.ValueError):
        user_profile_sethandle(data, token, "Sherry!")

def test_user_profile_sethandle_invalid_05():
    with pytest.raises(errors.ValueError):
        user_profile_sethandle(data, token, "Sherry-Birkin")

def test_user_profile_sethandle_invalid_06():
    with pytest.raises(errors.ValueError):
        user_profile_sethandle(data, token, "Sherry.Birkin")

def test_user_profile_sethandle_invalid_07():
    with pytest.raises(errors.ValueError):
        user_profile_sethandle(data, token, ".Sherry")

def test_user_profile_sethandle_invalid_08():
    with pytest.raises(errors.ValueError):
        user_profile_sethandle(data, token, ".")

def test_user_profile_sethandle_invalid_09():
    with pytest.raises(errors.ValueError):
        user_profile_sethandle(data, token, " ")

def test_user_profile_sethandle_invalid_10():
    with pytest.raises(errors.ValueError):
        user_profile_sethandle(data, token, "")


# Handle has already being used
def test_user_profile_sethandle_used():
    with pytest.raises(errors.ValueError):
        user_profile_sethandle(data, token, "chrisbirkin")



def test_user_profile_sethandle_invaild_token():
    
    with pytest.raises(errors.ValueError):
        user_profile_sethandle(data, 'invaildToken', "Sherry")







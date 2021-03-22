from user_helper import user_profile_setname
from test_data import *
import errors
import pytest



# TESTS
def test_user_profile_setname_correct():
	user_profile_setname(data, token, "Bob", "Smith")


def test_user_profile_setname_long_last_name():
    
    with pytest.raises(errors.ValueError):
        user_profile_setname(data, token, "Bob", "Smithhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")


def test_user_profile_setname_long_first_name():
    
    with pytest.raises(errors.ValueError):
        user_profile_setname(data, token, "Bobbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", "Smith")


def test_user_profile_setname_long_both():
    
    with pytest.raises(errors.ValueError):
        user_profile_setname(data, token, "Bobbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", "Smithhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")


def test_user_profile_setname_digit_last_name():
    
    with pytest.raises(errors.ValueError):
        user_profile_setname(data, token, "Bob", "Smith1")


def test_user_profile_setname_digit_first_name():

    with pytest.raises(errors.ValueError):
        user_profile_setname(data, token, "233", "Smith")


def test_user_profile_setname_digit_name_01():
    
    with pytest.raises(errors.ValueError):
        user_profile_setname(data, token, "B0b", "Smi0th")

def test_user_profile_setname_digit_name_02():
    with pytest.raises(errors.ValueError):
        user_profile_setname(data, token, "000", "3")



def test_user_profile_setname_empty_name_01():
    with pytest.raises(errors.ValueError):
        user_profile_setname(data, token, "", "Smith")

def test_user_profile_setname_empty_name_02():
    with pytest.raises(errors.ValueError):
        user_profile_setname(data, token, "Bob", "")

def test_user_profile_setname_empty_name_03():
    with pytest.raises(errors.ValueError):
        user_profile_setname(data, token, "", "")


def test_user_profile_setemail_invaild_token():
    with pytest.raises(errors.ValueError):
        user_profile_setname(data, 'invalidToken', "Bob", "Smith")


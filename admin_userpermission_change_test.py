from admin_userpermission_change import admin_userpermission_change
from test_data import *
import errors
import pytest



# TESTS
def test_admin_userpermission_change_correct():
    
    # Sherry modify Chris's permission level
    admin_userpermission_change(data, token, u_id2, 2)
    admin_userpermission_change(data, token, u_id2, 3)



# Value Error

def test_admin_userpermission_change_invaild_uid():
    
    # Sherry modify an invaild u_id
    with pytest.raises(errors.ValueError):
        admin_userpermission_change(data, token, 'invaild_u_id', 2)


def test_admin_userpermission_change_invaild_permid_01():
    # Sherry has LV.1 permission
    # Chris has LV.3 permission
    # Sherry modify Chris's permission level
    with pytest.raises(errors.ValueError):
        admin_userpermission_change(data, token, u_id2, 4)

def test_admin_userpermission_change_invaild_permid_02():
    with pytest.raises(errors.ValueError):
        admin_userpermission_change(data, token, u_id2, 9)

def test_admin_userpermission_change_invaild_permid_03():
    with pytest.raises(errors.ValueError):
        admin_userpermission_change(data, token, u_id2, -1)

def test_admin_userpermission_change_invaild_permid_04():
    with pytest.raises(errors.ValueError):
        admin_userpermission_change(data, token, u_id2, "a")

def test_admin_userpermission_change_invaild_permid_05():
    with pytest.raises(errors.ValueError):
        admin_userpermission_change(data, token, u_id2, "abc1")




# Access Error
def test_admin_userpermission_change_admin_01():
    # Sherry has LV.1 permission
    # Chris has LV.3 permission
    
    # Chris modify Sherry's permission level
    with pytest.raises(errors.AccessError):
        admin_userpermission_change(data, token2, u_id, 3)

def test_admin_userpermission_change_admin_02():    
    with pytest.raises(errors.AccessError):
        admin_userpermission_change(data, token2, u_id, 2)


def test_admin_userpermission_change_invaild_token():
    
    with pytest.raises(errors.ValueError):
        admin_userpermission_change(data, 'invaildToken', u_id2, "1")







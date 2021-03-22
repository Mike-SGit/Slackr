from user_helper import user_profile
import errors
from test_data import *
import pytest   



# TESTS
def test_user_profile():
    assert user_profile(data, token, u_id) == {
        'email': 'sherry@gmail.com',
        'name_first': 'Sherry',
        'name_last': 'Birkin',
        'handle_str': 'sherrybirkin',
    }
    
    assert user_profile(data, token, u_id2) == {
        'email': 'chris123@gmail.com',
        'name_first': 'Chris',
        'name_last': 'Birkin',
        'handle_str': 'chrisbirkin', 
    }


def test_user_profile_wrong_uid():

    with pytest.raises(errors.ValueError):
        user_profile(data, token, 'invaild_u_id')


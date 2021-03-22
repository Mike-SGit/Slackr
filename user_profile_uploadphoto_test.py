from user_helper import user_profile_uploadphoto
from test_data import *
from PIL import Image
from io import BytesIO
import pytest
import errors
import requests


img_url = "https://www.bigw.com.au/medias/sys_master/images/images/h56/h2f/14184123367454.jpg"
img_url_not_200 = "https://www.bigw.com.au/medias/sys_master/images/images/h56/h2f/1418467454.jpg"
img_url_not_jpg = "https://www.stickpng.com/assets/images/580b57fbd9996e24bc43bc9b.png"


def test_user_profile_uploadphoto_correct():
    user_profile_uploadphoto(data, token, img_url, 600, 100, 900, 400)


def test_user_profile_uploadphoto_http():
    with pytest.raises(errors.ValueError):
        user_profile_uploadphoto(data, token, img_url_not_200, 600, 100, 900, 400)


def test_user_profile_uploadphoto_jpg():
    with pytest.raises(errors.ValueError):
        user_profile_uploadphoto(data, token, img_url_not_jpg, 10, 10, 200, 200)

def test_user_profile_uploadphoto_dimension_01():
    with pytest.raises(errors.ValueError):
        user_profile_uploadphoto(data, token, img_url, -600, 100, 900, 400)


def test_user_profile_uploadphoto_dimension_02():
    with pytest.raises(errors.ValueError):
        user_profile_uploadphoto(data, token, img_url, 600, -1, 900, 400)


def test_user_profile_uploadphoto_dimension_03():
    with pytest.raises(errors.ValueError):
        user_profile_uploadphoto(data, token, img_url, 600, 100, -10, 400)


def test_user_profile_uploadphoto_dimension_04():
    with pytest.raises(errors.ValueError):
        user_profile_uploadphoto(data, token, img_url, 600, 100, 900, -1)


def test_user_profile_uploadphoto_dimension_05():
    with pytest.raises(errors.ValueError):
        user_profile_uploadphoto(data, token, img_url, 60000, 100, 900, 400)


def test_user_profile_uploadphoto_dimension_06():
    with pytest.raises(errors.ValueError):
        user_profile_uploadphoto(data, token, img_url, 600, 100, 900, 40000)


def test_user_profile_uploadphoto_end_larger_01():
    with pytest.raises(errors.ValueError):
        user_profile_uploadphoto(data, token, img_url, 900, 100, 600, 400)


def test_user_profile_uploadphoto_end_larger_02():
    with pytest.raises(errors.ValueError):
        user_profile_uploadphoto(data, token, img_url, 600, 100, 900, 50)


def test_user_profile_setemail_invaild_token():
    with pytest.raises(errors.ValueError):
        user_profile_uploadphoto(data, 'invaildToken', img_url, 600, 900, 100, 400)


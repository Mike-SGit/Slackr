from auth_register_helper import checkEmail, getUserFromToken
from errors import AccessError, ValueError
from json import dumps
from PIL import Image
from io import BytesIO
import urllib.request
import requests



def user_profile(data, token, u_id):
    profile = {}

    # Check if u_id exists
    exist = False
    for user in data['users']:
        if user['u_id'] == u_id:
            exist = True
            profile['email'] = user['email']
            profile['name_first'] = user['name_first']
            profile['name_last'] = user['name_last']
            profile['handle_str'] = user['handle']

    # Raise error u_id if not exist
    if exist == False:
        raise ValueError("u_id does not refer to a valid user")

    return profile


def user_profile_setemail(data, token, email):
    # Decode token to match user
    u_id = getUserFromToken(token)

    # Check email is vaild, use function in auth_register_helper
    checkEmail(email)

    # Reset
    for user in data['users']:
        if email in user['email']:
            raise ValueError("Email address is already being used")
        elif user['u_id'] == u_id:
            user['email'] = email


def user_profile_sethandle(data, token, handle_str):
    # Check if the handle is valid
    letter_number = True

    # Assumption: Has to be letter or number
    for i in handle_str:
        if not (i.isdigit() or i.isalpha()):
            letter_number = False

    if len(handle_str) > 20:
        raise ValueError("Should be no more than 20 characters")
    elif letter_number == False:
        raise ValueError("Handle can only be letters and digits")
    elif not handle_str:
        raise ValueError("Handle cannot be empty")
    
    # Decode token to match user
    u_id = getUserFromToken(token)
    # Reset
    for user in data['users']:
        if user['handle'] == handle_str:
            raise ValueError("Handle is already being used")
        elif user['u_id'] == u_id:
            user['handle'] = handle_str


def user_profile_setname(data, token, name_first, name_last):
    # Check if the names are valid
    # Error will arise if vaild
    if not name_first.isalpha() or not name_last.isalpha():
        raise ValueError("Should contain alpha letters only")
    elif len(name_first) > 50:
        raise ValueError("First name can not be more than 50 characters")
    elif len(name_last) > 50:
        raise ValueError("Last name can not be more than 50 characters")

    # Decode token to match user
    u_id = getUserFromToken(token)
    # Reset
    for user in data['users']:
        if user['u_id'] == u_id:
            user['name_last'] = name_last
            user['name_first'] = name_first


def user_profile_uploadphoto(data, token, img_url, x_start, y_start, x_end, y_end):
    # Decode token to match user
    u_id = getUserFromToken(token)
    
    # Eroor checking
    req = requests.head(img_url)
    status = req.status_code
    if status != 200:
        raise ValueError("Invaild URL: HTTP status is not 200")
    elif img_url[-3:] != 'jpg':
        raise ValueError("Invaild URL: Not a JPG image")

    # Image down
    save_name = "./photo/" + str(u_id) + "photo.jpg"
    urllib.request.urlretrieve(img_url, save_name)

    # Error checking: Out of dimension
    data = requests.get(img_url).content
    im = Image.open(BytesIO(data))
    width, height = im.size
    if x_start < 0 or x_start > width or x_end < 0 or x_end > width or y_start < 0 or y_start > height or y_end < 0 or y_end > height:
        raise ValueError("Out of dimension")
    elif x_end <= x_start or y_end <= y_start:
        raise ValueError("x_start, y_start are left top corner; x_end, y_end are right bottom corner")

    # Crop
    save_crop_name = "./photo/" + str(u_id) + "photoCrop.jpg"
    imageObject = Image.open(save_name)
    cropped = imageObject.crop((x_start, y_start, x_end, y_end))
    cropped.save(save_crop_name)

    
    # Reset
    '''
    for user in data['users']:
        if user['u_id'] == u_id:
            user['img_url'] = ???
    '''

# ====== Start of imported library modules ======= #
import os
import threading
import jwt # Be sure to have installed PyJWT; pip3 install pyjwt
import hashlib
from json import dumps, dump, load
from flask import Flask, request, jsonify
from flask_cors import CORS # Be sure to have installed flask_cors; pip3 install flask_cors
from werkzeug.exceptions import HTTPException
from flask_mail import Mail, Message # Be sure to have installed flask_mail; pip3 install flask_mail
from random import randrange
# ======= End of imported library modules ======== #

#  =========== Start of imported files =========== #
from errors import AccessError, ValueError
from auth_register_helper import checkEmail, checkPassword, checkName, createHandle, randomHandle, createU_ID, getUserFromToken, validUser
from channels_helper import channelNameCheck, userIsInChannel, addUserToChannel, addOwnerToChannel, removeOwnerFromChannel, removeUserFromChannel, joinChannel
from channels_create import channelsCreate
from user_profile import user_profile
from user_profile_setname import user_profile_setname
from user_profile_setemail import user_profile_setemail
from user_profile_sethandle import user_profile_sethandle
from admin_userpermission_change import admin_userpermission_change
# ============ End of imported files ============= #

def defaultHandler(err):
    response = err.get_response()
    response.data = dumps({
        'code': err.code,
        'name': 'System Error',
        'message': err.description,
    })
    response.content_type = 'application/json'
    return response

APP = Flask(__name__)
APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)
CORS(APP)
APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'h13ahsp@gmail.com',
    MAIL_PASSWORD = "2521isworse"
)

JWTSECRET = 'myjwtsecret'
PERMISSION1 = 1
PERMISSION2 = 2
PERMISSION3 = 3

data = {
    'users': [],
    'tokens': [],
    'channels': [],
}
if os.path.exists('dataStore.json'):
    with open('dataStore.json', 'r') as FILE:
        data = load(FILE)

def save():
    global data
    print('Saving...')
    with open('dataStore.json', 'w') as FILE:
        dump(data, FILE)

def timerAction():
    timer = threading.Timer(1.0, timerAction)
    timer.start()
    save()

timerAction()

def getData():
    global data
    return data

def sendSuccess(data):
    return dumps(data)

def sendError(message):
    return dumps({
        '_error' : message,
    })

def generateToken(u_id):
    global JWTSECRET
    encoded = str(jwt.encode({'u_id': u_id}, JWTSECRET, algorithm='HS256'))
    return encoded[2:-1]
    # This removes the 'b' and the apostrophes surronding the JWT which indicate that is it a byte string, 
    # however they cause invalid header padding and are unnecessary, they're truncated off. 

def hashPassword(password):
    return hashlib.sha256(password.encode()).hexdigest()

def checkTokenValidity(token, data):
    if token in data['tokens']:
        if getUserFromToken(request.args.get('token')) is not None:
            return True
    else:
        raise AccessError('Invalid Token!')

def invalidateToken(token, tokenList):
    # Tokens are invalidated by removing all occurances from the tokenList
    while token in tokenList: 
        tokenList.remove(token)
    return tokenList

@APP.route('/echo/post', methods = ['POST'])
def echoPost():
    input = request.form.get('echo')
    sendSuccess({'echo': input})

@APP.route('/echo/get', methods = ['GET'])
def echoGet():
    input = request.args.get('echo')
    sendSuccess({'echo': input})

@APP.route('/auth/register', methods=['POST'])
def create():
    data = getData()
    email = request.form.get('email')
    password = request.form.get('password')
    nameFirst = request.form.get('name_first')
    nameLast = request.form.get('name_last')
    handle = createHandle(nameFirst, nameLast) # In the form 'firstNamelastName' or if already taken: 'firstNamelastName123'.
    u_id = createU_ID(data) # In the form 'U123456'.

    for users in data['users']:
        if email in users['email']:
            raise ValueError ('Email entered is already being used.')
        while handle in users['handle']:
            handle = randomHandle(handle)
            
    checkEmail(email)
    checkPassword(password)
    checkName(nameFirst, nameLast)

    data['users'].append({
        'email': email,
        'password': hashPassword(password),
        'name_first': nameFirst,
        'name_last': nameLast,
        'handle': handle, 
        'u_id': u_id,
        'resetCode': None,
        'is_admin': PERMISSION3,
    })

    # The very first user who signs up is an owner
    data['users'][0]['is_admin'] = PERMISSION1

    data['tokens'].append(generateToken(u_id))
    print(data)
    
    return sendSuccess({
        'u_id': u_id,
        'token': generateToken(u_id),
    })

@APP.route('/auth/login', methods=['POST'])
def connect():
    data = getData()
    email = request.form.get('email')
    password = request.form.get('password')
    checkEmail(email)

    for user in data['users']:
        if user['email'] == email and user['password'] == hashPassword(password):  
            data['tokens'].append(generateToken(user['u_id']))
            return sendSuccess({
                'u_id': user['u_id'],
                'token': generateToken(user['u_id']),
            })
        elif user['email'] == email and user['password'] != hashPassword(password):
            raise ValueError('Password is incorrect.')
    raise ValueError('Email does not belong to a user.')

@APP.route('/auth/logout', methods=['POST'])
def logout():
    data = getData()
    isSuccess = False
    token = request.args.get('token')
    checkTokenValidity(token, data)

    if token in data['tokens']:
        data['tokens'] = invalidateToken(token, data['tokens'])
        isSuccess = True

    return sendSuccess({
        'is_success': isSuccess,
    })    

@APP.route('/auth/passwordreset/request', methods=['POST'])
def passwordRequest():
    data = getData()
    email = request.form.get('email')

    for user in data['users']:
        if user['email'] == email:
            resetCode = randrange(99999)
            user['resetCode'] = resetCode # Sets a 5 digit random reset code.
            mail = Mail(APP)
            try:
                msg = Message("Slackr: Account Reset Code",
                    sender="h13ahsp@gmail.com",
                    recipients=[email])
                msg.body = f"Hello, your account password reset code is: {user['resetCode']}"
                mail.send(msg)
                return 'Mail sent! Please check your indox.'
            except Exception as e:
                return (str(e))
    return sendSuccess({})

@APP.route('/auth/passwordreset/reset', methods=['POST'])
def reset():
    data = getData()
    resetCode = int(request.form.get('reset_code'))
    newPassword = request.form.get('new_password')

    checkPassword(newPassword)

    for user in data['users']:
        if user['resetCode'] == resetCode:
            user['password'] = hashPassword(newPassword)
            user['resetCode'].remove(resetCode)
            return sendSuccess({})
    raise ValueError ('Reset code is not valid.')

@APP.route('/channel/invite', methods=['POST'])
def channelInvite():
    data = getData()
    token = request.args.get('token')
    checkTokenValidity(token, data)
    channel_id = request.form.get('channel_id')
    u_id = request.form.get('u_id')

    userIsInChannel(data, channel_id, getUserFromToken(token))
    if validUser(data, u_id) is False:
        raise ValueError ('The invitee is an invalid user.')

    addUserToChannel(data, channel_id, u_id)
    return sendSuccess({})

@APP.route('/channel/details', methods=['GET'])
def channelDetails():
    data = getData()
    token = request.args.get('token')
    checkTokenValidity(token, data)
    u_id = getUserFromToken(token)
    channel_id = request.form.get('channel_id')

    userIsInChannel(data, channel_id, u_id)

    for channel in data['channels']:
        if channel_id == channel['channel_id']:
            name = channel['name']
            owner_members = channel['owners']
            all_members = channel['members']

    return sendSuccess({
        'name': name,
        'owner_members': owner_members,
        'all_members': all_members,
    })

@APP.route('/channel/messages', methods=['GET'])
def channelMessages():
    data = getData()
    token = request.args.get('token')
    checkTokenValidity(token, data)
    u_id = getUserFromToken(token)
    channel_id = request.form.get('channel_id')
    start = request.form.get('start')

    userIsInChannel(data, channel_id, u_id)

    # TODO
    return sendSuccess({
        #'messages': messages,
        'start': start,
        #'end': end,
    })
    

@APP.route('/channel/leave', methods=['POST'])
def leaveChannel():
    data = getData()
    token = request.args.get('token')
    checkTokenValidity(token, data)
    u_id = getUserFromToken(token)
    channel_id = request.form.get('channel_id')

    removeUserFromChannel(data, channel_id, u_id)
    return sendSuccess({})

@APP.route('/channel/join', methods=['POST'])
def channelJoin():
    data = getData()
    token = request.args.get('token')
    checkTokenValidity(token, data)
    u_id = getUserFromToken(token)
    channel_id = request.form.get('channel_id')

    joinChannel(data, channel_id, u_id)
    return sendSuccess({})


@APP.route('/channel/addowner', methods=['POST'])
def addOwner():
    token = request.args.get('token')
    checkTokenValidity(token, data)
    u_id = getUserFromToken(token)
    new_owner_u_id = request.form.get('u_id')
    channel_id = request.form.get('channel_id')

    addOwnerToChannel(data, channel_id, u_id, new_owner_u_id)
    return sendSuccess({})

@APP.route('/channel/removeowner', methods=['POST'])
def removeOwner():
    token = request.args.get('token')
    checkTokenValidity(token, data)
    u_id = getUserFromToken(token)
    target_owner_u_id = request.form.get('u_id')
    channel_id = request.form.get('channel_id')

    removeOwnerFromChannel(data, channel_id, u_id, target_owner_u_id)
    return sendSuccess({})

@APP.route('/channels/list', methods=['GET'])
def list():
    # Returns a list of all the PUBLIC and PRIVATE channels that the user is a member of.
    token = request.args.get('token')
    checkTokenValidity(token, data)
    u_id = getUserFromToken(token)

    returnList = []
    for channel in data['channels']:
        if u_id in channel['members']: 
            positiveChannel = {
                'channel_id': channel['channel_id'],
                'name': channel['name'],
            }
            returnList.append(positiveChannel)
    return sendSuccess({'channels': returnList})
      
@APP.route('/channels/listall', methods=['GET'])
def listAll():
    # Returns a list of all the PUBLIC channels (as well as PRIVATE channels if the user is a member of any).
    token = request.args.get('token')
    checkTokenValidity(token, data)
    u_id = getUserFromToken(token)

    returnList = []
    for channel in data['channels']:
        if channel['is_public'] is True or u_id in channel['members']:
            positiveChannel = {
                'channel_id': channel['channel_id'],
                'name': channel['name'],
            }
            returnList.append(positiveChannel)
    return sendSuccess({'channels': returnList})

@APP.route('/channels/create', methods=['POST'])
def createChannel():
    data = getData()
    token = request.args.get('token')
    checkTokenValidity(token, data)
    name = request.form.get('name')
    is_public = request.form.get('is_public') # Expects True or False

    checkTokenValidity(token, data)
    channelNameCheck(name)
    u_id = getUserFromToken(token)

    channel_id = channelsCreate(data, u_id, name, is_public)

    print(data['channels'])
    return sendSuccess({
        'channel_id': channel_id,
    })


## Justin's work

@APP.route('/user/profile', methods=['GET'])
def viewUserProfile():
    data = getData()
    u_id = request.args.get('u_id')
    token = request.args.get('token')
    checkTokenValidity(token, data)

    profile = user_profile(data, token, u_id)
    return dumps(profile)



@APP.route('/user/profile/setname', methods=['PUT'])
def setName():
    data = getData()
    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')
    token = request.args.get('token')
    checkTokenValidity(token, data)
    
    user_profile_setname(data, token, name_first, name_last)
    return sendSuccess({})



@APP.route('/user/profile/setemail', methods=['PUT'])
def setEmail():
    data = getData()
    new_email = request.form.get('email')
    token = request.args.get('token')
    checkTokenValidity(token, data)

    user_profile_setemail(data, token, new_email)
    return sendSuccess({})


@APP.route('/user/profile/sethandle', methods=['PUT'])
def setHandle():
    data = getData()
    handle_str = request.form.get('handle')
    token = request.args.get('token')
    checkTokenValidity(token, data)

    user_profile_sethandle(data, token, handle_str)
    return sendSuccess({})



@APP.route('/admin/userpermission/change', methods=['POST'])
def changePermission():
    data = getData()
    u_id = request.form.get('u_id')
    token = request.args.get('token')
    checkTokenValidity(token, data)
    permission_id = int(request.form.get('permission_id'))

    # TODO: how permission works, add id in?
    # TODO: ACCESS ERROR check permission level

    admin_userpermission_change(data, token, u_id, permission_id)
    return sendSuccess({})






if __name__ == '__main__':
    APP.run(debug=True, port=3000)


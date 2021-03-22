# ====== Start of imported library modules ======= #
import sys
import os
import threading
import jwt # Be sure to have installed PyJWT; pip3 install pyjwt
import datetime
from flask_cors import CORS # Be sure to have installed flask_cors; pip3 install flask_cors
from json import dumps, dump, load
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.exceptions import HTTPException
from flask_mail import Mail, Message # Be sure to have installed flask_mail; pip3 install flask_mail
from random import randrange
# ======= End of imported library modules ======== #

#  =========== Start of imported files =========== #
from errors import AccessError, ValueError
from invalidate_token import invalidateToken
from hash_password import hashPassword
from auth_register_helper import createUser, emailExists, checkEmail, checkPassword, checkName, createHandle, randomHandle, uniqueHandle, createU_ID, getUserFromToken, validUser
from login_helper import loginFunc
from logout_helper import logoutFunc
from password_reset import resetPasswordFunc
from channels_helper import channelNameCheck, userIsInChannel, addUserToChannel, addOwnerToChannel, removeOwnerFromChannel, removeUserFromChannel, joinChannel
from channels_create import channelsCreate
from channel_details import getDetails
from channels_lists import channelList, channelListAll
from channel_messages_helper import endFunc
from return_messages import returnMessages
from get_users import getAllUserNames
from user_helper import user_profile, user_profile_setname, user_profile_setemail, user_profile_sethandle, user_profile_uploadphoto
from search import search
from admin_userpermission_change import admin_userpermission_change
from messages_helper import editMessage, remove_message, message_send, validate_remove, validate_message, validate_messageLater
from standup_helper import standupStillActive, standupNotActive, standupEnd
from standup_start import standupStartFunc
from standup_send import standupSendFunc
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
    # print('Saving...')
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

def checkTokenValidity(token, data):
    if token in data['tokens']:
        return True
    else:
        raise AccessError('Invalid Token!')

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
    email, password, nameFirst, nameLast = (request.form[x] for x in ('email', 'password', 'name_first', 'name_last'))
    
    handle = createHandle(nameFirst, nameLast) # In the form 'firstNamelastName' or if already taken: 'firstNamelastName123'.
    u_id = createU_ID(data) # In the form '123456'.

    if emailExists(email, data):
        raise ValueError ('Email entered is already being used.')

    handle = uniqueHandle(data, handle)
            
    checkEmail(email)
    checkPassword(password)
    checkName(nameFirst, nameLast)

    createUser(data, email, hashPassword(password), nameFirst, nameLast, handle, u_id, PERMISSION3)

    data['users'][0]['is_admin'] = PERMISSION1 # The very first user who signs up is an owner

    data['tokens'].append(generateToken(u_id))
    print(data)
    
    return sendSuccess({
        'u_id': u_id,
        'token': generateToken(u_id),
    })

@APP.route('/auth/login', methods=['POST'])
def connect():
    data = getData()
    email, password = (request.form[x] for x in ('email', 'password'))
    checkEmail(email)

    user = loginFunc(data, email, password)
    data['tokens'].append(generateToken(user['u_id']))

    return sendSuccess({
        'u_id': user['u_id'],
        'token': generateToken(user['u_id']),
    })

@APP.route('/auth/logout', methods=['POST'])
def logout():
    data = getData()
    token = request.form.get('token')
    checkTokenValidity(token, data)

    return sendSuccess({
        'is_success': logoutFunc(data, token),
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
    resetPasswordFunc(data, resetCode, newPassword)

    return sendSuccess({})

@APP.route('/channel/invite', methods=['POST'])
def channelInvite():
    data = getData()
    token = request.form.get('token')
    checkTokenValidity(token, data)
    channel_id, u_id = (request.form[x] for x in ('channel_id', 'u_id'))

    userIsInChannel(data, int(channel_id), getUserFromToken(token))
    if validUser(data, int(u_id)) is False:
        raise ValueError ('The invitee is an invalid user.')

    addUserToChannel(data, int(channel_id), int(u_id))
    return sendSuccess({})

@APP.route('/channel/details', methods=['GET'])
def channelDetails():
    data = getData()
    token = request.args.get('token')
    checkTokenValidity(token, data)
    u_id = getUserFromToken(token)
    channel_id = int(request.args.get('channel_id'))

    userIsInChannel(data, channel_id, u_id)

    return sendSuccess(getDetails(data, channel_id))

@APP.route('/channel/messages', methods=['GET'])
def channelMessages():
    data = getData()
    token = request.args.get('token')
    checkTokenValidity(token, data)
    u_id = getUserFromToken(token)

    channel_id, start = (request.args[x] for x in ('channel_id', 'start'))
    channel_id = int(channel_id)
    start = int(start)

    userIsInChannel(data, channel_id, u_id)

    for channel in data['channels']:
        if channel_id == channel['channel_id']:
            tempMessages = channel['messages'][::-1]

    if start > len(tempMessages):
        raise ValueError ('Start is greater than the total number of messages.')
        
    return sendSuccess({
        'messages': returnMessages(tempMessages, start),
        'start': int(start),
        'end': int(endFunc(tempMessages, start)),
    })
    

@APP.route('/channel/leave', methods=['POST'])
def leaveChannel():
    data = getData()
    token = request.form.get('token')
    checkTokenValidity(token, data)
    u_id = getUserFromToken(token)
    channel_id = int(request.args.get('channel_id'))

    removeUserFromChannel(data, int(channel_id), u_id)
    return sendSuccess({})

@APP.route('/channel/join', methods=['POST'])
def channelJoin():
    data = getData()
    token = request.form.get('token')
    checkTokenValidity(token, data)
    u_id = getUserFromToken(token)
    channel_id = int(request.args.get('channel_id'))

    joinChannel(data, int(channel_id), u_id)
    return sendSuccess({})


@APP.route('/channel/addowner', methods=['POST'])
def addOwner():
    token = request.form.get('token')
    checkTokenValidity(token, data)
    u_id = getUserFromToken(token)
    new_owner_u_id, channel_id = (request.form[x] for x in ('u_id', 'channel_id'))

    addOwnerToChannel(data, int(channel_id), u_id, int(new_owner_u_id))
    return sendSuccess({})

@APP.route('/channel/removeowner', methods=['POST'])
def removeOwner():
    token = request.form.get('token')
    checkTokenValidity(token, data)
    u_id = getUserFromToken(token)
    target_owner_u_id, channel_id = (request.form[x] for x in ('u_id', 'channel_id'))

    removeOwnerFromChannel(data, int(channel_id), u_id, int(target_owner_u_id))
    return sendSuccess({})

@APP.route('/channels/list', methods=['GET'])
def list():
    # Returns a list of all the PUBLIC and PRIVATE channels that the user is a member of.
    token = request.args.get('token')
    checkTokenValidity(token, data)
    u_id = getUserFromToken(token)

    return sendSuccess({'channels': channelList(data, u_id)})
      
@APP.route('/channels/listall', methods=['GET'])
def listAll():
    # Returns a list of all the PUBLIC channels (as well as PRIVATE channels if the user is a member of any).
    token = request.args.get('token')
    checkTokenValidity(token, data)
    u_id = getUserFromToken(token)

    return sendSuccess({'channels': channelListAll(data, u_id)})

@APP.route('/channels/create', methods=['POST'])
def createChannel():
    data = getData()
    token = request.form.get('token')
    checkTokenValidity(token, data)
    name, is_public = (request.form[x] for x in ('name', 'is_public'))

    checkTokenValidity(token, data)
    channelNameCheck(name)
    u_id = getUserFromToken(token)

    channel_id = channelsCreate(data, u_id, name, is_public)

    print(data['channels'])
    return sendSuccess({
        'channel_id': channel_id,
    })

@APP.route('/users/all', methods=['GET'])
def allUsers():
    data = getData()
    token = request.args.get('token')
    checkTokenValidity(token, data)
    
    return sendSuccess({
        'users': getAllUserNames(data),
    })

@APP.route('/user/profile', methods=['GET'])
def viewUserProfile():
    data = getData()
    u_id = int(request.args.get('u_id'))
    token = request.args.get('token')
    checkTokenValidity(token, data)

    profile = user_profile(data, token, u_id)
    return dumps(profile)

@APP.route('/user/profile/setname', methods=['PUT'])
def setName():
    data = getData()
    name_first, name_last, token = (request.form[x] for x in ('name_first', 'name_last', 'token'))

    checkTokenValidity(token, data)

    user_profile_setname(data, token, name_first, name_last)
    return sendSuccess({})

@APP.route('/user/profile/setemail', methods=['PUT'])
def setEmail():
    data = getData()
    email, token = (request.form[x] for x in ('email', 'token'))
    checkTokenValidity(token, data)

    user_profile_setemail(data, token, email)
    return sendSuccess({})

@APP.route('/user/profile/sethandle', methods=['PUT'])
def setHandle():
    data = getData()
    handle_str, token = (request.form[x] for x in ('handle_str', 'token'))
    checkTokenValidity(token, data)

    user_profile_sethandle(data, token, handle_str)
    return sendSuccess({})

@APP.route('/user/profile/uploadphoto', methods=['POST'])
def cropPhoto():
    data = getData()
    token = request.form.get('token')
    img_url = request.form.get('url')
    x_start = request.form.get('xstart')
    y_start = request.form.get('ystart')
    x_end = request.form.get('xend')
    y_end = request.form.get('yend')

    user_profile_uploadphoto(data, token, img_url, x_start, y_start, x_end, y_end)
    return sendSuccess({})


@APP.route('/search', methods=['GET'])
def searchMessage():
    data = getData()
    token = request.args.get('token')
    query_str = request.args.get('query_str')

    matched_mesg = search(data, token, query_str)
    return dumps(matched_mesg)


@APP.route('/admin/userpermission/change', methods=['POST'])
def changePermission():
    data = getData()
    u_id = int(request.form.get('u_id'))
    token = request.form.get('token')
    permission_id = int(request.form.get('permission_id'))
    checkTokenValidity(token, data)

    admin_userpermission_change(data, token, u_id, permission_id)
    return sendSuccess({})

@APP.route('/message/send', methods=['POST'])
def messageSend():
    message, channel_id = (request.form[x] for x in ('message', 'channel_id'))
    channel_id = int(channel_id)
    token = request.form.get('token')
    checkTokenValidity(token, data)
    message_id = message_send(data, message, channel_id, token)
    return dumps({'message_id': message_id})
    
@APP.route('/message/sendLater', methods=['POST'])
def messageSendLater():
    token = request.form.get('token')
    checkTokenValidity(token, data)
    message, channel_id, time_send = (request.form[x] for x in ('message', 'channel_id', 'time_sent'))
    message_send_later(data, message, channel_id, time_send, token)

    return dumps({})
    
@APP.route('/message/remove', methods=['DELETE'])
def removeMessage():
    token = request.form.get('token')
    checkTokenValidity(token, data)
    message_id = (request.form[x] for x in ('message_id'))
    remove_message(data, message_id, token)
    return dumps({})

@APP.route('/message/edit', methods=['PUT'])
def messageedit():
    data = getData()
    token = request.form.get('token')
    checkTokenValidity(token, data)
    newMessage, messageId = (request.form[x] for x in ('message', 'message_id'))
    editMessage(data, messageId, newMessage, token)
    return dumps({})

@APP.route('/message/react', methods=['POST'])
def messageReact():
    token = request.form.get('token')
    checkTokenValidity(token, data)
    messageId, reactId = (request.form[x] for x in ('message_id', 'react_id'))
    u_id = getUserFromToken(token)
    reactToMessage(data, messageId, reactId, token)
    return dumps({})



@APP.route('/message/unreact', methods=['POST'])
def messageUnreact():
    token = request.form.get('token')
    checkTokenValidity(token, data)
    messageId, reactId = (request.form[x] for x in ('message_id', 'react_id'))
    u_id = getUserFromToken(token)
    unreactMessage(data, messageId, reactId, token)
    return dumps({})


@APP.route('/message/pin', methods=['POST'])
def messagePin():
    data = getData
    token = request.form.get('token')
    checkTokenValidity(token, data)
    messageId = (request.form[x] for x in ('message_id'))
    pinMessage(data, token, messageId)

@APP.route('/message/unpin', methods=['POST'])
def messageUnpin():
    data = getData
    token = request.form.get('token')
    checkTokenValidity(token, data)
    messageId = (request.form[x] for x in ('message_id'))
    unpinMessage(data, token, messageId) 

@APP.route('/standup/active', methods=['GET'])
def standupActive():
    # STUB
    is_active = None 
    time_finish = None
    return sendSuccess({
        'is_active': is_active,
        'time_finish': time_finish,
    })

@APP.route('/standup/start', methods = ['POST'])
def standupStart():
    data = getData()
    token = request.form.get('token')
    checkTokenValidity(token, data)
    channel_id = int(request.form.get('channel_id'))
    time_finish = standupStartFunc(data, token, channel_id)
    return sendSuccess({time_finish})


@APP.route('/standup/send', methods = ['POST'])
def standupSend():
    data = getData()
    token = request.form.get('token')
    checkTokenValidity(token, data)
    message = request.form.get('message')
    channel_id = int(request.form.get('channel_id'))
    standupSendFunc(data, token, channel_id, message)
    return sendSuccess({})


if __name__ == '__main__':
    APP.run(port=(sys.argv[1] if len(sys.argv) > 1 else 5000))

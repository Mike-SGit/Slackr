import datetime
import time, threading
from messages_helper import message_send
from auth_register_helper import getUserFromToken
from threading import Timer
from errors import AccessError

def standupStillActive (data, channel_id, u_id):
    for channel in data['channels']:
        if str(channel_id) == str(channel['channel_id']):
            if channel['standup_active'] and channel['standup_end'] > datetime.datetime.now():
                return True
            else:
                print(channel['standup_active'])
    return False

def standupNotActive (data, channel_id, u_id):
    for channel in data['channels']:
        if str(channel_id) == str(channel['channel_id']):
            if channel['standup_active'] is False:
                return True
    return False

def standupTerminate (data, channel_id, token, endTime):
    for channel in data['channels']:
        if str(channel_id == channel['channel_id']):
            channel['standup_active'] = False
    time.sleep(15*60)

def standupEnd (data, channel_id, token, finish):
    u_id = getUserFromToken(token)
    for channel in data['channels']:
        if str(channel_id == channel['channel_id']):
            standupEndTime = channel['standup_end'] - datetime.datetime.now()
            if (channel['standup_active'] is True):
                standupTerminate(data, channel_id, token, standupEndTime)
                message = channel['standup_messages']
                message_send(data, message, channel_id, token)

def checkTokenValidity(token, data):
    if token in data['tokens']:
        if getUserFromToken(token) is not None:
            return True
    else:
        raise AccessError('Invalid Token!')
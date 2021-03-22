import datetime
import time, threading
from messages import post_message

def standupStillActive (data, channel_id, u_id):
    for channel in data['channels']:
        if channel_id == channel['channel_id']:
            if channel['standup_active'] and channel['standup_end'] < datetime.datetime.now():
                return True
            else:
                return False
    return False

def standupNotActive (data, channel_id, u_id):
    data['channels']['channel_id']['standup_active'] = False

def standupEnd (data, channel_id, u_id, finish):
    threading.timer(finish, standupNotActive (data, channel_id, u_id)).start()
    post_message(data['channels']['channel_id']['standup_message'], channel_id)
    
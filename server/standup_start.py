import datetime


def standup_start(token, channel_id):
    
    now = datetime.datetime.now()
    finish = now + datetime.timedelta(minutes = 15)
    
    return {
        'time_finish': finish,
    }



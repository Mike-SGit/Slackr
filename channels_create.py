from random import randrange
CHANNEL_NAME_MAX_LEN = 20

def createC_ID(data):
	# Creating channel_id that resembles: C123456
	channel_id = randrange(100000)
	for channels in data['channels']:
		while channel_id == channels['channel_id']:
			channel_id = randrange(100000)
	return int(channel_id)

def channelsCreate(data, u_id, name, is_public):
    channel_id = createC_ID(data)

    data['channels'].append({
        'is_public': is_public, 
        'channel_id': channel_id,
        'name': name,
        'channel_owners': {
            'original_owner': u_id, # A variable containing only one u_id, that being the owner's. 
            'owners': [u_id], # A list of u_id's that correspond to channel owners, this includes the originalOwner.
        },
        'members': [int(u_id)],
        'standup_active' : False,
        'standup_end': 0,
        'standup_messages': [],
        'messages': [],
    })

    return channel_id

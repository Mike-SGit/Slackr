def channelList(data, u_id):
    returnList = []
    for channel in data['channels']:
        if u_id in channel['members']: 
            positiveChannel = {
                'channel_id': channel['channel_id'],
                'name': channel['name'],
            }
            returnList.append(positiveChannel)
    return returnList

def channelListAll(data, u_id):
    returnList = []
    for channel in data['channels']:
        if channel['is_public'] is True or u_id in channel['members']:
            positiveChannel = {
                'channel_id': channel['channel_id'],
                'name': channel['name'],
            }
            returnList.append(positiveChannel)
    return returnList
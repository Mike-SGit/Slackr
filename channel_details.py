def getDetails(data, channel_id):
    for channel in data['channels']:
        if channel_id == channel['channel_id']:
            return {
                'name': channel['name'],
                'owner_members': channel['channel_owners'],
                'all_members': channel['members'],
                }

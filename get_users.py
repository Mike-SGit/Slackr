def getAllUserNames(data):
    names = []
    for user in data['users']:
        names.append(user['handle'])
    return names
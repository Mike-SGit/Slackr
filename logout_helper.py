from invalidate_token import invalidateToken

def logoutFunc(data, token):
    if token in data['tokens']:
        data['tokens'] = invalidateToken(token, data['tokens'])
        return True
    return False
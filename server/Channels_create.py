from Channels_list import invalid_token

def Channels_create (token, name, is_public):
    if invalid_token(token):
        raise ValueError ("Invalid token")
    else:
        if len(name) > 20:
            raise ValueError ("Name is longer than 20 char")
        else:
            #do something
            pass
    
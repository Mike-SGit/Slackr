from auth_register_helper import checkEmail, getUserFromToken
from errors import AccessError, ValueError
from json import dumps

'''
Given a query string, return a collection of messages in all of the channels 
that the user has joined that match the query
'''

def search(data, token, query_str):
    # Decode token to match user
    u_id = getUserFromToken(token)

    matched_mesg = {
        'messages': []
    }

    for ser_chan in data['channels']:
        # Check if user in the channel
        if str(u_id) in str(ser_chan['members']):

            # Find matched message
            # ser_mesg['message'] is the content of a message
            for ser_mesg in ser_chan['messages']:
                raise AccessError('2nd')
                # Match found
                if query_str in ser_mesg['message']:
                    matched_mesg['messages'].append(ser_mesg)

    return matched_mesg
    


    
    






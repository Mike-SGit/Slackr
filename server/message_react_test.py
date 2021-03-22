from message_react import message_react
from message_remove import message_remove
from message_send import message send
from auth_register import auth_register
from channels_create import channels_create
import pytest   

def test_message_reactFAILfalseReactID():
    ## set up
    AuthRegDict = auth_register("haydo@gmail.com", "123456", "Hayden", "Smith")
    token = AuthRegDict['token']
    AuthRegDict2 = auth_register("haydo1@gmail.com", "1123456", "Hayen", "Sith")
    token2 = AuthRegDict['token']
    publicChan = channels_create(token, "public", True)
    publicId = publicChan['channel_id']
    
    message_send(token, publicId, "message one")
    messageDic = channel_messages(token, publicChan, 0)
    ###messageDic{ message_id, u_id, message, time_created, is_unread }
    firstId = messageDic[message_id][0]
    firstMessage = messageDic[message][0]
    ## set up done
    badReact_id = "Bad react id 123#"
    
    with pytest.raises(AccessError, match=r"*"):
        message_react(token, firstId, badReact_id)
    
    


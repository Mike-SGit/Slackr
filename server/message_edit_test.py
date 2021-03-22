from message_edit import message_edit
from message_remove import message_remove
from message_send import message send
from auth_register import auth_register
from channels_create import channels_create
import pytest   
    
def test_message_edit():
    ## set up
    AuthRegDict = auth_register("haydo@gmail.com", "123456", "Hayden", "Smith")
    token = AuthRegDict['token']

    publicChan = channels_create(token, "public", True)
    publicId = publicChan['channel_id']
    ## end setup
    
    
    message_send(token, publicId, "message one")
    messageDic = channel_messages(token, publicChan, 0)
    ###messageDic{ message_id, u_id, message, time_created, is_unread }
    firstId = messageDic[message_id][0]
    firstMessage = messageDic[message][0]
    ## end setup
    message_edit(token, firstId, "edited message one")
    
    messageDic1 = channel_messages(token, publicChan, 0)
    ###messageDic{ message_id, u_id, message, time_created, is_unread }
    editFirstId = messageDic[message_id][0]
    editFirstMessage = messageDic[message][0]
    assert editFirstMessage == "edit message one"
    assert editFirstId == firstId
    
    
def test_message_editFAILeditOthers():
    ## set up
    AuthRegDict = auth_register("haydo@gmail.com", "123456", "Hayden", "Smith")
    token = AuthRegDict['token']
    AuthRegDict2 = auth_register("haydo1@gmail.com", "1123456", "Hayen", "Sith")
    token2 = AuthRegDict['token']
    publicChan = channels_create(token, "public", True)
    publicId = publicChan['channel_id']
    ## end setup
    
    
    message_send(token, publicId, "message one")
    messageDic = channel_messages(token, publicChan, 0)
    ###messageDic{ message_id, u_id, message, time_created, is_unread }
    firstId = messageDic[message_id][0]
    firstMessage = messageDic[message][0]
    ## end setup
    with pytest.raises(AccessError, match=r"*"):
        message_edit(token2, firstId, "edited message one")
    
    messageDic1 = channel_messages(token, publicChan, 0)
    ###messageDic{ message_id, u_id, message, time_created, is_unread }
    editFirstId = messageDic[message_id][0]
    editFirstMessage = messageDic[message][0]
    assert editFirstMessage == "message one"
    assert editFirstId == firstId
    

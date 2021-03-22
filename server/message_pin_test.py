from message_pin import message_pin
from message_remove import message_remove
from message_send import message send
from auth_register import auth_register
from channels_create import channels_create
import pytest   



def test_message_pin():
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

   
    message_pin(token, firstId)

def test_message_pinFAILalreadyPinned():
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
    message_pin(token, firstId)
    
    with pytest.raises(AccessError, match=r"*"):
        message_pin(token, firstId)



def test_message_pinFAILnotAdmin():
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

    with pytest.raises(AccessError, match=r"*"):
        message_pin(token, firstId)
    message_pin(token2, firstId)



def test_message_pinFAILinvalidMessage():
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
    fakeId = "asdfg123#"
    firstMessage = messageDic[message][0]
    ## set up done

    with pytest.raises(AccessError, match=r"*"):
        message_pin(token, fakeId)


def test_message_pinFAILadminNotInChan():
    ## set up
    AuthRegDict = auth_register("haydo@gmail.com", "123456", "Hayden", "Smith")
    token = AuthRegDict['token']
    AuthRegDict2 = auth_register("haydo1@gmail.com", "1123456", "Hayen", "Sith")
    token2 = AuthRegDict['token']
    publicChan = channels_create(token2, "public", True)
    publicId = publicChan['channel_id']
    
    message_send(token2, publicId, "message one")
    messageDic = channel_messages(token2, publicChan, 0)
    ###messageDic{ message_id, u_id, message, time_created, is_unread }
    firstId = messageDic[message_id][0]
    firstMessage = messageDic[message][0]
    ## set up done

    with pytest.raises(AccessError, match=r"*"):
        message_pin(token, firstId)

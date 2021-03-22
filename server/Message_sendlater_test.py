from errors import AccessError, ValueError
import pytest
from message import message_send
from message_send_test import *

def Message_sendlater_test():
    # Begin setup
    auth_user1_dict = auth_register("random@gmail.com", "user1", "random", "rand")
    user1_token = auth_user1['token']
    # End setup

    #standard delayed message procedure
    channel_id1 = channel_create(user1_token, 'test', True)
    Message_sendlater(user1_token, channel_id1, "hello", datetime(2019/10/7/00/00))

    #invalid channel id
    with pytest.raises(ValueError, match = r"*"):
        Message_sendlater(user1_token, channel_id1, "hello", datetime(2019/10/7/00/00))   

    user3_token = 'invalid token'

    #invalid token
    with pytest.raises(ValueError, match = r"*"):
        Message_sendlater(user3_token, channel_id1, "hello", datetime(2019/10/7/00/00)) 

    ##insert test with 1000 char message during iteration 2
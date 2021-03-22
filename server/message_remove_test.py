from errors import AccessError, ValueError
import pytest
from message import message_send
from message_send_test import *


def test_message_removeFirstMessage():
    message_remove(token, 'U64567M0001')

def test_message_remove_wrong_messageid():
    with pytest.raises(AccessError, match=r"*"):
        message_remove(token, 'U64567M0011')
    
def test_message_remove_unautorised_user():
    with pytest.raises(AccessError, match=r"*"):
        message_remove(token2, 'U64567M0001')

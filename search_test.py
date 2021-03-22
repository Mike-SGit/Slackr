from search import search
from errors import AccessError, ValueError
from test_data import *
import pytest 




def test_search_01():
    matched_mesg = {
        'messages': ['Hello my name is Sherry!', 'Hello my name is Chris!', 'Hello again Im Sherry!']
    }
    a = search(data, token, "again Im Sher")
    expected = "{'messages': [{'message_id': 'M0001', 'u_id': '57946', 'message': 'Hello again Im Sherry!', 'time_created': None, 'reacts': [{'react_id': 0, 'u_id': None, 'is_this_user_reacted': 0}], 'is_pinned': 0}]}"
    assert str(a) == expected
    

def test_search_02():
    matched_mesg = {
        'messages': ['Hello my name is Sherry!', 'Hello again Im Sherry!']
    }
    assert str(search(data, token, 'herr')) == "{'messages': [{'message_id': 'M0001', 'u_id': '57946', 'message': 'Hello my name is Sherry!', 'time_created': None, 'reacts': [{'react_id': 0, 'u_id': None, 'is_this_user_reacted': 0}], 'is_pinned': 0}, {'message_id': 'M0001', 'u_id': '57946', 'message': 'Hello again Im Sherry!', 'time_created': None, 'reacts': [{'react_id': 0, 'u_id': None, 'is_this_user_reacted': 0}], 'is_pinned': 0}]}"
    # b = search(data, token, 'herr')
    # print(b)
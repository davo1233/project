from src.data_interface import read_data, write_data
from src.error import AccessError, InputError
from src.auth import decode_token
import os
import glob
import time

def clear_v1():
    '''
    Clears all application data and resets application data to its initial state 

    Arguments:
        None
    
    Exceptions:
        None

    Return Value:
        None
    '''
    

def search_v1(token, query):
    '''
    Given a query string, return a collection of messages in all of the channels/DMs
    that the user has joined that match the query

    Arguments:
        auth_user_id (int)      id of user requesting search
        query (string)          query string to use for search

    Exceptions:
        AccessError             user id passed is invalid
        InputError              query string is above 1000 characters

    Return Value:
        {'messages': [{}]}      list of dictionaries where each dictionary contains
                                types {message_id, u_id, message, time_created}
    '''
    

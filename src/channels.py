from src.data_interface import read_data, write_data
from src.error import AccessError, InputError
from src.auth import decode_token
import time

def channels_list_v1(token):
    '''
    Returns a dictionary containing a list of dictionaries of channels and their
    id's and names that the authorised user is part of.

    Arguments (1):
        auth_user_id - int value of ID of user requesting list of channels

    Returns (1):
        {'channels' : channels_list} - dictionary with one entry with key 'channels'
        and value containing a list of dictionaries containing channel entries
        'channel_id' and corresponding 'name'

    Exceptions (1):
        Raises an Access Error if invalid user ID is passed as argument
    '''
   return {}

    


def channels_listall_v1(token):
    '''
    Returns a dictionary containing a list of dictionaries of channels and their
    id's and names of all existing channels. This includes Private channels

    Arguments (1):
        auth_user_id - int value of ID of user requesting list of channels

    Returns (1):
        {'channels' : channels_list} - dictionary with one entry with key 'channels'
        and value containing a list of dictionaries containing channel entries
        'channel_id' and corresponding 'name'

    Exceptions (1):
        Raises an Access Error if invalid user ID is passed as argument
    '''
    return {}


def channels_create_v1(token, name, is_public):
    '''
    Creates a new channel and assigns the appropriate data to it within the
    stored data. Returns the id of the channel. The creator of the channel
    will be automatically added as an owner member of the channel

    Arguments (3):
        - auth_user_id - int value of ID of user requesting channel creation
        - name - str value of proposed channel name
        - is_public - boolean to determine if channel created is Private or Public

    Returns (1):
        {'channel_id' : channel_id} - dictionary containing one entry with key
        'channel_id' and value equal to the ID of the channel created

    Exceptions (3):
        - Raises an Access Error if invalid user ID is passed as argument
        - Raises an Input Error if channel name is over 20 characters
        - Raises an Input Error if channel name is already taken
    '''
    
    return {}

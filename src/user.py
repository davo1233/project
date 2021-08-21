import re
import requests
from urllib.request import urlretrieve
from PIL import Image
from pathlib import Path

from src import config
from src.auth import decode_token,create_token
from src.data_interface import read_data, write_data
from src.error import AccessError, InputError

MIN_PASSWORD_LENGTH = 6
MIN_NAME_LENGTH = 0
MAX_NAME_LENGTH = 50
MAX_HANDLE_LENGTH = 20
MIN_HANDLE_LENGTH = 3

def user_profile_v1(token, u_id):
    """
    Returns the details of the user that contains the relevant u_id and token

    Args:
        token: The encoded token that contains the session id
        u_id: The id that matches the user to be found

    Returns:
        A user's details is returned in a dictionary named 'user'.
        'user': {
            'u_id': u_id,
            'email': 'email',
            'name_first': 'name_first',
            'name_last': 'name_last',
            'handle_str': 'handle_str',
        }

    Exceptions:
        InputError occurs if:
            The u_id is invalid or not found.

    """


    

def user_profile_setname_v1(token, name_first, name_last):
    """
    Changes the first name and the last name of a user that matches the token

    Args:
        token: Token of the user
        name_first: User's new first name
        name_last: User's new last name

    Returns:
        An empty dictionary.
        For example:
        {}

    Exceptions:
        InputError occurs if:
            the first and last name is not between 1 and 50 char long.

    """
   

def user_profile_setemail_v1(token, email):
    """
    Modify the user's email address.

    Args:
        email: The user's new email
        token: The token that contains the session id and u_id of the user

    Returns:
        An empty dictionary. 
        For example: 
        {}

    Exceptions:
        InputError occurs if:
            the email is invalid.

    """
   
def user_profile_sethandle_v1(token, handle_str):
    """
    Handles the user's handle

    Args:
        token: The token that contains the session id and u_id of the user
        handle_str: the user's handle

    Returns:
        An empty dictionary. 
        For example: 
        {}

    Exceptions:
        InputError occurs if:
            the handle_str is invalid.

    """
    

def user_profile_uploadphoto_v1(token, img_url, x_start, y_start, x_end, y_end):
   

def user_stats_v1(token):
    
import re
import time
import random
import hashlib
import jwt
import smtplib
#from src.data_interface import read_data, write_data
from src.error import InputError,AccessError
from src import config


SECRET = 'NANQISPENSERWILLIAMWILLIAM'

def encrypted_password(password):
    """
    Converts a password of type string into a sha256 encrypted string. 

    Args:
        password: A password that is entered by the user when logging in or registering. 

    Returns:
        A hashed password is returned.
        The sha256 encrypted password is stored as a string. For example:
        {encoded_password: 9d52fc15395c9b1f3a87d160e89018c6946409ef0f4c69f89e60a7bed74df5c9}
    Exceptions:
        N/A

    """
    return hashlib.sha256(password.encode()).hexdigest()

def create_token(session_id):
    """
    Generates a token from the session id. Returns a token of type string.

    Args:
        session_id: the session id generated from either auth_login or auth_register 

    Returns:
        A token is returned which stores the login session id for the relevant user.
        The token is stored as a string. For example:
        {token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c}
    Exceptions:
        N/A

    """
    return jwt.encode({'session_id': session_id}, SECRET,algorithm = 'HS256')

def decode_token(token):
    """
    Decodes a token from the session id. Returns a dictionary containing 
    both session_id and user_id
    Args:
        token: an encrypted string that contains the payload of session_id

    Returns:
        A dictionary is returned containing:
            session_id: the session id generated from each registration or login of each user
            user_id: id assigned to each user that registers
        Both session_id and user_id return and int. For example:
        {'session_id': 3,'user_id': 2}
        
    Exceptions:
        AccessError occurs if:
            The tokens do not match.
            IF the auth_user_id is invalid. 

    """


    return  {
    }

def auth_login(email, password):
    """
    Handles the user login.

    Retrieves an email and password from a dictionary when entered by a user 
    and when successful returns an user id.

    Args:
        email: The string of the user's email
        password: The string of the user's password

    Returns:
        An auth_user_id that represents the contents pertaining to that user.
        The auth_user_id is stored as an integer. For example:

        {auth_user_id: 1}
        A token is returned which stores the login session id for the relevant user.
        The token is stored as a string. For example:
        {token: sfjodhf238472304780hoHLHlF}
    Exceptions:
        InputError occurs if:
            the password is incorrect.
            the email entered does not belong to a user.
            the email is invalid.

    """


    return {
    }

def auth_register(email, password, name_first, name_last):
    """
    Handles the user registration details.
    Uses a dictionary to store the registration details.

    Args:
        email: The user's email
        password: The user's password
        name_first: User's first name
        name_last: User's last name

    Returns:
        An auth_user_id that represents the contents pertaining to that user.
        The auth_user_id is stored as an integer. For example:
        {auth_user_id: 1}

    Exceptions:
        InputError occurs if:
            the password is less than 6 characters long.
            the email entered is already being used.
            the email is invalid.
            the first and last name is not between 1 and 50 char long.

    """
    
    return{} 
    

def auth_logout(token):
    """
    Handles the logout by deleting the tokenised session id. 

    Args:
        token: The encoded session_id of the relevant user

    Returns:
        A true or false boolean depending on whether or not the logout has been successful
        For example {is_success: True}
    Exceptions: 
        N/A

    """
    #if the token does not exist in the session id list return false
    #when a matching decoded token is found then remove the session id from the session id dictionary
    #function will never be able to return false since error always raised

def auth_passwordreset_request(email):
    """
    Sends an email with a recovery reset code.

    Args:
        email: The email of the user

    Returns:
        An empty dictionary.
    Exceptions: 
        N/A

    """
    return {}


def auth_passwordreset_reset(reset_code,new_password):
    """
    Resets the password for the user with a valid reset code. 

    Args:
        reset_code: The reset code received in the user's email.
        new_password: The desired password from the user. 

    Returns:
        An empty dictionary.
    Exceptions: 
        InputError occurs if:
            the password is less than 6 characters long.
            there is an invalid reset code. 

    """
    

    
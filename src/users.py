from src.auth import decode_token,create_token
from src.data_interface import read_data, write_data
from src.error import AccessError

def users_all(token):
    """
    Returns the details of the user every user if a valid token is entered.

    Args:
        token: The encoded token that contains the session id
        u_id: The id that matches the user to be found

    Returns:
        All users' details are returned in a list that contains each user's details.
        For example:

        {'users': [
        {
            'u_id': 0,
            'email': 'nanqichen@gmail.com',
            'name_first': 'Nanqi',
            'name_last': 'Chen',
            'handle_str': 'nanqichen',
        },
        {
            'u_id': 1,
            'email': 'williammorphett@gmail.com',
            'name_first': 'William',
            'name_last': 'Morphett',
            'handle_str': 'williammorphett',
        },
        {
            'u_id': 2,
            'email': 'gazza69@gmail.com',
            'name_first': 'Gary',
            'name_last': 'Zhang',
            'handle_str': 'garyzhang',
        },]
        }

    Exceptions:
        InputError occurs if:
            N/A

    """
   

def users_stats(token):
    

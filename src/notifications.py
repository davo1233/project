from src.data_interface import read_data, write_data
from src.error import AccessError, InputError
from src.auth import decode_token

def notifications_get_v1(token):
    '''
    Description:
    This function will return a users 20 most recent notifications in the form of a list of dictionaries
    where each dictionary contains types {channel_id, dm_id, notification_message}.
    The list is ordered from most to least recent
    
   
    Arguments:
    auth_user_id - ID of user whose notifications are being returned
        
    Returns:
    notifications - A list of dictionaries containing types {channel_id, dm_id, notification_message}
                    channel_id is -1 if the event happened in a dm and vice versa for dm_id
                    If there are no notifications the function will return an empty list

    Exceptions:
    InputError - If an invalid auth_user_id is input 
    '''
    
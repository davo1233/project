from src.data_interface import read_data, write_data
from src.error import AccessError, InputError
from src.auth import decode_token
import time

def add_user_to_channel(user_id, channel_id, data):
    

def create_reacts_list(auth_user_id, message_id):
    

    return react_list

def channel_invite_v1(token, channel_id, u_id):
    '''
    Invites a user to join a channel. The invited user is immediately added
    to the channel if the inviting user is already a member of the channel. 

    Arguments:
        auth_user_id (int)    id of inviting user
        channel_id (int)      id of channel
        u_id (int)            id of user being invited
    
    Exceptions:
        InputError  - channel_id or u_id is invalid
        AccessError - auth_user_id invalid, 
                      inviting user is not a member of the channel already

    Return Value:
        Returns empty dictionary 
    '''
    
    data = read_data()
    
    

    add_user_to_channel(u_id, channel_id, data)
    write_data(data)

    return {
    }

def channel_details_v1(token, channel_id):
    '''
    Description:
    This function returns a dictionary with keys that are the name, owner_members and all_members of a specific channel. 
   

    Inputs:
    auth_user_id - id of a user
    channel_id - id of a channel
    
    Outputs:
    channel_details - dictionary with keys that the name, owner_members and all_members of a specific channel.
                        The name is the name of the channel, owner_members is a list of the owners in the channel,
                        all_members is a list of the members in the channel.

    Exceptions:
    Raises an InputError if the channel ID is not a valid channel
    Raises an AccessError if user is not a member of the channel with channel_id
    '''
    
   

    return {}

def channel_messages_v1(token, channel_id, start):
    '''
    Description:
    This function returns a dictionary of messages from a specific channel. 

    Inputs:
    auth_user_id - id of a user
    channel_id - id of a channel
    start - starting position of messages in channel
    
    Outputs:
    message_details - dictionary with keys that the name, owner_members and all_members of a specfic channel.

    Exceptions:
    Raises an InputError if the channel ID is not a valid channel
    Raises an InputError if the start input is larger than the amount of messages
    Raises an AccessError if user is not a member of the channel with channel_id
    '''
    
    data = read_data()

    
    
def channel_leave_v1(token, channel_id):
    '''
    Removes a user from the given channel. Messages sent by the user will 
    be retained. 

    Arguments:
        auth_user_id (int)    id of user to be removed
        channel_id (int)      id of channel
    
    Exceptions:
        InputError  - channel_id is invalid
        AccessError - auth_user_id is invalid, 
                      inviting user is not a member of the channel already

    Return Value:
        Returns empty dictionary 
    '''

    
    return {
    }

def channel_join_v1(token, channel_id):
    '''
    Adds an authorised user to a channel if they are permitted to join. 
    Global owners are permitted to join any channel, public or private
    while global members are only allowed to join public channels. 

    Arguments:
        auth_user_id (int)    id of user seeking to join channel
        channel_id (int)      id of channel
    
    Exceptions:
        InputError  - channel_id is invalid
        AccessError - auth_user_id is invalid,
                      global member attempts to join private channel

    Return Value:
        Returns empty dictionary 
    '''
    
    
    
    return {
    }

def channel_addowner_v1(token, channel_id, u_id):
    '''
    Makes a nominated user an owner of the channel if the authorised user is a
    channel owner or a global owner. 

    Arguments:
        auth_user_id (int)    id of user granting owner permissions
        channel_id (int)      id of channel
        u_id (int)            id of user being made an owner
    
    Exceptions:
        InputError  - channel_id or u_id is invalid,
                      u_id is already an owner of the channel
        AccessError - auth_user_id is invalid,
                      authorised user is not a channel owner or global owner

    Return Value:
        Returns empty dictionary 
    '''
    
    return {
    }

def channel_removeowner_v1(token, channel_id, u_id):
    '''
    Removes a nominated owner of the channel if the authorised user is a
    channel owner or a global owner. 

    Arguments:
        auth_user_id (int)    id of user removing owner permissions
        channel_id (int)      id of channel
        u_id (int)            id of user being removed as an owner
    
    Exceptions:
        InputError  - channel_id or u_id is invalid,
                      u_id is not already an owner of the channel,
                      u_id is the only owner of a channel
        AccessError - auth_user_id is invalid,
                      authorised user is not a channel owner or global owner

    Return Value:
        Returns empty dictionary 
    '''
    

    return {
    }

from src.data_interface import read_data, write_data
from src.error import AccessError, InputError
from src.auth import decode_token
import time
from src.channel import create_reacts_list

def create_dm_name(dm_id):
    '''
    Returns a name created from the handle strings of the members of the
    DM provided
    '''
    
    return dm_name

def add_dm_notification(adder_id, dm_id, u_id):
    '''
    Create notification that adder has added user to DM
    '''


    return data

def dm_details_v1(token, dm_id):
    '''
    Returns the name of the specified DM and its members

    Arguments:
        auth_user_id (int)      ID of user calling function
        dm_id (int)             ID of DM that user is referring to

    Exceptions:
        AccessError             user is not a member of the specified dm
                                or user is not a valid user
        InputError              dm_id is not a valid DM ID

    Return Value:
    {
        name,                   name of DM
        members                 list of details of user members in DM
    }         
    '''
    data = read_data()
    

    return {
        'name': dm_name,
        'members': member_details
    }

def dm_list_v1(token):
    '''
    Returns a list of DMs that the user is a member of

    Arguments:
        auth_user_id (int)      ID of user calling function

    Exceptions:
        AccessError             user is not a valid user

    Return Value:
        {dms}                   list of dictionaries where each dictionary
                                contains types {dm_id, dm_name}
    '''


    return {}

def dm_create_v1(token, u_ids):
    '''
    Creates a DM between creator and included users. DMs can exist with the
    same name but must have different IDs. Creator can create DM with
    themselves by passing empty list as u_ids

    Arguments:
        auth_user_id (int)      ID of user calling function. They are
                                automatically marked as the original creator
                                of the DM
        u_ids (list of int)     list of user IDs to be added to the DM

    Exceptions:
        AccessError             user is not a valid user
        InputError              any u_id in u_ids is not a valid user

    Return Value:
    {
        dm_id,                  ID of created DM
        dm_name                 name of created DM will be an alphabetically
                                sorted, comma-separated combination of the
                                handles of the DM's members
    }        
    '''
   

    # Return DM ID and DM name created
    return {

    }

def dm_invite_v1(token, dm_id, u_id):
    '''
    Invites a user to join a DM. The invited user is immediately added to
    the DM if the inviting user is already a member of the DM. The name of
    the DM will be automatically changed to account for the new member

    Arguments:
        auth_user_id (int)      ID of inviting user
        dm_id (int)             ID of DM that user is being invited into
        u_id (int)              ID of user being invited. If user was the
                                original creator of the DM, they will be 
                                reinstated as such. If user is already a
                                member of the DM, this function will do
                                nothing

    Exceptions:
        AccessError             user is not a valid user or user is not a
                                member of the DM
        InputError              dm_id is not a valid DM ID or
                                u_id is not a valid user ID
    
    Return Value:
        {}                      Empty dictionary
    '''
    

    return {}

def dm_leave_v1(token, dm_id):
    '''
    Removes the user as a member of the given DM

    Arguments:
        auth_user_id (int)      ID of user calling quits
        dm_id (int)             ID of DM that user wants to leave

    Exceptions:
        AccessError             user is not a valid user or user is not a
                                member of the DM
        InputError              dm_id is not a valid DM ID

    Return Value:
        {}                      Empty dictionary
    '''
    

    return 

def dm_remove_v1(token, dm_id):
    '''
    Remove an existing DM. This can only be done by the original creator
    of the DM

    Arguments:
        auth_user_id (int)      ID of user calling function
        dm_id (int)             ID of DM that user is referring to

    Exceptions:
        AccessError             user is not a valid user or user is a member
                                of or the original creator of the DM
        InputError              dm_id is not a valid DM ID

    Return Value:
        {}                      Empty dictionary
    '''
    
    return {}

def dm_messages_v1(token, dm_id, start):
    '''
    Return up to 50 messages between index 'start' and 'start + 50' using
    pagination behaviour. Message with index 0 is the most recent message

    Arguments:
        auth_user_id (int)      ID of user calling function
        dm_id (int)             ID of DM that user is referring to
        start (int)             starting index to return messages from

    Exceptions:
        AccessError             user is not a valid user or user is not a
                                member of the DM
        InputError              dm_id is not a valid DM ID or
                                start is greater than or equal to the 
                                total number of messages in the DM. The
                                exception is when there are no messages in
                                the DM and start '0' is called

    Return Value:
    {
        messages,               list of dictionaries where each contains
                                types {id, u_id, message, time_created}
        start,                  index start of returned messages
        end                     index end of returned messages. Value is
                                'start + 50' or '-1' if function has
                                returned the oldest messages in the DM
    }
    '''
   

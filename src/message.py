from src.data_interface import read_data, write_data
from src.error import AccessError, InputError
from src.auth import decode_token
from src.standups import message_to_standup, START_STR
import time
import threading

def add_dm_message_notification(auth_user_id, dm_id, message):
    '''
    Generate notifications if a user is tagegd in a dm message
    '''
    

def add_channel_message_notification(auth_user_id, channel_id, message):
    '''
    Generate notification if a user is tagged in a channel message
    '''
   

def create_reacts_dict():
    '''
    Generate the dictionary of dictionaries with types {react_id, u_ids} where 
    react_id are the id's of current reacts and u_ids is a list of users id's
    of people who have reacted with that react
    '''
   

def add_channel_react_notif(auth_user_id, channel_id, message_id):
    '''
    Generate notification if a user reacts to a channel message
    '''
    

def add_dm_react_notif(auth_user_id, dm_id, message_id):
    '''
    Generate notification if a user reacts to a dm message
    '''


def delayed_channel_message(auth_user_id, message_id, channel_id, message):
    
    

def delayed_dm_message(auth_user_id, message_id, dm_id, message):
    
    

def message_send_v1(token, channel_id, message):
    '''
    Description:
    This function sends a message from an authorised user to the channel specified by channel_id.
    Each message has a unique id even across channels.

    Arguments:
    auth_user_id - ID of user sending message
    channel_id - ID of channel receiving message 
    message - String of message being sent

    Returns:
    message_id - Unique ID of message created

    Exceptions:
    InputError - when a message is more than 1000 characters
    InputError - if any of the arguments are invalid inputs
    AccessError - when authorised user is not a member of the channel they are trying to post to 
    '''
    

    # Create new message dictionary
  


def message_remove_v1(token, message_id):
    '''
    Description:
    This function removes a message given by the message_id 
    from the channel it is contained in. 
    This can only be done by the user who sent the message, 
    the owner of the channel or DM and Dreams owners.

    Arguments:
    auth_user_id - ID of user calling the function
    message_id - ID of the message being removed

    Returns:
    {} - An empty dictionary

    Exceptions:
    InputError - when message_id no longer exists
    InputError - if any of the arguments are invalid inputs
    AccessError - if the user calling the function did not create the message
    AccessError - if the user calling the function is not the owner of the channel the message is in
                    (if the message is in a channel) or if the user is not an owner of the Dreams

    '''
    

    return {
    }


def message_edit_v1(token, message_id, message):
    '''
    Description:
    This function allows a user to update a message with new text.
    If the new text is an empty string the message is deleted.
    This can only be done 

    Arguments:
    auth_user_id - ID of user calling the function
    message_id - ID of the message being updated
    message - string of the updated text of the message

    Returns:
    {} - An empty dictionary

    Exceptions:
    InputError - when the length of the new message is over 1000 characters 
    InputError - if any of the arguments are invalid inputs
    AccessError - if the user calling the function did not create the message
    AccessError - if the user calling the function is not the owner of the channel the message is in
                    (if the message is in a channel) or if the user is not an owner of the Dreams
    '''
    
    
    


def message_share_v1(token, og_message_id, message, channel_id, dm_id):
    '''
    Description:
    This function allows a user to share a message to a specified channel or DM.
    The user can also send an optional message in addition to the shared message.
    
    Arguments:
    auth_user_id - ID of user sharing the message
    og_message_id - ID of the message being shared
    message - string of the optional message
                If this is an empty string no message will be added
    channel_id - ID of the channel the message is being shared to 
                If this value is -1 the message is being shared to a DM
    dm_id - ID of the DM message is being shared to 
                If this value is -1 the message is being shared to a channel

    Returns:
    shared_message_id - ID of the shared message

    Exceptions:
    InputError - if any of the arguments input are invalid
    AccessError - when the user is not a part of the channel or DM they are 
                    trying to share the message to
    '''
    


def message_senddm_v1(token, dm_id, message):
    '''
    Description:
    This function allows a user to send a message to a specified DM.
    Each message will have a unique ID even across channels and DM's
   
    Arguments:
    auth_user_id - ID of user who is sending the message
    dm_id - ID of DM the message is being sent to
    message - string of the message being sent
    
    Returns:
    message_id - ID of the message sent

    Exceptions:
    InputError - when the message sent is more than 1000 characters 
    InputError - if any of the arguements are invalid inputs
    AccessError - when the user is not a member of the DM they are trying to send to

    '''
    
    
   

def message_sendlater_v1(token, channel_id, message, time_sent):
    '''
    This function allows a user to send a message to a channel with channel_id
    automatically at a specified time in the future
       
    Arguments:
        token (JWT)         JWT token of user who is sending the message
        channel_id (int)    ID of channel the message is being sent to
        message (string)    string of the message being sent
        time_sent (int)     UNIX timestamp of the time message will be sent
    
    Exceptions:
        InputError          channel_id is not a valid channel ID or
                            message is larger than 1000 characters or
                            time_sent is in the past
        AccessError         authorised user is not a part of the channel they are trying to post to

    Return Value:
        {message_id}        dictionary with a single entry containing the ID of the message sent
    '''
    

def message_sendlaterdm_v1(token, dm_id, message, time_sent):
    '''
    This function allows a user to send a message to a dm with dm_id
    automatically at a specified time in the future
       
    Arguments:
        token (JWT)         JWT token of user who is sending the message
        dm_id (int)         ID of dm the message is being sent to
        message (string)    string of the message being sent
        time_sent (int)     UNIX timestamp of the time message will be sent
    
    Exceptions:
        InputError          dm_id is not a valid dm ID or
                            message is larger than 1000 characters or
                            time_sent is in the past
        AccessError         authorised user is not a part of the dm they are trying to post to

    Return Value:
        {message_id}        dictionary with a single entry containing the ID of the message sent
    '''
    

def message_react_v1(token, message_id, react_id):
    '''
    This function allows a user to add a react to a message with message_id
       
    Arguments:
        token (JWT)         JWT token of user who adding the react
        message_id (int)    ID of the message to add the react to
        react_id (int)      ID of the react the message will receive
    
    Exceptions:
        InputError          message_id is not a valid message in the channel/dm user has joined or
                            react_id is not a valid react ID or
                            message_id already contains an active react with react_id from user
        AccessError         authorised user is not a part of the channel/dm the message is within
    
    Return Value:
        {}                  An empty dictionary
    '''
    

def message_unreact_v1(token, message_id, react_id):
    '''
    This function allows a user to remove a react to a message with message_id
       
    Arguments:
        token (JWT)         JWT token of user who is removing their react
        message_id (int)    ID of the message to remove the react from
        react_id (int)      ID of the react that will be removed from the message
    
    Exceptions:
        InputError          message_id is not a valid message in the channel/dm user has joined or
                            react_id is not a valid react ID or
                            message_id does not contain an active react with react_id from user
        AccessError         authorised user is not a part of the channel/dm the message is within
    
    Return Value:
        {}                  An empty dictionary
    '''
   

def message_pin_v1(token, message_id):
    '''
    This function allows a user to mark a message with message_id as "pinned" 
       
    Arguments:
        token (JWT)         JWT token of user who is marking the message as "pinned"
        message_id (int)    ID of the message to mark as "pinned"
    
    Exceptions:
        InputError          message_id is not a valid message ID or
                            message with message_id is already "pinned"
        AccessError         authorised user is not a part of the channel/dm the message is within or
                            the user is not an owner of the channel or DM
    
    Return Value:
        {}                  An empty dictionary
    '''
    

def message_unpin_v1(token, message_id):
    '''
    This function allows a user to remove a pinned messages mark as "unpinned"
       
    Arguments:
        token (JWT)         JWT token of user who is marking the message as "unpinned"
        message_id (int)    ID of the message to mark as "unpinned"
    
    Exceptions:
        InputError          message_id is not a valid message ID or
                            message with message_id is already "unpinned"
        AccessError         authorised user is not a part of the channel/dm the message is within or
                            the user is not an owner of the channel or DM
    
    Return Value:
        {}                  An empty dictionary
    '''
    
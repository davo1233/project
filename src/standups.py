import threading
import time

from src.data_interface import read_data, write_data
from src.error import AccessError, InputError
from src.auth import decode_token

START_STR = '/standup'
#SEND_STR = 'standup_send'

def message_to_standup(token, channel_id, message):
    '''
    A helper function called by functions in message.py when the prefix is detected to be
    /standup or standup_send. Decides to call standup_start or standup_send depending and
    verifies the corresponding input.
    
    Returns and does nothing if any problem with the input is found. Token and channel_id
    are assumed to have been checked by the message.py function.
    '''
    

def finish_standup(channel_id):
    '''
    A helper function called by the timer in standup_start that enacts once the startup
    finishes. Sends the startup message and clears the startup_cache in the corresponding
    channel. Modifies the posting time of the startup message to align exactly with the
    time_finished designated in standup_start
    '''
    

def send_standup_summary(auth_user_id, channel_id, message, time_finish):
    '''
    A variation of message_send that is allowed to have more than 1000 characters in its
    body. time_created is set to be time_finish and no error checks are used as the only
    way to get to this function is through the necessary error checks
    '''
    

def standup_start_v1(token, channel_id, length):
    '''
    For a given channel, start the standup period whereby for the next "length" seconds, 
    if someone calls "standup_send" with a message, it is buffered during the X second 
    window then at the end of the X second window a message will be added to the message 
    queue in the channel from the user who started the standup

    Arguments:
        token (JWT)             JWT token of authorised user
        channel_id (int)        ID of channel that standup is being called in
        length (int)            Length in seconds of standup

    Exceptions:
        AccessError             user is not a member of the specified channel or
                                user is not a valid user
        InputError              channel_id is not a valid channel ID or
                                an active standup is already running in the channel or
                                the length is invalid
    
    Return Value:
        {time_finish}           dictionary containing a single entry specifying the unix
                                time when the standup will finish
    '''
    

def standup_active_v1(token, channel_id):
    '''
    Check if a standup is currently active in the given channel

    Arguments:
        token (JWT)             JWT token of authorised user
        channel_id (int)        ID of channel that active is being called in

    Exceptions:
        AccessError             user is not a member of the specified channel or
                                user is not a valid user
        InputError              channel_id is not a valid channel ID
    
    Return Value:
    {
        is_active,              boolean representing if there is an active standup
        time_finish             expected finishign time of the active standup. None if 
                                no standup is currently active
    }
    '''
    

def standup_send_v1(token, channel_id, message):
    '''
    Sending a message to get buffered in the standup queue

    Arguments:
        token (JWT)             JWT token of authorised user
        channel_id (int)        ID of channel that standup is being called in
        message (str)           standup message to be added to queue

    Exceptions:
        AccessError             user is not a member of the specified channel or
                                user is not a valid user
        InputError              channel_id is not a valid channel ID or
                                an active standup is not running in the channel or
                                message is over 1000 characters
    
    Return Value:
        {}                      Returns an empty dictionary
    '''
    


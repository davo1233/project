from src.data_interface import read_data, write_data
from src.error import AccessError, InputError
from src.auth import decode_token

def admin_user_remove_v1(token, u_id):
    '''
    Allow a global owner to remove a nominated user from Dreams

    Arguments:
        auth_user_id (int)    id of user removing another user
        u_id (int)            id of user being removed
    
    Exceptions:
        InputError  - u_id is invalid,
                      u_id is currently the only global owner of Dreams
                      
        AccessError - auth_user_id is invalid,
                      authorised user is not a global owner

    Return Value:
        Returns empty dictionary 
    '''
    GLOBAL_OWNER_PERM_ID = 1
    GLOBAL_MEMBER_PERM_ID = 2
    
    auth_user_id = decode_token(token)['user_id']
    
    #Check if auth_user is a global owner
    if data['user_data'][str(auth_user_id)]['global_permission_id'] == GLOBAL_MEMBER_PERM_ID: 
        raise AccessError(description='auth_user is not a global owner')

    #Check if u_id exists
    if str(u_id) not in data['user_data']:
        raise InputError(description='u_id is not a valid user id')

    #Check if u_id is the only global owner of dreams
    global_owner_count = 0
    for user_dict in data['user_data'].values():
        if user_dict['global_permission_id'] == GLOBAL_OWNER_PERM_ID:
            global_owner_count += 1

    if global_owner_count <= 1 and \
        data['user_data'][str(u_id)]['global_permission_id'] == GLOBAL_OWNER_PERM_ID: 
        raise InputError(description='u_id is currently the only global owner')
    
    #Erase user from channel_data
    for channel_id in data['user_data'][str(u_id)]['channels']:

    write_data(data)

    return {}
    
def admin_userpermission_change_v1(token, u_id, permission_id):
    '''
    Allow a global owner to change the global permission value of a nominated user 

    Arguments:
        auth_user_id (int)    id of user granting owner permissions
        u_id (int)            id of user being made an owner
        permission_id (int)   permission_id value 
    
    Exceptions:
        InputError  - u_id is invalid,
                      permission_id is invalid,
                      
        AccessError - auth_user_id is invalid,
                      authorised user is not a global owner

    Return Value:
        Returns empty dictionary 
    '''

    return {}

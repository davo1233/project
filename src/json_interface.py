import json

def read_data(): 
    '''
    Returns a copy of the data stored in the JSON data storage file

    Arguments:
        None
    
    Exceptions:
        None

    Returns:
        data - dictionary containing fields outlined by data structure
    '''
    f = open('src/data.json',"r")
    data = json.load(f)
    return data


def write_data(data):
    file1 = open('src/data.json',"w")
    file1.write(data)
    file1.close()

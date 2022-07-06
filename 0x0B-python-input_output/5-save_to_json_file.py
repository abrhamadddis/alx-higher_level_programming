#!/usr/bin/python3
''''
JSON representation of object
'''

import json


def to_json_string(my_obj):
    '''
    returns the JSON rep of my_obj
    '''
    return json.dumps(my_obj)

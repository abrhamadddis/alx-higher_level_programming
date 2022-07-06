#!/usr/bin/python3
'''
a script that return the json representation of an object
'''

import json


def to_json_string(my_obj):
    '''
    a function that take my_obj as an argument
    and return json representation
    '''

    return json.dumps(my_obj)

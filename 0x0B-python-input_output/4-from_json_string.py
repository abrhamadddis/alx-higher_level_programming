#!/usr/bin/python3
'''
a script that return the string from json representation
'''

import json


def from_json_string(my_str):
    '''
    a function that take my_str as an argument
    and return string representation
    '''

    return json.loads(my_str)

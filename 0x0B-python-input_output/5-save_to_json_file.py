#!/usr/bin/python3
"""
Writes an Object to a text file
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes the representation of my_obj to filenname
    Args:
        - my_obj: object to write
        - filename: file to write to
    """

    with open(filename, 'w+') as f:
        json.dump(my_obj, f)

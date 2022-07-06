#!/usr/bin/python3
'''
script that writes a string to a text file and return the length of string
'''


def write_file(filname="", text=""):
    with open(filname, 'w+') as f:
        f.write(text)
    length_string = len(text)
    return length_string

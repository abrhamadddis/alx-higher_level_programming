#!/usr/bin/python3
# 4-append_write.py
'''
a script that append a file to a script
'''


def append_write(filename="", text=""):
    '''
    a functon that take filename and a string
    as an argument
    '''

    with open(filename, 'a', encoding="utf-8") as f:
        new_file = f.write(text)
        return new_file

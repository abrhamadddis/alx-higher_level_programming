#!/usr/bin/python3
'''
a script that append a file to a script
'''


from asyncore import write


def append_write(filename="", text=""):
    '''
    a functon that take filename and a string
    that will be append to a file
    '''

    with open(filename, 'a', encoding="utf-8") as f:
        new_file = f.write(text)
        return new_file

#!/usr/bin/python3
'''
python script that check inhertnce
'''


def is_same_class(obj, a_class):
    '''
    check if the instance is the same
    '''

    return issubclass(a_class, type(obj))

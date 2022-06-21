#!/usr/bin/python3
'''2-square.py: a script defines a square and check type and value errror'''


class Square:
    ''' create a square type'''

    def __init__(self, size=0):
        '''intialize square with size'''
        self.__size = size

        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

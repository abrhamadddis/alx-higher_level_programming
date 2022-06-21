#!/usr/bin/python3
''' 1-square.py: A script defines square and private instance attribute size'''


class Square:
    '''creating a square type'''

    def __init__(self, size):
        '''intilize a square with size'''

        self.__size = size

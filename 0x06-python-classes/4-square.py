#!/usr/bin/python3
'''4-square.py: script that returnns the current square area'''


class Square:
    '''creates square type'''

    def __init__(self, size=0):
        '''initializes square with size'''
        self.size = size

    @property
    def size(self):
        '''defines the size of square and returns its value'''
        return self.__size

    @size.setter
    def size(self, value):
        '''defines the value of size of square and checkes if >=0'''
        self.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        '''Defines the area of a square'''
        return self.__size * self.__size

#!/usr/bin/python3
'''5-squae.py:prints to stdout the square with the character #'''


class Square:
    '''Creates square type'''
    def __init__(self, size=0):
        '''initializes square with size'''
        self.size = size

    @property
    def size(self):
        '''Defines the size of square and returns its value'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Defines the value of size of square and checks if >='''
        self.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        '''defines the area of a square'''
        return self.__size * self.__size

    def my_print(self):
        '''prints in stdout the square with character #'''
        for a in range(self.__size):
            for b in range(self.__size):
                print('#', end="")
            print()
        if self.__size == 0:
            print()

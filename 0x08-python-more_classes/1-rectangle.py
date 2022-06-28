#!/usr/bin/python3
'''
a python script that create a class callled Rectangle
'''


class Rectangle:
    '''
    a class called Rectangle
    setter and getter function for width and height
    '''
    def __init__(self, width=0, height=0):
        '''
        instantiaion with optional width and height
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''''
        a property to retirive width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' a property to set the value of width'''
        if type(value) is not int:
            return TypeError("width must be an integer")
        elif value < 0:
            return ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        ''' a property to retirive height'''
        return self.__height

    @height.setter
    def height(self, value):
        ''' a property to set the value of height'''
        if type(value) is not int:
            return TypeError("height must be an integer")
        elif value < 0:
            return ValueError("height must be >= 0")
        else:
            self.__height = value

#!/usr/bin/python3
""" a class Rectangle inherites form base class"""


from optparse import Values
from models.base import Base


class Rectangle(Base):
    '''Rectangle methods and filds'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def update(self, *args, **kwargs):
        '''set up args for a rectangle'''
        if args:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.__width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            if len(args) == 5:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
        else:
            for key, vlaues in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, Values)

    def area(self):
        '''a public method that return the area of a rectangle'''
        return self.__width * self.__height

    def display(self):
        '''method for printing Rectangel to stdout'''
        print('\n' * self.y, end="")
        for i in range(self.height):
            for j in range(self.width):
                print ("#", end="")
            print(" ")

    def __str__(self):
        '''return a string representation of Rectatngle'''
        a, d, e, = self.id, self.width, self.height
        b, c = self.x, self.y
        return("[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e))

    @property
    def width(self):
        '''set the property of width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set the width attribute'''
        if type(value) is not int:
            raise TypeError("width is not an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''set the property of height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set the height attribute'''
        if type(value) is not int:
            raise TypeError("height is not an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        '''set the property of x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''set the x attribute'''
        if type(value) is not int:
            raise TypeError("x is not an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        else:
            self.__x = value

    @property
    def y(self):
        '''set the property of y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''set the  y attribute'''
        if type(value) is not int:
            raise TypeError("y is not an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = value

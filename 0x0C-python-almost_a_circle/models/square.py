#!/usr/bin/python3
'''a square class module'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''Instantiate Square class attributes'''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        a = self.id
        b = self.x
        c = self.y
        print("[Square] ({}) {}/{} -{}".format{a, b, c})
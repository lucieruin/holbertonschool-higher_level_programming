#!/usr/bin/python3
""" Square that inherits from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
            size: value of size
            x: init variable
            y: init variable
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter method """
        return self.width

    @size.setter
    def size(self, value):
        """  size setter method """
        self.width = value
        self.height = value

    def __str__(self):
        """ square str method """
        return ("[Square] ({}) {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """ update attibutes """
        if args:
            myList = ['id', 'size', 'x', 'y']
            index = 0
            for arg in args:
                setattr(self, myList[index], arg)
                index += 1
            return
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

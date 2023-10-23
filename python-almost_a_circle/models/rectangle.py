#!/usr/bin/python3
""" class Rectangle that inherits from Base """


from models.base import Base


class Rectangle(Base):
    """ class rectangle """

    @property
    def width(self):
        """ width getter method """

        return self.__width

    @width.setter
    def width(self, value):
        """ width setter method """
        self.integerValid('width', value)
        self.__width = value

    @property
    def height(self):
        """ height getter method """

        return self.__height

    @height.setter
    def height(self, value):
        """ height setter method """
        self.integerValid('height', value)
        self.__height = value

    @property
    def x(self):
        """ x getter method """

        return self.__x

    @x.setter
    def x(self, value):
        """ x setter method """
        self.integerValid2('x', value)
        self.__x = value

    @property
    def y(self):
        """ y getter method """

        return self.__y

    @y.setter
    def y(self, value):
        """ y setter method """
        self.integerValid2('y', value)
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """instance initialization method

        Args:
            width: width of rectangle
            height: height of rectangle
            x: init variable
            y: init variable
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ area of rectangle """
        return (self.width * self.height)

    def display(self):
        """ print rectangle with # """
        for row in range(self.x):
            print()
        for row in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def __str__(self):
        """ the str method """
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}"
                .format(self.id, self.x, self.y, self.width, self.height))

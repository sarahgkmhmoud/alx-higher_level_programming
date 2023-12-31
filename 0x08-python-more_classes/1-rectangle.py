#!/usr/bin/python3
"""creat a Rectangle class """


class Rectangle:
    """Difention of class Rectangle
        Args:
        width(int): the width of rectangle
        height(int): the hight of rectangle
    """

    def __init__(self, width=0, height=0):
        """intialize the variable of rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """get the value of the width

        Return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """reset the value of the width
            Args:
            value: the new value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the value of the width

        Return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """reset the value of the height
            Args:
            value: the new value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

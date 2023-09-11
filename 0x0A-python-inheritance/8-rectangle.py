#!/usr/bin/python3
"""construnct inhrient class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inhtrent class from base_geometry
        Args:
        width(int) the width of rectangulat
        height(int the height of rectangular)
    """

    def __init__(self, width, height):
        """initialize the private value"""

        self._width = width
        self._height = height

    def validation_dimension(self):
        """module to check  the value of rec dimensions"""
        super().integer_validator("width", self._width)
        super().integer_validator("height", self._height)

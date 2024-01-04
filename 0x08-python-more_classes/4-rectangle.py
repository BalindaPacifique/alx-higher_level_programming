#!/usr/bin/python3
"""Creating a Rectangle class"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """new Rectangle

            width (int): new rectangle width.
            height (int): new rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the Area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the Perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the Rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        recta = []
        for i in range(self.__height):
            [recta.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                recta.append("\n")
        return (''.join(recta))

    def __repr__(self):
        """Return the string representation of the Rectangle"""
        recta = "Rectangle(" + str(self.__width)
        recta += ', ' + str(self.__height) + ')'
        return (recta)

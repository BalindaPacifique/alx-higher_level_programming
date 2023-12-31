#!/usr/bin/python3

"""creating a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the Area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """square with the # character."""
        for items in range(0, self.__size):
            [print("#", end="") for indx in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

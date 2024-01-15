#!/usr/bin/python3

"""Creates a base model class."""
import json
import csv
import turtle


class Base:
    """Base model."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

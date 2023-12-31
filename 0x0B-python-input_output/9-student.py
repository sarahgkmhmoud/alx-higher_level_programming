#!/usr/bin/python3
""" Student module
"""


class Student:
    """Write a class Student that defines a student by:
    args:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves
        a dictionary representation of a Student"""
        return self.__dict__

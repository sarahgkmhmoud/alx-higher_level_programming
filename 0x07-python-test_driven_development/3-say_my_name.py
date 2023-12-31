#!/usr/bin/python3
""" function tell the first and second name"""


def say_my_name(first_name, last_name=""):
    """
     a function that prints My name is <first name> <last name>
     ARGS:
        first_name (str): represent first user name
        last_name  (str): default by empty str represent second user name
    """
    if not isinstance(first_name, str) or first_name is None:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {0} {1}".format(first_name, last_name))

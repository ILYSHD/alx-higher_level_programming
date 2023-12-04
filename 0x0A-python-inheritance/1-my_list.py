#!/usr/bin/python3
"""Defines a class Mylist"""


class MyList(list):
    """
    Class that defines properties of a list.
    """
    def print_sorted(self):
        """sort list
        """
        print(sorted(self))

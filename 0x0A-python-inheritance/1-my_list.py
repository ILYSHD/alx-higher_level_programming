#!/usr/bin/python3
"""Defines a class mylist"""

class MyList(list):
    """ a class that defines the properties of mylist"""
    def print_sorted(self):
        """a method to print a listed sorted"""
        print(sorted(self))

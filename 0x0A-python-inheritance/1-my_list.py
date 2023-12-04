#!/usr/bin/python3
"""Defines a class mylist"""

class MyList(list):
    """ a class that defines the properties of mylist"""
    def print_sorted(self):
        """a method to print a listed sorted"""
        print(sorted(self))

if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/1-my_list.txt")

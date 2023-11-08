#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    sorted_dic = dict(sorted(a_dictionary.items()))
    for k, v in sorted_dic.items():
        print("{}: {}".format(k, v))

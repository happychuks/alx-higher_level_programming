#!/usr/bin/python3
#  Function that prints all integers in a list separatee by new line

def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))

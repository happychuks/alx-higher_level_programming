#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return 'None'
    maxNum = 0
    for i in range(len(my_list)):
        if maxNum < my_list[i]:
            maxNum = my_list[i]
    return (maxNum)

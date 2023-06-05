#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    a = my_list[0]
    for i in range(1, len(my_list)):
        if a < my_list[i]:
            a = my_list[i]
    return a

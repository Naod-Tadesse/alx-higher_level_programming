#!/usr/bin/python3
def uniq_add(my_list=[]):
    other_set = set(my_list)
    num = 0
    for i in other_set:
        num += i
    return num

#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0

    for tup in my_list:
        score, weight = tup
        num += score * weight
        den += weight

    if den == 0:
        return 0

    return num / den

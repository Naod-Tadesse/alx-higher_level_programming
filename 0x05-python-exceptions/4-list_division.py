#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    li = []
    i = 0
    result = 0
    while i < list_length:
        try:
            result = my_list_1[i] / my_list_2[i]
            i = i + 1
        except IndexError:
            print("out of range")
            i = i + 1
        except ZeroDivisionError:
            print("division by 0")
            i = i + 1
        except TypeError:
            print("wrong type")
            i = i +1
        finally:
            li.append(result)
            i = i + 1
    return li

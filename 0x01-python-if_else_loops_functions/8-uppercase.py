#!/usr/bin/python3
def uppercase(str):
    string = ''
    for let in str:
        ascii_rep = ord(let)
        if ascii_rep >=  97 and ascii_rep <= 122:
            letter = chr(ascii_rep - 32)
            string = string + letter
        else:
            string = string + let
        print("{}".format(string))



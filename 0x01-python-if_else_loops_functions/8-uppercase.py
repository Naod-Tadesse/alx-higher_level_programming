#!/usr/bin/python3
def uppercase(str):
    for let in str:
        ascii_rep = ord(let)
        if ascii_rep >=  97 and ascii_rep <= 122:
            letter = chr(ascii_rep - 32)
        print("{}".format(letter), end="")
    print()



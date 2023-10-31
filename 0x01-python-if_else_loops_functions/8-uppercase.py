#!/usr/bin/python3
def uppercase(str):
    for let in str:
        ascii_rep = ord(let)
        if ascii_rep >=  97 and ascii_rep <= 122:
            let = chr(ascii_rep - 32)
        print("{}".format(let), end="")
    print()



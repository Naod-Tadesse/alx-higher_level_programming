#!/usr/bin/python3
sub = 31
ind = 91
for i in range(0, 26):
    ind = ind + sub 
    print("{}".format(chr(ind)), end='')
    if sub == 31:
        sub = -33
    elif sub == -33:
        sub = 31


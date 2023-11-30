#!/usr/bin/python3
"""text indenting"""


def text_indentation(text):
    """text indenting function body"""
    if not (type(text) == str):
        raise TypeError("text must be a string")
    count = 0
    tx = ''
    while count < len(text):
        tx = tx + text[count]
        if text[count] in '.?:':
            print(tx.strip(), end="")
            print('\n\n', end="")
            tx = ''
        count = count + 1

    if tx.strip():
        print(tx.strip(), end="")

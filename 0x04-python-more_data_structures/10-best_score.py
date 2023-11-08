#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        alist = list(a_dictionary.keys())
        score = 0
        best = ""
        for i in alist:
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                best = i
        return best

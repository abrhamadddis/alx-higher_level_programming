#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff1 = set_1.difference(set_2)
    diff2 = set_2.difference(set_1)
    dif = diff1.union(diff2)
    return (dif)

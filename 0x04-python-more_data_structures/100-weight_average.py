#!/usr/bin/python3
def weight_average(my_list=[]):
    weight = 0
    div = 0
    for tupl in my_list:
        weight += (tupl[0] * tupl[1])
        div += tupl[1]
    return weight / (div if my_list else 1)

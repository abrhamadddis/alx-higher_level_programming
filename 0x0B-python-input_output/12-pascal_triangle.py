#!/usr/bin/python3
"""
Pascals Triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    my_list = [[1]]
    for i in range(1, n):
        k = [1]
        for j in range(1, i):
            k.append(my_list[i - 1][j - 1] + my_list[i - 1][j])
        k.append(1)
        my_list.append(k)
    return my_list

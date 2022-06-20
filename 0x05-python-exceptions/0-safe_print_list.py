#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for items in my_list:
            print("{}".format(my_list[items]), end="")
    except IndexError:
        pass
    print()
    return i

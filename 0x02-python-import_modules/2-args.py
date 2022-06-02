#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    arg = "arguments:" if length > 1 else "argument:" \
        if length == 1 else "arguments."
    print("{} {}".format(length, arg))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))

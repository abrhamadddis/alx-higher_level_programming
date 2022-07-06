#!/usr/bin/python3
# 3-write_file.py
"""Defines a file-writing function.
"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

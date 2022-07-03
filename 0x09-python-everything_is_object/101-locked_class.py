#!/usr/bin/python3
""" module for a locked class """


class LockedClass:
    """ Locked class that only allow for first_name call """
    __slots__ = ["first_name"]

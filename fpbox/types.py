from .funcs import *

__all__ = [
    "Array",
    "Char",
    "chars",
    "FPboxException"
]


class FPboxException(Exception):
    pass


class Array(tuple):
    """
    Immutable homogenous collection. It can be initialized with either a
    single iterable or with multiple arguments.
    """

    def __new__(cls, *items):
        items = collect(items)
        if items and not is_homogenous(items):
            raise FPboxException("You can't mix types in an Array")
        return tuple.__new__(cls, items)

    def __repr__(self):
        if isinstance(head(self), Char):
            return '"{}"'.format(sum(self))
        return str(list(self))

    def __str__(self):
        if isinstance(head(self), Char):
            return self.__repr__()[1:-1]
        return self.__repr__()


class Char(str):
    """Holds a single character"""

    def __new__(cls, char):
        if not isinstance(char, str) and len(char) == 1:
            raise FPboxException(
                "Invalid input, Chars must be str with a length of 1"
            )
        return str.__new__(cls, char)

    def __repr__(self):
        return "'{}'".format(self)



def chars(string):
    """
    Helper function that returns an array of characters from a string
    """
    return map(Char, Array(string))

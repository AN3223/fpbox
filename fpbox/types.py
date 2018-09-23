from .funcs import map, sum, head, is_homogeneous, collect
from .static import I

__all__ = [
    "Array",
    "Char",
    "chars"
]


class Array(tuple):
    """
    Immutable homogenous collection. It can be initialized with either a
    single iterable or with multiple arguments.
    """

    def __new__(cls, *items):
        items = collect(items)
        if not is_homogeneous(items):
            raise TypeError("You can't mix types in an Array")
        return tuple.__new__(cls, items)

    def is_chars(self):
        try:
            if isinstance(head(self), Char):
                return True
        except IndexError:
            return False
        return False

    def __repr__(self) -> str:
        if self.is_chars():
            return '"{}"'.format(sum(self))
        return str(list(self))

    def __str__(self) -> str:
        if self.is_chars():
            return self.__repr__()[1:-1]
        return self.__repr__()


class Char(str):
    """Holds a single character"""

    def __new__(cls, char):
        if not isinstance(char, str) and len(char) == 1:
            raise ValueError(
                "Invalid input, Char must be str with a length of 1"
            )
        return str.__new__(cls, char)

    def __repr__(self) -> str:
        return "'{}'".format(self)


def chars(string: str) -> I:
    """
    Helper function that returns an array of characters from a string
    """
    return map(Char, Array(string))

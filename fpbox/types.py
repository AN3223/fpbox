from collections.abc import Sequence
from inspect import isgenerator
from builtins import map as lazymap, filter as lazyfilter
from itertools import takewhile, dropwhile

from .funcs import *

class FPboxException(Exception):
    pass


class Stream:
    """
    Takes any iterable, returns a Stream object that gives access to
    a set of lazy (FP-related) methods. Some things to note: no methods
    mutate the iterable, most methods return a Stream object, and the
    Stream objects themselves are generators that yield the contents
    of the original iterable
    """

    def __init__(self, xs):
        self.xs = xs

    def __iter__(self):
        return (x for x in self.xs)

    def map(self, f):
        return Stream(lazymap(f, self))

    def filter(self, f):
        return Stream(lazyfilter(f, self))

    def reduce(self, f):
        return Stream(lazy_reduce(f, self))

    def takewhile(self, f):
        return Stream(takewhile(f, self))

    def dropwhile(self, f):
        return Stream(dropwhile(f, self))

    def list(self):
        """Packs the stream up into a list"""
        return list(self)

    def tuple(self):
        """Packs the stream up into a tuple"""
        return tuple(self)


class Array(Sequence):
    """
    Immutable homogenous collection. It can be initialized with either a
    single list/tuple/generator (which will return an Array consisting of the
    contents of said list/tuple/generator) or it can just be given multiple
    arguments to initialize the Array with
    """

    def __init__(self, *items):
        self.items = collect(items)
        self.type = type(head(self.items))
        if False in (isinstance(x, self.type) for x in self.items):
            raise FPboxException("You can't mix types in an Array")

    def __repr__(self):
        if self.type == Char:  # Creates a representation of [Char]
            unpacked_chars = [x.char for x in self.items]
            return '"{}"'.format(sum(unpacked_chars))
        else:
            return str(list(self.items))

    def __str__(self):
        if self.type == Char:
            return self.__repr__()[1:-1]
        return self.__repr__()

    def __add__(self, other):
        if isinstance(other, Array):
            other = other.items
        return Array(self.items + tuple(other))

    def __getitem__(self, item):
        return self.items[item]

    def __len__(self):
        return len(self.items)


class Char:
    """Holds a single character"""

    def __init__(self, char):
        if isinstance(char, str) and len(char) == 1:
            self.char = char
        else:
            raise FPboxException("Invalid input, Chars must be str with a length of 1")

    def __repr__(self):
        return "'{}'".format(self.char)

    def __str__(self):
        return self.char

    def __add__(self, other):
        return self.char + other


def chars(string):
    """
    Helper function that returns an array of characters from a string
    """
    return Array(map(Char, list(string)))

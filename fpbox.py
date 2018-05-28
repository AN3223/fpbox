from functools import reduce
from collections.abc import Sequence
from inspect import isgenerator


class FPboxException(Exception):
    pass


def head(xs):
    return xs[0]


def tail(xs):
    return xs[1:]


def last(xs):
    return xs[-1]


def init(xs):
    return xs[:-1]


def map(f, xs):
    """Strict version of map"""
    return [f(x) for x in xs]


def filter(f, xs):
    """Strict version of filter (uses truthiness)"""
    return [x for x in xs if f(x)]


def sum(xs):
    """Sum implementation that also works on non-int types"""
    return reduce(lambda x, y: x + y, xs)


def bool_filter(f, xs):
    """Strict version of filter (no truthiness, only booleans)"""
    return [x for x in xs if f(x) is True]


def foldl(f, acc, xs):
    return reduce(f, ([acc] + xs))


def foldr(f, acc, xs):
    return reduce(f, (reverse(xs) + [acc]))


def reverse(xs):
    """Returns a reversed sequence"""
    return type(xs)(reversed(xs))


def chars(string):
    """Returns an array of characters"""
    return Array(map(Char, string))


def c(f, g):
    """Function composition"""
    return lambda x: f(g(x))


class Array(Sequence):
    """
    Immutable sequence where all items can only be of a single type
    """

    def __init__(self, *items):
        if len(items) == 1:
            if isinstance(head(items), list):
                items = head(items)
            if isgenerator(head(items)):
                items = list(head(items))
        self.items = tuple([x for x in items if isinstance(x, type(head(items)))])

    def __repr__(self):
        if isinstance(head(self.items), Char):  # Creates a representation of [Char]
            unpacked_chars = map(lambda x: x.char, self.items)
            return '"{}"'.format(sum(unpacked_chars))
        return str(list(self.items))

    def __add__(self, other):
        if isinstance(other, Array):
            other = other.items
        return Array(list(self.items) + list(other))

    def __getitem__(self, item):
        return self.items[item]

    def __len__(self):
        return len(self.items)


class Char:
    def __init__(self, char):
        if isinstance(char, str) and len(char) == 1:
            self.char = char
        else:
            raise Exception("Invalid char")

    def __repr__(self):
        return "'{}'".format(self.char)

    def __str__(self):
        return self.char

    def __add__(self, other):
        return self.char + other

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
                items = [x for x in head(items)]
        self._items = [x for x in items if isinstance(x, type(head(items)))]

    def __repr__(self):
        return str(self._items)

    def __add__(self, other):
        if isinstance(other, Array):
            other = other._items
        return Array([x for x in self._items] + [x for x in other])

    def __getitem__(self, item):
        return self._items[item]

    def __len__(self):
        return len(self._items)

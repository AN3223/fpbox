from functools import reduce, lru_cache
from collections.abc import Sequence
from inspect import isgenerator
from builtins import map as lazymap, filter as lazyfilter
from operator import add


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
    return type(xs)(lazymap(f, xs))


def filter(f, xs):
    """Strict version of filter"""
    return type(xs)(lazyfilter(f, xs))


def sum(xs):
    """Sum implementation that also works on non-int types"""
    return reduce(add, xs)


def foldl(f, acc, xs):
    # Double reverses cancel each other out, so you can think of it like this:
    # reduce(f, ([acc] + xs))
    # However, it's done like this so foldl can work on Arrays
    return reduce(f, reverse(reverse(xs) + [acc]))


def foldr(f, acc, xs):
    return reduce(f, (reverse(xs) + [acc]))


def reverse(xs):
    """Returns a reversed sequence"""
    return type(xs)(reversed(xs))


def chars(string):
    """Returns an array of characters"""
    return Array(map(Char, list(string)))


def c(f, g):
    """Function composition"""
    return lambda x: f(g(x))


class Array(Sequence):
    """Immutable homogenous list"""

    def __init__(self, *items):
        if len(items) == 1:  # Deconstructs single instances of generator and list/tuple
            if isinstance(head(items), list) or isinstance(head(items), tuple):
                items = head(items)
            if isgenerator(head(items)):
                items = list(head(items))
        for x in items:  # Checks if all items are the same type
            if not isinstance(x, type(head(items))):
                raise FPboxException("You can't mix types in an Array")
        self.items = tuple(items)

    def __repr__(self):
        if isinstance(head(self.items), Char):  # Creates a representation of [Char]
            unpacked_chars = [x.char for x in self.items]
            return '"{}"'.format(sum(unpacked_chars))
        else:
            return str(list(self.items))

    def __add__(self, other):
        if isinstance(other, Array):
            other = other.items
        return Array(self.items + tuple(other))

    def __getitem__(self, item):
        return self.items[item]

    def __len__(self):
        return len(self.items)


class Char:
    def __init__(self, char):
        if isinstance(char, str) and len(char) == 1:
            self.char = char
        else:
            raise FPboxException("Invalid char")

    def __repr__(self):
        return "'{}'".format(self.char)

    def __str__(self):
        return self.char

    def __add__(self, other):
        return self.char + other


def partition(f, xs):
    """
    Applies a function that returns a bool to each element of a sequence and
    returns a tuple with a true sequence and a false sequence.
    Should not be called with an impure function.
    """
    t = type(xs)
    true = filter(f, xs)
    false = [x for x in xs if x not in true]
    return t(true), t(false)


def pure(memo=False):
    """Mark a function as pure, optionally taking
    advantage of functool's lru_cache decorator"""

    def inner(f):
        if memo:
            return lru_cache()(f)
        else:
            return f

    return inner


class Stream:
    """Takes any iterable, returns a Stream object that
    gives access to a set of lazy methods"""

    def __init__(self, xs):
        self.xs = xs

    def __iter__(self):
        for x in self.xs:
            yield x

    def map(self, f):
        return Stream(lazymap(f, self))

    def filter(self, f):
        return Stream(lazyfilter(f, self))

    def reduce(self, f):
        return reduce(f, self)

    def takewhile(self, f):
        def inner():
            for x in self:
                if f(x):
                    yield x
                else:
                    break

        return Stream(inner())

    def list(self):
        return list(self)

    def tuple(self):
        return tuple(self)

from functools import reduce, partial


def head(xs):
    return xs[0]


def unsafe_tail(xs):
    """Might not always return a list"""
    return xs[1:]


def tail(xs: list):
    return list(xs[1:])


def last(xs):
    return xs[-1]


def init(xs: list):
    return list(xs[:-1])


def unsafe_init(xs):
    """Might not always return a list"""
    return xs[1:]


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
    """Returns a sequence reversed as a list"""
    return [x for x in reversed(xs)]


def c(f, g):
    """Function composition"""
    return lambda x: f(g(x))


class Array:
    """
    Immutable list where all items can only be of a single type
    """

    def __init__(self, *items):
        if len(items) == 1 and isinstance(head(items), list):
            items = head(items)
        self._items = [x for x in items if isinstance(x, type(head(items)))]

    def __repr__(self):
        return str(self._items)

    def __add__(self, other):
        if isinstance(other, Array):
            other = other._items
        return Array([x for x in self._items] + [x for x in other])

    def __iter__(self):
        for x in self._items:
            yield x

    def __reversed__(self):
        for x in reversed(self._items):
            yield x

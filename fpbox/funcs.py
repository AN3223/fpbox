from builtins import map as lazy_map, filter as lazy_filter
from collections import Iterable
from inspect import signature
from functools import reduce
from functools import wraps
from operator import add


__all__ = [
    "lazy",
    "head",
    "tail",
    "last",
    "init",
    "map",
    "binmap",
    "flipped_binmap",
    "filter",
    "sum",
    "partition",
    "lazy_binmap",
    "lazy_flipped_binmap",
    "lazy_reduce",
    "reverse",
    "c",
    "compose",
    "curry",
    "collect",
    "lazy_map",
    "lazy_filter",
    "reduce",
    "is_homogenous"
]


def lazy(f):
    """A decorator to simply yield the result of a function"""

    @wraps(f)
    def lazyfunc(*args):
        yield f(*args)

    return lazyfunc


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
    return type(xs)(lazy_map(f, xs))


def binmap(f, xs):
    """Strict version of lazy_binmap"""
    return type(xs)(lazy_binmap(f, xs))


def flipped_binmap(f, xs):
    """Strict version of lazy_flipped_binmap"""
    return type(xs)(lazy_flipped_binmap(f, xs))


def filter(f, xs):
    """Strict version of filter"""
    return type(xs)(lazy_filter(f, xs))


def sum(xs):
    """
    A "sum" implementation that can take advantage of operator overloading
    """
    return reduce(add, xs)


def partition(f, xs):
    """
    Works similar to filter, except it returns a two-item tuple where the
    first item is the sequence of items that passed the filter and the
    second is a sequence of items that didn't pass the filter
    """
    t = type(xs)
    true = filter(f, xs)
    false = [x for x in xs if x not in true]
    return t(true), t(false)


def lazy_binmap(f, xs):
    """
    Maps a binary function over a sequence. The function is applied to each item
    and the item after it until the last item is reached.
    """
    return (f(x, y) for x, y in zip(xs, xs[1:]))


def lazy_flipped_binmap(f, xs):
    """
    Same as lazy_binmap, except the parameters are flipped for the binary function
    """
    return (f(y, x) for x, y in zip(xs, xs[1:]))


@lazy
def lazy_reduce(f, xs):
    """Lazy version of functools.reduce"""
    return reduce(f, xs)


def reverse(xs):
    """Strict version of reversed"""
    return type(xs)(reversed(xs))


def c(f, g):
    """Function composition"""
    return lambda x: f(g(x))


def compose(*fs):
    """
    Function composition over a sequence of functions. Functions can be supplied
    as multiple arguments or a single iterable.
    """
    return reduce(c, collect(fs))


def curry(f, args_supplied=()):
    """
    Takes a function and returns a curried version of it. You probably shouldn't use this
    with built-ins! Even if it seems to work with a built-in, it might not work properly
    in previous versions of Python.
    """
    try:
        nargs_required = len(signature(f).parameters)
    except ValueError as e:
        raise ValueError(
            str(e) + " (maybe you're trying to curry a built-in?)"
        )

    def inner(arg):
        new_args_supplied = args_supplied + (arg,)
        if len(new_args_supplied) == nargs_required:
            return f(*new_args_supplied)
        return curry(f, new_args_supplied)

    return inner


def collect(items, convert_to=tuple):
    """
    Converts a nested iterable into a tuple. If no nested iterable is found (or if multiple are
    found) then "items" is returned unchanged to the caller. Useful for generic functions.

    :param items: Target sequence
    :param convert_to: Target type
    :return: The "collected" sequence
    """
    if len(items) == 1 and isinstance(head(items), Iterable):
        return convert_to(*items)
    return convert_to(items)


def is_homogenous(xs):
    t = type(head(xs))
    if any(not isinstance(x, t) for x in xs):
        return False
    return True

from builtins import map as lazy_map, filter as lazy_filter
from collections import Iterable
from inspect import signature
from functools import reduce
from functools import wraps
from operator import add

from typing import Tuple, Generator
from .static import T, I, C, S, F

__all__ = [
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
    "reverse",
    "c",
    "compose",
    "curry",
    "collect",
    "lazy_map",
    "lazy_filter",
    "reduce",
    "is_homogeneous"
]


def head(xs: S[T]) -> T:
    return xs[0]


def tail(xs: S) -> S:
    return xs[1:]


def last(xs: S[T]) -> T:
    return xs[-1]


def init(xs: S) -> S:
    return xs[:-1]


def map(f: F, xs: T) -> I:
    """Strict version of map"""
    return type(xs)(lazy_map(f, xs))


def binmap(f: F, xs: T) -> I:
    """Strict version of lazy_binmap"""
    return type(xs)(lazy_binmap(f, xs))


def flipped_binmap(f: F, xs: T) -> I:
    """Strict version of lazy_flipped_binmap"""
    return type(xs)(lazy_flipped_binmap(f, xs))


def filter(f: F, xs: T) -> I:
    """Strict version of filter"""
    return type(xs)(lazy_filter(f, xs))


def sum(xs: I) -> I:
    """
    A "sum" implementation that can take advantage of operator overloading
    """
    return reduce(add, xs)


def partition(f: F, xs: T) -> Tuple[T, T]:  # TODO: Make a lazy counterpart
    """
    Works similar to filter, except it returns a two-item tuple where the
    first item is the sequence of items that passed the filter and the
    second is a sequence of items that didn't pass the filter
    """
    t = type(xs)
    true = filter(f, xs)
    false = [x for x in xs if x not in true]
    return t(true), t(false)


def lazy_binmap(f: F, xs: S) -> Generator:
    """
    Maps a binary function over a sequence. The function is applied to each item
    and the item after it until the last item is reached.
    """
    return (f(x, y) for x, y in zip(xs, xs[1:]))


def lazy_flipped_binmap(f: F, xs: S) -> Generator:
    """
    Same as lazy_binmap, except the parameters are flipped for the binary function
    """
    return (f(y, x) for x, y in zip(xs, xs[1:]))


def reverse(xs: T) -> I:
    """Strict version of reversed"""
    return type(xs)(reversed(xs))


def c(f: F, g: F) -> F:
    """Function composition"""
    return lambda x: f(g(x))


def compose(*fs: T) -> F:
    """
    Function composition over a sequence of functions. Functions can be supplied
    as multiple arguments or a single iterable.
    """
    return reduce(c, collect(fs))


def curry(f: F, args_supplied: tuple = ()) -> F:
    """
    Takes a function and returns a curried version of it (don't use with built-ins).
    """
    try:
        nargs_required: int = len(signature(f).parameters)
    except ValueError as e:
        raise ValueError(
            str(e) + " (maybe you're trying to curry a built-in?)"
        )

    @wraps(f)
    def inner(arg):
        new_args_supplied: tuple = args_supplied + (arg,)
        if len(new_args_supplied) == nargs_required:
            return f(*new_args_supplied)
        return curry(f, new_args_supplied)

    return inner


def collect(items: S, convert_to: type = tuple) -> I:
    """
    Converts a nested iterable into a tuple. If no nested iterable is found (or if multiple are
    found) then "items" is returned unchanged to the caller.

    :param items: Target sequence
    :param convert_to: Target type
    :return: The "collected" sequence
    """
    if len(items) == 1 and isinstance(head(items), Iterable):
        return convert_to(*items)
    return convert_to(items)


def is_homogeneous(xs: S) -> bool:
    """
    Checks if an iterable is homogeneous in type.

    :param xs: Iterable to be checked
    :return: Boolean, representing whether the iterable is homogeneous
    """
    try:
        t: type = type(head(xs))
    except IndexError:
        return True
    if any(not isinstance(x, t) for x in xs):
        return False
    return True

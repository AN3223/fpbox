from builtins import map as lazy_map, filter as lazy_filter
from functools import reduce
from functools import wraps
from operator import add


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


def reverse_binmap(f, xs):
    """Strict version of lazy_reverse_binmap"""
    return type(xs)(lazy_reverse_binmap(f, xs))


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
    for index in range(len(xs)):
        if index + 1 == len(xs):
            break
        yield f(xs[index], xs[index + 1])


def lazy_reverse_binmap(f, xs):
    """
    Same as lazy_binmap, except the parameters are flipped for the binary function
    """
    for index in range(len(xs)):
        if index + 1 == len(xs):
            break
        yield f(xs[index + 1], xs[index])


def lazy_dropwhile(f, xs):
    """
    Returns a sequences with every item from the beginning removed
    that causes f to return True
    """
    done_dropping = False
    for x in xs:
        if not done_dropping:
            if not f(x):
                done_dropping = True
        else:
            yield x


def lazy_takewhile(f, xs):
    """
    Returns every item of a sequence, until it encounters an item that
    causes f to return false.
    """
    for x in xs:
        if f(x):
            yield x
        else:
            break


@lazy
def lazy_reduce(f, xs):
    """Lazy version of functools.reduce"""
    return reduce(f, xs)


def dropwhile(f, xs):
    """Strict version of lazy_dropwhile"""
    return type(xs)(lazy_dropwhile(f, xs))


def takewhile(f, xs):
    """Strict version of lazy_takewhile"""
    return type(xs)(lazy_takewhile(f, xs))


def reverse(xs):
    """Returns a reversed sequence"""
    return type(xs)(reversed(xs))


def c(f, g):
    """Function composition"""
    return lambda x: f(g(x))

def compose(fs):
    """Function composition over a list of functions"""
    return reduce(c, reversed(fs))

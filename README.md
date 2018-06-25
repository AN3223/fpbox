# FPbox
A toolkit for functional programming in Python

# Install
`pip install fpbox`

# Examples
```python
from functools import partial as p
from fpbox import *

# The Array collection enforces that the whole sequence be the same type. Immutable.
xs = Array([1, 2, 3])

# head/tail/init/last functions, alternative to slicing
one = head(xs)
two_three = tail(xs)
three = last(xs)
one_two = init(xs)

# Gets the last item of a reversed sequence that has been mapped over
# with a function that adds one to each value
fn_composition = c(last, c(reverse, p(map, lambda x: x + 1)))(xs)

# Use strings like normal sequences with the "chars" helper function
reversed_string = reverse(chars("Racecar"))

# Really pushing the strings-as-sequences idea with string comprehension
string_comprehension = Array([Char(x) for x in 'hello' if not x == 'h'])

# The Stream class takes a sequence and returns a generator, and also
# gives a handful of FP-related methods. Map isn't actually applied to
# any of the elements yet, because we haven't asked for any yet.
lazy_xs_plus_one = Stream(xs).map(lambda x: x + 1)


# Here's a quicksort implementation that shows how the tools
# FPBox gives you can be used for great good
def quicksort(xs):
    if len(xs) > 1:
        pivot = head(xs)
        lesser, greater = map(quicksort, partition(lambda x: x < pivot, tail(xs)))
        return lesser + [pivot] + greater
    else:
        return xs

one_to_five_ascending = quicksort([5, 4, 3, 2, 1])
```

# Reference
https://fpbox.readthedocs.io/en/latest/

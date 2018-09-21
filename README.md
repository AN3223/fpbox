# FPbox
A toolkit for functional programming in Python

# Install
`pip install fpbox`

# Examples
```python
from fpbox import *
from operator import sub

# The Array collection enforces that the whole sequence be the same type. Immutable.
xs = Array([1, 2, 3])

# head/tail/init/last functions
one = head(xs)
two_three = tail(xs)
three = last(xs)
one_two = init(xs)

# Function composition, right to left
fn_composition = compose(last, reverse)(xs)

# Use strings more like tuples/lists/sets with the "chars" helper function
# This wouldn't work with normal strings because the str constructor would
# just try to create a representation of the map object used under the hood
# by "reverse"
reversed_string = reverse(chars("Racecar"))

# String comprehension!
string_comprehension = Array(Char(x) for x in 'hello' if not x == 'h')

# Calculating the amount of numbers between each number in the Array
distance_between = flipped_binmap(sub, xs)

curried_function = curry(lambda x, y: x + y)  # Curries a function
curried_result = curried_function(1)(2)  # Result is 3!


# Here's a quicksort implementation that shows how the tools
# FPBox offers can be used for great good
def quicksort(xs):
    if len(xs) > 1:
        pivot = head(xs)
        lesser, greater = map(quicksort, partition(lambda x: x < pivot, tail(xs)))
        return lesser + [pivot] + greater
    return xs


one_to_five_ascending = quicksort([5, 4, 3, 2, 1])
```

# Reference
https://fpbox.readthedocs.io/en/latest/

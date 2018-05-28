# FPbox
A toolkit for functional programming in Python

# Install
`pip install fpbox`

# Examples
```python
from functools import partial
from fpbox.fpbox import *

xs = Array([1, 2, 3])
sum_of_xs = foldr(lambda x, y: x + y, 0, xs)
three_two_one = reverse(xs)
one = head(xs)
two_three = tail(xs)
three = last(xs)
one_two = init(xs)
fn_composition = c(last, c(reverse, partial(map, lambda x: x + 1)))(xs)
reversed_string = reverse(chars("Racecar"))
```

# Reference
Read the source code! :D

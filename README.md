# FPbox
A toolkit for functional programming in Python

# Install
`pip install fpbox`

# Examples
```python
from functools import partial as p
from fpbox import *

xs = Array([1, 2, 3])
three_two_one = reverse(xs)
one = head(xs)
two_three = tail(xs)
three = last(xs)
one_two = init(xs)
fn_composition = c(last, c(reverse, p(map, lambda x: x + 1)))(xs)
reversed_string = reverse(chars("Racecar"))
string_comprehension = Array([Char(x) for x in 'hello' if not x == 'h'])
lazy_xs_plus_one = Stream(xs).map(lambda x: x + 1)
```

# Reference
https://fpbox.readthedocs.io/en/latest/

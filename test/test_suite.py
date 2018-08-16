import unittest
import fpbox as fp
from itertools import dropwhile, takewhile


class TestBox(unittest.TestCase):
    def test_partition(self):
        def quicksort(xs):
            if len(xs) > 1:
                pivot = fp.head(xs)
                lesser, greater = map(quicksort, fp.partition(lambda x: x < pivot, fp.tail(xs)))
                return lesser + [pivot] + greater
            else:
                return xs

        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_stream(self):
        xs = fp.Array(1, 2, 3, 4, 5)

        xs_mapped = fp.Stream(xs).map(lambda x: x + 1).list()
        self.assertEqual(xs_mapped, [x + 1 for x in xs])

        def less_than_four(x):
            return x < 4

        xs_takewhile = fp.Stream(xs).takewhile(less_than_four).list()
        self.assertEqual(xs_takewhile, list(takewhile(less_than_four, xs)))

        xs_dropwhile = fp.Stream(xs).dropwhile(less_than_four).list()
        self.assertEqual(xs_dropwhile, list(dropwhile(less_than_four, xs)))

    def test_binmap(self):
        from operator import sub

        xs = [10, 15, 20, 25, 30]
        self.assertEqual(fp.flipped_binmap(sub, xs), [5, 5, 5, 5])

    def test_chars(self):
        self.assertEqual(str(fp.chars('hello')), 'hello')

    def test_compose(self):
        fs = [lambda x: x + 1, lambda x: x * 100]
        f = fp.compose(fs)
        self.assertEqual(f(1), 101)

        f = fp.compose(*fs)
        self.assertEqual(f(1), 101)

    def test_curry(self):
        def test(x, y):
            return x, y

        f = fp.curry(test)
        f10 = f(10)
        f20 = f(20)

        self.assertEqual(f10(20), (10, 20))
        self.assertEqual(f20(10), (20, 10))

    def test_collect(self):
        def genericfunction(*items):
            return fp.collect(items)

        xs = (1,2,3,4)

        self.assertEqual(xs, genericfunction(xs))
        self.assertEqual(xs, genericfunction(list(xs)))
        self.assertEqual(xs, genericfunction((x for x in xs)))

    def test_array(self):
        xs = fp.Array([1, 2, 3])

        self.assertEqual(fp.Array(1, 2, 3), xs)
        self.assertEqual(fp.Array((1, 2, 3)), xs)
        self.assertEqual(fp.Array({1, 2, 3}), xs)
        self.assertEqual(fp.map(int, fp.Array("123")), xs)

        self.assertEqual(xs + fp.Array(), xs)


if __name__ == '__main__':
    unittest.main()

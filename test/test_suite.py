import unittest
import fpbox as fp


class TestBox(unittest.TestCase):
    def test_partition(self):
        def quicksort(xs):
            if len(xs) > 1:
                pivot = fp.head(xs)

                def sort(x): return x < pivot
                lesser, greater = fp.partition(sort, fp.tail(xs))
                return quicksort(lesser) + [pivot] + quicksort(greater)
            else:
                return xs

        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

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

        xs = (1, 2, 3, 4)

        self.assertEqual(xs, genericfunction(xs))
        self.assertEqual(xs, genericfunction(list(xs)))
        self.assertEqual(xs, genericfunction((x for x in xs)))

    def test_array(self):
        xs = fp.Array([1, 2, 3])

        self.assertEqual(fp.Array(1, 2, 3), xs)
        self.assertEqual(fp.Array((1, 2, 3)), xs)
        self.assertEqual(fp.map(int, fp.Array("123")), xs)

        self.assertEqual(xs + fp.Array(), xs)
        self.assertEqual(fp.Array(), fp.Array())

    def test_homogeneous(self):
        self.assertTrue(fp.is_homogeneous([]))
        self.assertTrue(fp.is_homogeneous([1, 2, 3]))
        self.assertFalse(fp.is_homogeneous([1, 2, "3"]))


if __name__ == '__main__':
    unittest.main()

import unittest
import fpbox as fp


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

    def test_binmap(self):
        from operator import sub

        xs = [10, 15, 20, 25, 30]
        self.assertEqual(fp.reverse_binmap(sub, xs), [5, 5, 5, 5])

    def test_chars(self):
        self.assertEqual(str(fp.chars('hello')), 'hello')

    def test_compose(self):
        f = fp.compose([lambda x: x + 1, lambda x: x * 100])
        self.assertEqual(f(1), 101)


if __name__ == '__main__':
    unittest.main()

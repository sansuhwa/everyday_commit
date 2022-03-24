import unittest

from basic_practice import mysum


class TestPractice(unittest.TestCase):
    def test_mysum(self):
        self.assertEqual(mysum('abc', 'def', 'skdlfn'), 'abcdefskdlfn')
        self.assertEqual(mysum([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(mysum((1, 2, 3), (4, 5, 6)), (1, 2, 3, 4, 5, 6))
        self.assertEqual(mysum(''), '')
        self.assertEqual(mysum([]), [])
        self.assertEqual(mysum(()), ())


if __name__ == '__main__':
    unittest.main()
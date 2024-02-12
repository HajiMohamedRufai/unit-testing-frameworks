import unittest
from unittest import TestCase


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 4, "Should be 4")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 5")

if __name__ == '__main__':
    # Here you call the unittest differently by mentioning unittest.main()
    unittest.main()  
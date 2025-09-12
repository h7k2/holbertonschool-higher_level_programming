#!/usr/bin/python3
"""Unittests for max_integer([..])."""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        self.assertIsNone(max_integer())

    def test_all_negative(self):
        self.assertEqual(max_integer([-10, -5, -7, -8]), -5)

    def test_mixed_signs(self):
        self.assertEqual(max_integer([-10, 0, 5, -3]), 5)

    def test_duplicates(self):
        self.assertEqual(max_integer([3, 3, 2, 3]), 3)

    def test_identical_elements(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_large_numbers(self):
        self.assertEqual(max_integer([10**6, 10**12, -10**15]), 10**12)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 2.1]), 2.2)

    def test_ints_and_floats(self):
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)


if __name__ == '__main__':
    unittest.main()

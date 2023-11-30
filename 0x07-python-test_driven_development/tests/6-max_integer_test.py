#!/usr/bin/python3
"""task 6 unittest"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """body for the class"""
    def test_elements_2(self):
        self.assertEqual(max_integer([2, 3]), 3)

    def test_negative_elements(self):
        self.assertEqual(max_integer([-3, -6, -1, -4]), -1)

    def test_mixed_elements(self):
        self.assertEqual(max_integer([-7, -1, 1, -4]), 1)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000000, 2000000, 7000000]), 7000000)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_negative_with_zero(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, 0]), 0)

    def test_same_but_notm(self):
        self.assertEqual(max_integer([2, 2, 6, 8]), 8)

    def test_all_zero(self):
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_same_max(self):
        self.assertEqual(max_integer([2, 6, 4, 6]), 6)

    def test_list_of_str(self):
        self.assertEqual(max_integer(["alx", "swe", "python"]), "swe")

    def test_empty_str(self):
        self.assertEqual(max_integer(""), None)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, -2.5, 3.5]), 3.5)

    def test_one(self):
        self.assertEqual(max_integer([3]), 3)

    def test_beginning(self):
        self.assertEqual(max_integer([7, 3, 4, 5]), 7)
if __name__ == '__main__':
    unittest.main()

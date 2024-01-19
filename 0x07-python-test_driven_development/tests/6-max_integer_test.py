#!/usr/bin/python3
""" Unittest for max_integer(list=[]) """


import unittest
max_integer = __import__("6-max_integer")


class TestMaxInteger(unittest.TestCase):
    """
    Tests various functionalieties of max_integer function
    """

    def test_max(self):
        self.assertEqual(max_integer([12, 9, 0, 45]), 45)
        self.assertEqual(max_integer([-2, -100, -70, -34], -2))
        self.assertEqual(max_integer([]), None)

    def test_values(self):
        self.assertRaises(TypeError, max_integer, )
        self.assertRaises(TypeError, max_integer, 23)
        self.assertRaises(TypeError, max_integer, "hello")

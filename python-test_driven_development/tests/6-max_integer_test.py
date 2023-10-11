#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    """ class for unittests """
    def test_max_integer(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([-3]), -3)
        self.assertEqual(max_integer([-1, -2]), -1)
        self.assertEqual(max_integer([15, 10, 5]), 15)
        self.assertEqual(max_integer([15, 10, 5, -5, -10, -15]), 15)
        self.assertEqual(max_integer([15, 15, 15]), 15)
        self.assertEqual(max_integer([1.25, 2.25, 3.25]), 3.25)
        self.assertEqual(max_integer([-1.25, -2.25, -3.25]), -1.25)
        self.assertEqual(max_integer([1.25, 2.56, 3, 4]), 4)
        self.assertEqual(max_integer([-1.25, -2.56, -3, -4]), -1.25)



    def test_type_error(self):
        """ type_errors """
        self.assertRaises(TypeError, max_integer, ["h", 1])
        self.assertRaises(TypeError, max_integer, [2, [2, 1]])
        self.assertRaises(TypeError, max_integer, ["hey", 1])
        self.assertRaises(TypeError, max_integer, [('inf'), 1])
        self.assertRaises(TypeError, max_integer, [('nan'), 1])
        self.assertRaises(TypeError, max_integer, [('nan')], 1)
        self.assertRaises(TypeError, max_integer, [('inf')], 1)
        self.assertRaises(TypeError, max_integer, [(6, 6, 6)], 'inf')
        self.assertRaises(TypeError, max_integer, [(6, 6, 6)], 'nan')
        self.assertRaises(TypeError, max_integer, [(6, 6, 6)], "Hey Georgie")
        self.assertRaises(TypeError, max_integer, [(6, 6, 6)], "H")
        self.assertRaises(TypeError, max_integer, [(6, 6, 6)], 'a')

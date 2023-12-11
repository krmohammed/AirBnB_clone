#!/usr/bin/python3
"""
Test cases for the Review Class
"""
import unittest
from datetime import datetime
from models.review import Review


class TestInitMethod(unittest.TestCase):
    """
    Tests for new instances
    """

    def test_no_args(self):
        """
        no arguments
        """
        a = Review()
        b = Review()
        self.assertTrue(a.id != b.id)
        self.assertFalse(b.id is None)

    def test_dict_init(self):
        """
        initializing with a dictionary
        """
        a = Review()
        a_dict = a.to_dict()
        b = Review(**a_dict)
        self.assertTrue(a.__str__(), b.__str__())
        self.assertTrue(a.to_dict(), b.to_dict())
        self.assertFalse(a is b)

    def test_args(self):
        """
        initialization with non-keyworded args
        """
        a = Review("Khalil", "Rahman", 89)
        b = Review(99)
        c = Review(**a.to_dict())
        self.assertIsInstance(a, Review)
        self.assertIsInstance(b, Review)
        self.assertTrue(a.id == c.id)

    def test_types(self):
        """
        test for class attribute types
        """
        a = Review()
        b = Review()
        self.assertIsInstance(a, Review)
        self.assertIsInstance(b, Review)
        self.assertIsInstance(a.id, str)
        self.assertIsInstance(b.updated_at, datetime)
        self.assertIsInstance(b.created_at, datetime)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""
Test cases for the Place Class
"""
import unittest
from datetime import datetime
from models.city import City


class TestInitMethod(unittest.TestCase):
    """
    Tests for new instances
    """

    def test_no_args(self):
        """
        no arguments
        """
        a = City()
        b = City()
        self.assertTrue(a.id != b.id)
        self.assertFalse(b.id is None)

    def test_dict_init(self):
        """
        initializing with a dictionary
        """
        a = City()
        a_dict = a.to_dict()
        b = City(**a_dict)
        self.assertTrue(a.__str__(), b.__str__())
        self.assertTrue(a.to_dict(), b.to_dict())
        self.assertFalse(a is b)

    def test_args(self):
        """
        initialization with non-keyworded args
        """
        a = City("Khalil", "Rahman", 89)
        b = City(99)
        c = City(**a.to_dict())
        self.assertIsInstance(a, City)
        self.assertIsInstance(b, City)
        self.assertTrue(a.id == c.id)

    def test_types(self):
        """
        test for class attribute types
        """
        a = City()
        b = City()
        self.assertIsInstance(a, City)
        self.assertIsInstance(b, City)
        self.assertIsInstance(a.id, str)
        self.assertIsInstance(b.updated_at, datetime)
        self.assertIsInstance(b.created_at, datetime)


if __name__ == "__main__":
    unittest.main()

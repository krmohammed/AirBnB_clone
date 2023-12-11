#!/usr/bin/python3
"""
Test cases for the Amenity Class
"""
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestInitMethod(unittest.TestCase):
    """
    Tests for new instances
    """

    def test_no_args(self):
        """
        no arguments
        """
        a = Amenity()
        b = Amenity()
        self.assertTrue(a.id != b.id)
        self.assertFalse(b.id is None)

    def test_dict_init(self):
        """
        initializing with a dictionary
        """
        a = Amenity()
        a_dict = a.to_dict()
        b = Amenity(**a_dict)
        self.assertTrue(a.__str__(), b.__str__())
        self.assertTrue(a.to_dict(), b.to_dict())
        self.assertFalse(a is b)

    def test_args(self):
        """
        initialization with non-keyworded args
        """
        a = Amenity("Khalil", "Rahman", 89)
        b = Amenity(99)
        c = Amenity(**a.to_dict())
        self.assertIsInstance(a, Amenity)
        self.assertIsInstance(b, Amenity)
        self.assertTrue(a.id == c.id)

    def test_types(self):
        """
        test for class attribute types
        """
        a = Amenity()
        b = Amenity()
        self.assertIsInstance(a, Amenity)
        self.assertIsInstance(b, Amenity)
        self.assertIsInstance(a.id, str)
        self.assertIsInstance(b.updated_at, datetime)
        self.assertIsInstance(b.created_at, datetime)


if __name__ == "__main__":
    unittest.main()

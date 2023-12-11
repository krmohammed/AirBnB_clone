#!/usr/bin/python3
"""
Test cases for the User Class
"""
import unittest
from datetime import datetime
from models.user import User


class TestInitMethod(unittest.TestCase):
    """
    Tests for new instances
    """

    def test_no_args(self):
        """
        no arguments
        """
        a = User()
        b = User()
        self.assertTrue(a.id != b.id)
        self.assertFalse(b.id is None)

    def test_dict_init(self):
        """
        initializing with a dictionary
        """
        a = User()
        a_dict = a.to_dict()
        b = User(**a_dict)
        self.assertTrue(a.__str__(), b.__str__())
        self.assertTrue(a.to_dict(), b.to_dict())
        self.assertFalse(a is b)

    def test_args(self):
        """
        initialization with non-keyworded args
        """
        a = User("Khalil", "Rahman", 89)
        b = User(99)
        c = User(**a.to_dict())
        self.assertIsInstance(a, User)
        self.assertIsInstance(b, User)
        self.assertTrue(a.id == c.id)

    def test_types(self):
        """
        the types of the class attributes
        """
        a = User()
        b = User()
        self.assertIsInstance(a, User)
        self.assertIsInstance(b, User)
        self.assertIsInstance(a.id, str)
        self.assertIsInstance(b.updated_at, datetime)
        self.assertIsInstance(b.created_at, datetime)


if __name__ == "__main__":
    unittest.main()

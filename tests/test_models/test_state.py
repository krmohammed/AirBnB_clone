#!/usr/bin/python3
"""
Test cases for the State Class
"""
import unittest
from datetime import datetime
from models.state import State


class TestInitMethod(unittest.TestCase):
    """
    Tests for new instances
    """

    def test_no_args(self):
        """
        no arguments
        """
        a = State()
        b = State()
        self.assertTrue(a.id != b.id)
        self.assertFalse(b.id is None)

    def test_dict_init(self):
        """
        initializing with a dictionary
        """
        a = State()
        a_dict = a.to_dict()
        b = State(**a_dict)
        self.assertTrue(a.__str__(), b.__str__())
        self.assertTrue(a.to_dict(), b.to_dict())
        self.assertFalse(a is b)

    def test_args(self):
        """
        initialization with non-keyworded args
        """
        a = State("Khalil", "Rahman", 89)
        b = State(99)
        c = State(**a.to_dict())
        self.assertIsInstance(a, State)
        self.assertIsInstance(b, State)
        self.assertTrue(a.id == c.id)

    def test_types(self):
        """
        test class attribute types
        """
        a = State()
        b = State()
        self.assertIsInstance(a, State)
        self.assertIsInstance(b, State)
        self.assertIsInstance(a.id, str)
        self.assertIsInstance(b.updated_at, datetime)
        self.assertIsInstance(b.created_at, datetime)


if __name__ == "__main__":
    unittest.main()

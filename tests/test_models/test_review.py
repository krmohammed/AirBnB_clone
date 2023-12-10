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
        self.assertTrue(a.created_at == a.updated_at)
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


class TestSaveMethod(unittest.TestCase):
    """
    Test cases for the save() method
    """

    def test_zero_args(self):
        """
        no arguments
        """
        c = Review()
        a = c.updated_at
        c.save()
        self.assertTrue(c.updated_at)


class TestToDictMethod(unittest.TestCase):
    """
    Test cases for to_dict() method
    """

    def test_no_args(self):
        """
        no arguments
        """
        c = Review()
        d = c.to_dict()
        self.assertIsInstance(d, dict)
        self.assertTrue(hasattr(d, "__class__"))

    def test_types(self):
        """
        the types of the return value
        """
        c = Review()
        d = c.to_dict()
        self.assertEqual(type(d), dict)
        self.assertIsInstance(d["updated_at"], str)
        self.assertIsInstance(d["created_at"], str)


class TestStr(unittest.TestCase):
    """
    Test cases for __str__() method
    """

    def test_str(self):
        """
        __str__ method
        """
        obj = Review()
        self.assertIsInstance(obj.__str__(), str)


if __name__ == "__main__":
    unittest.main()

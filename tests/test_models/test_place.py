#!/usr/bin/python3
"""
Test cases for the Place Class
"""
import unittest
from datetime import datetime
from models.place import Place


class TestInitMethod(unittest.TestCase):
    """
    Tests for new instances
    """

    def test_no_args(self):
        """
        no arguments
        """
        a = Place()
        b = Place()
        self.assertTrue(a.id != b.id)
        self.assertTrue(a.created_at == a.updated_at)
        self.assertFalse(b.id is None)

    def test_dict_init(self):
        """
        initializing with a dictionary
        """
        a = Place()
        a_dict = a.to_dict()
        b = Place(**a_dict)
        self.assertTrue(a.__str__(), b.__str__())
        self.assertTrue(a.to_dict(), b.to_dict())
        self.assertFalse(a is b)

    def test_args(self):
        """
        initialization with non-keyworded args
        """
        a = Place("Khalil", "Rahman", 89)
        b = Place(99)
        c = Place(**a.to_dict())
        self.assertIsInstance(a, Place)
        self.assertIsInstance(b, Place)
        self.assertTrue(a.id == c.id)

    def test_types(self):
        """
        test for class attribute types
        """
        a = Place()
        b = Place()
        self.assertIsInstance(a, Place)
        self.assertIsInstance(b, Place)
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
        c = Place()
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
        c = Place()
        d = c.to_dict()
        self.assertIsInstance(d, dict)
        self.assertTrue(hasattr(d, "__class__"))

    def test_types(self):
        """
        the types of the return value
        """
        c = Place()
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
        obj = Place()
        self.assertIsInstance(obj.__str__(), str)


if __name__ == "__main__":
    unittest.main()

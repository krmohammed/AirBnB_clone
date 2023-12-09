#!/usr/bin/python3
"""
Test cases for the BaseModel Class
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestInitMethod(unittest.TestCase):
    """Tests for new instances"""

    def test_no_args(self):
        """no arguments"""
        a = BaseModel()
        b = BaseModel()
        self.assertTrue(a.id != b.id)
        self.assertTrue(a.created_at == a.updated_at)
        self.assertFalse(b.id is None)

    def test_types(self):
        a = BaseModel()
        b = BaseModel()
        self.assertIsInstance(a, BaseModel)
        self.assertIsInstance(b, BaseModel)
        self.assertIsInstance(a.id, str)
        self.assertIsInstance(b.updated_at, datetime)
        self.assertIsInstance(b.created_at, datetime)


class TestSaveMethod(unittest.TestCase):
    """
    Test cases for the save() method
    """

    def test_zero_args(self):
        """no arguments"""
        c = BaseModel()
        a = c.updated_at
        c.save()
        self.assertFalse(a == c.updated_at)


class TestToDictMethod(unittest.TestCase):
    """
    Test cases for to_dict() method
    """

    def test_no_args(self):
        """no arguments"""
        c = BaseModel()
        d = c.to_dict()
        self.assertIsInstance(d, dict)
        self.assertTrue(hasattr(d, "__class__"))

    def test_types(self):
        c = BaseModel()
        d = c.to_dict()
        self.assertIsInstance(d["updated_at"], str)
        self.assertIsInstance(d["created_at"], str)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""
Test Cases for the FileStorage Class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestInitMethod(unittest.TestCase):
    """
    Test for init method
    """

    def test_no_args(self):
        s = FileStorage()
        self.assertFalse(hasattr(s, "__objects"))
        self.assertFalse(hasattr(s, "__file_path"))
        self.assertIsInstance(s.all(), dict)


class TestDestroyMethod(unittest.TestCase):
    """
    Test for destroy method
    """

    def test_destroy(self):
        s = FileStorage()
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        s.destroy(b)

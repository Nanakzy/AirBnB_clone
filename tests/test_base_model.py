#!/usr/bin/python3
"""Unit tests for BaseModel class"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""
    def test_attributes(self):
        """Test initialization of BaseModel attributes"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_save(self):
        """Test save method"""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        my_model = BaseModel()
        obj_dict = my_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')


if __name__ == '__main__':
    unittest.main()

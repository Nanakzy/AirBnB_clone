#!/usr/bin/python3

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """Unit tests for FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.file_path = "file_test.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        """Tear down test environment."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test all() method."""
        self.assertEqual(self.storage.all(), {})

        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(self.storage.all(), {'BaseModel.' + obj.id: obj})

    def test_new(self):
        """Test new() method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(self.storage.all(), {'BaseModel.' + obj.id: obj})

    def test_save_reload(self):
        """Test save() and reload() methods."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        self.assertIn('BaseModel.' + obj.id, new_storage.all())
        self.assertEqual(new_storage.all()['BaseModel.' + obj.id].id, obj.id)
        self.assertEqual(new_storage.all()
                         ['BaseModel.' + obj.id].created_at, obj.created_at)
        self.assertEqual(new_storage.all()
                         ['BaseModel.' + obj.id].updated_at, obj.updated_at)


if __name__ == '__main__':
    unittest.main()

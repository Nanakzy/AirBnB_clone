#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()

        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertTrue('id' in model_dict)
        self.assertTrue('created_at' in model_dict)
        self.assertTrue('updated_at' in model_dict)

    def test_save_reload(self):
        storage = FileStorage()
        model = BaseModel()
        model.name = "Test Model"
        model.my_number = 42

        # Save the model to file
        model.save()

        # Reload the model from file
        storage.reload()

        # Get all objects from storage
        objects = storage.all()

        # Check if the reloaded object exists in storage
        self.assertTrue(model.__class__.__name__ + '.' + model.id in objects)

        # Check if the reloaded object has correct attributes
        reloaded_model = objects[model.__class__.__name__ + '.' + model.id]
        self.assertEqual(reloaded_model.name, "Test Model")
        self.assertEqual(reloaded_model.my_number, 42)


if __name__ == '__main__':
    unittest.main()

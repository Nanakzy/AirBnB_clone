#!usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Set up method to create a BaseModel instance before each test.
        """
        self.base_model = BaseModel()

    def test_attributes(self):
        """
        Test if BaseModel instance has all required attributes.
        """
        self.assertTrue(hasattr(self.base_model, "id"))
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))

    def test_id_type(self):
        """
        Test if id attribute is of type str.
        """
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_type(self):
        """
        Test if created_at attribute is of type datetime.
        """
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_type(self):
        """
        Test if updated_at attribute is of type datetime.
        """
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_method(self):
        """
        Test if __str__ method returns the expected string representation.
        """
        expected_str = "[BaseModel] ({}) {}".format(
                self.base_model.id, self.base_model.__dict__
                )
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        """
        Test if save method updates the updated_at attribute.
        """
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """
        Test if to_dict method returns the expected dictionary representation.
        """
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertTrue("__class__" in obj_dict)
        self.assertTrue("created_at" in obj_dict)
        self.assertTrue("updated_at" in obj_dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")


if __name__ == "__main__":
    unittest.main()

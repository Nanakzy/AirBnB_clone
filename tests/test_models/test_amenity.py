#!/usr/bin/python3

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_amenity_inherits_from_base_model(self):
        """Test Amenity inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_attributes(self):
        """Test Amenity attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

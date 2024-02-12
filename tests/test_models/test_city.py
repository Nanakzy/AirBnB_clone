#!/usr/bin/python3

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def test_city_inherits_from_base_model(self):
        """Test City inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_attributes(self):
        """Test City attributes"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

#!/usr/bin/python3

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_state_inherits_from_base_model(self):
        """Test State inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_attributes(self):
        """Test State attributes"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

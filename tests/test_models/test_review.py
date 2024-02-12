#!/usr/bin/python3

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_review_inherits_from_base_model(self):
        """Test Review inherits from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_attributes(self):
        """Test Review attributes"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

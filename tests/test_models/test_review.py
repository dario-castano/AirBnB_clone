#!/usr/bin/python3
""" Module for unit testing of Review class
"""
import unittest
from models.review import Review
import pep8


class TestReview(unittest.TestCase):
    """Tests class User
    """
    def test_review_pep8_conformance(self):
        """ The code is PEP8 conformant?
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0)

    def test_review_instances(self):
        """Tests if User instances are working
        """
        obj = Review()
        self.assertIsInstance(obj, Review)

    def test_review_attributes(self):
        """Tests if User instances are working
        """
        obj = Review()
        self.assertIsInstance(obj.place_id, str)
        self.assertIsInstance(obj.user_id, str)
        self.assertIsInstance(obj.text, str)

#!/usr/bin/python3
""" Module for unit testing of Amenity class
"""
import unittest
from models.amenity import Amenity
import pep8


class TestAmenity(unittest.TestCase):
    """Tests class for Amenity
    """
    def test_amenity_pep8_conformance(self):
        """ The code is PEP8 conformant?
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0)

    def test_amenity_instances(self):
        """Tests if Amenity instances are working
        """
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)

    def test_amenity_attributes(self):
        """Tests if amenity instances are working
        """
        obj = Amenity()
        self.assertIsInstance(obj.name, str)

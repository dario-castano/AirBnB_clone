#!/usr/bin/python3
""" Module for unit testing of City class
"""
import unittest
from models.city import City
import pep8


class TestCity(unittest.TestCase):
    """Tests class City
    """
    def test_city_pep8_conformance(self):
        """ The code is PEP8 conformant?
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0)

    def test_city_instances(self):
        """Tests if City instances are working
        """
        obj = City()
        self.assertIsInstance(obj, City)

    def test_city_attributes(self):
        """Tests if City instances are working
        """
        obj = City()
        self.assertIsInstance(obj.state_id, str)
        self.assertIsInstance(obj.name, str)

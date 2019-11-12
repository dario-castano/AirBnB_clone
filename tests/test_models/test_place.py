#!/usr/bin/python3
""" Module for unit testing of Place class
"""
import unittest
from models.place import Place
import pep8


class TestPlace(unittest.TestCase):
    """Tests class Place
    """
    def test_place_pep8_conformance(self):
        """ The code is PEP8 conformant?
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_place_instances(self):
        """Tests if Place instances are working
        """
        obj = Place()
        self.assertIsInstance(obj, Place)

    def test_place_attributes(self):
        """Tests if Place instances are working
        """
        obj = Place()
        self.assertIsInstance(obj.city_id, str)
        self.assertIsInstance(obj.user_id, str)
        self.assertIsInstance(obj.name, str)
        self.assertIsInstance(obj.description, str)
        self.assertIsInstance(obj.number_rooms, int)
        self.assertIsInstance(obj.number_bathrooms, int)
        self.assertIsInstance(obj.max_guest, int)
        self.assertIsInstance(obj.price_by_night, int)
        self.assertIsInstance(obj.latitude, float)
        self.assertIsInstance(obj.longitude, float)
        self.assertIsInstance(obj.amenity_ids, list)

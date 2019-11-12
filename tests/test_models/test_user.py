#!/usr/bin/python3
""" Module for unit testing of User class
"""
import unittest
from models.user import User
import pep8


class TestUser(unittest.TestCase):
    """Tests class User
    """
    def test_base_pep8_conformance(self):
        """ The code is PEP8 conformant?
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_user_instances(self):
        """Tests if User instances are working
        """
        obj = User()
        self.assertIsInstance(obj, User)

    def test_user_(self):
        """Tests if User instances are working
        """
        obj = User()
        self.assertIsInstance(obj.email, str)
        self.assertIsInstance(obj.password, str)
        self.assertIsInstance(obj.first_name, str)
        self.assertIsInstance(obj.last_name, str)

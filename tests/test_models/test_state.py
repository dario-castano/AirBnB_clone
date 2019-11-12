#!/usr/bin/python3
""" Module for unit testing of State class
"""
import unittest
from models.state import State
import pep8


class TestState(unittest.TestCase):
    """Tests class for State
    """
    def test_state_pep8_conformance(self):
        """ The code is PEP8 conformant?
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0)

    def test_state_instances(self):
        """Tests if State instances are working
        """
        obj = State()
        self.assertIsInstance(obj, State)

    def test_state_attributes(self):
        """Tests if State instances are working
        """
        obj = State()
        self.assertIsInstance(obj.name, str)

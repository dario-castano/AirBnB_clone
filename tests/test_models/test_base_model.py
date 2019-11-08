import unittest
""" Test cases for the BaseModels class
"""
import io
import sys
import datetime
import uuid
from models.base_model import BaseModel

class TestBase(unittest.TestCase):
    """ Unit tests for the Base model class for the project
    """

    def test_Base_performance(self):
        """ Tests if instances are working correctly
        """
        model_1 = BaseModel()
        self.assertTrue(uuid.UUID(model_1.id))
        self.assertIsInstance(model_1.created_at, datetime.datetime)
        self.assertIsInstance(model_1.updated_at, datetime.datetime)
        model_2 = BaseModel()
        self.assertIsNot(model_1, model_2)
        self.assertNotEqual(model_1.id, model_2.id)
        self.assertNotEqual(model_1.created_at, model_2.created_at)
        self.assertNotEqual(model_1.updated_at, model_2.updated_at)
        self.assertTrue(uuid.UUID(model_2.id))
        self.assertIsInstance(model_2.created_at, datetime.datetime)
        self.assertIsInstance(model_2.updated_at, datetime.datetime)
        self.assertIsInstance(model_1, BaseModel)
        self.assertIsInstance(model_2, BaseModel)

    def test_Base_str_format(self):
        """ Tests if the str method is printing the string correctly
        """
        model_1 = BaseModel()
        stream_out = io.StringIO()
        sys.stdout = stream_out
        print(model_1)
        sys.stdout = sys.__stdout__
        self.assertEqual(stream_out.getvalue(), #here goes the mock because we dont know the exact output)

import unittest
""" Test cases for the BaseModels class
"""
import io
import contextlib
import datetime
import pep8
import uuid
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """ Unit tests for the Base model class for the project
    """
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['../../../models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_base_performance(self):
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

    def test_base_str_format(self):
        """ Tests if the str method is printing the string correctly
        """
        title = '[BaseModel]'
        uu_id = 'ccb68527-5744-4e5c-ae6d-d21a09ecf50d'
        fake_date = datetime.datetime(2000, 1, 1, 0, 0, 0, 0)

        model_1 = BaseModel()
        model_1.id = uu_id
        model_1.created_at = fake_date
        model_1.updated_at = fake_date

        fake_dict = {'id': uu_id,
                     'created_at': fake_date,
                     'updated_at': fake_date}

        target = "{} ({}) {}\n".format(title, uu_id, fake_dict)

        stdout_data = io.StringIO()
        with contextlib.redirect_stdout(stdout_data):
            print(model_1)
        self.assertEqual(stdout_data.getvalue(), target)

    def test_base_id_is_str(self):
        obj = BaseModel()
        self.assertTrue(type(obj.id) is str)

    def test_base_id_is_uuid(self):
        obj = BaseModel()
        id_str = obj.id
        self.assertEqual(id_str, str(uuid.UUID(id_str)))

    def test_base_created_at_is_datetime(self):
        obj = BaseModel()
        self.assertTrue(type(obj.created_at) is datetime.datetime)

    def test_base_updated_at_is_datetime(self):
        obj = BaseModel()
        self.assertTrue(type(obj.updated_at) is datetime.datetime)

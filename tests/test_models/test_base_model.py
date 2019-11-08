import unittest
import uuid
import datetime
import pep8
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['../../../models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

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

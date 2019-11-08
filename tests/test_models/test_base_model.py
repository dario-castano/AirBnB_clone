import unittest
import uuid
import datetime
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
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

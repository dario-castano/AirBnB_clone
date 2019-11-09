import unittest
""" Test cases for the BaseModels class
"""
import time
import io
import contextlib
import datetime
import pep8
import uuid
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """ Unit tests for the Base model class for the project
    """
    def test_base_pep8_conformance(self):
        """ The code is PEP8 conformant?
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['../../../models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_base_documented(self):
        """ BaseModel has some documentation?
        """
        from models import base_model
        doc = base_model.__doc__
        self.assertTrue(len(doc) > 10)
        doc = BaseModel.__doc__
        self.assertTrue(len(doc) > 10)
        methods = [k for k, v in BaseModel.__dict__.
                   items() if 'function' in str(v)]
        for m in methods:
            self.assertTrue(len(m.__doc__) > 10)

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
        """ __str__ method is printing the string correctly?
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
        """ BaseModel's id is a str?
        """
        obj = BaseModel()
        self.assertTrue(type(obj.id) is str)

    def test_base_id_is_uuid(self):
        """ BaseModel's id is an UUID?
        """
        obj = BaseModel()
        id_str = obj.id
        self.assertEqual(id_str, str(uuid.UUID(id_str)))

    def test_base_created_at_is_datetime(self):
        """ BaseModel's created_at is a datetime object?
        """
        obj = BaseModel()
        self.assertTrue(type(obj.created_at) is datetime.datetime)

    def test_base_updated_at_is_datetime(self):
        """ BaseModel's updated_at is a datetime object?
        """
        obj = BaseModel()
        self.assertTrue(type(obj.updated_at) is datetime.datetime)

    def test_base_save_updates_timestamp(self):
        """ BaseModel's save() is updating the timestamp?
        """
        new_obj = BaseModel()
        date1 = new_obj.updated_at
        new_obj.save()
        date2 = new_obj.updated_at
        self.assertIsInstance(date1, datetime.datetime)
        self.assertIsInstance(date2, datetime.datetime)
        self.assertTrue(date2 > date1)

    def test_base_to_dict_returns_dict(self):
        """ BaseModel's to_dict() returns a dict?
        """
        obj = BaseModel()
        dic = obj.to_dict()
        self.assertTrue(type(dic) is dict)

    def test_base_to_dict_prints_isoformat(self):
        """ BaseModel's to_dict() are storing isoformats?
        """
        obj = BaseModel()
        iso_regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}$'
        dic = obj.to_dict()
        self.assertRegex(dic['created_at'], iso_regex)
        self.assertRegex(dic['updated_at'], iso_regex)

    def test_base_to_dict_return_attributes(self):
        """ Checks if to_dict() method returns  all the
        attributes required as keys
        """
        obj = BaseModel()
        obj.name = "holberton"
        dic = obj.to_dict()
        self.assertTrue("id" in dic.keys())
        self.assertTrue("updated_at" in dic.keys())
        self.assertTrue("created_at" in dic.keys())
        self.assertTrue("__class__" in dic.keys())
        self.assertTrue("name" in dic.keys())
        self.assertTrue(dic["__class__"] == "BaseModel")
        self.assertTrue(dic["name"] == "holberton")

    def test_base_args_ignored(self):
        """Tests that args are ignored as arguments of BaseModel()
        """
        obj = BaseModel("string")
        with self.assertRaises(AttributeError):
            print(obj.string)
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(uuid.UUID(obj.id))

        obj = BaseModel([])
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(uuid.UUID(obj.id))

        obj = BaseModel(None)
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(uuid.UUID(obj.id))

    def test_base_kwargs_used_only(self):
        """ Tests if instantiation is correct using kwargs
        """
        dic = {"id": 'ccb68527-5744-4e5c-ae6d-d21a09ecf50d',
               "created_at": '2000-01-01T00:00:00.000000',
               "updated_at": '2000-01-01T00:00:00.000000',
               "name": "holberton"}
        obj = BaseModel(**dic)
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(uuid.UUID(obj.id))
        self.assertTrue('ccb68527-5744-4e5c-ae6d-d21a09ecf50d' == obj.id)
        self.assertTrue(type(obj.created_at) is datetime.datetime)
        self.assertTrue(obj.created_at == datetime.
                        datetime(2000, 1, 1, 0, 0, 0, 0))
        self.assertTrue(type(obj.updated_at) is datetime.datetime)
        self.assertTrue(obj.updated_at == datetime.
                        datetime(2000, 1, 1, 0, 0, 0, 0))
        self.assertTrue(obj.name == "holberton")

    def test_base_kwargs_used_only_edge_cases_and_format(self):
        """ Tests posible edge cases using kwargs
        In case of wrong format, a new instance is created
        """
        dic = {"id": 'Wrong format: 5744-4e5c-ae6d-d21a09ecf50d',
               "created_at": 'Wrong format: 2000-01-01T',
               "updated_at": 'Wrong format :2000-01-01T',
               "name": "holberton"}
        obj = BaseModel(**dic)
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(uuid.UUID(obj.id))
        self.assertTrue(type(obj.created_at) is datetime.datetime)
        self.assertTrue(type(obj.updated_at) is datetime.datetime)
        self.assertTrue(obj.name == "holberton")

        dic = {"name": "holberton"}
        obj = BaseModel(**dic)
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(uuid.UUID(obj.id))
        self.assertTrue(type(obj.created_at) is datetime.datetime)
        self.assertTrue(type(obj.updated_at) is datetime.datetime)
        self.assertTrue(obj.name == "holberton")

        dic = {}
        obj = BaseModel(**dic)
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(uuid.UUID(obj.id))
        self.assertTrue(type(obj.created_at) is datetime.datetime)
        self.assertTrue(type(obj.updated_at) is datetime.datetime)

    def test_base_args_and_kwargs(self):
        """ Tests if the object is instantiated correctly
        when using both args and kwargs
        """
        dic = {"id": 'ccb68527-5744-4e5c-ae6d-d21a09ecf50d',
               "created_at": '2000-01-01T00:00:00.000000',
               "updated_at": '2000-01-01T00:00:00.000000',
               "name": "holberton"}
        args = ["hello",
                [],
                {}]
        obj = BaseModel(*args, **dic)
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(uuid.UUID(obj.id))
        self.assertTrue('ccb68527-5744-4e5c-ae6d-d21a09ecf50d' == obj.id)
        self.assertTrue(type(obj.created_at) is datetime.datetime)
        self.assertTrue(obj.created_at == datetime.
                        datetime(2000, 1, 1, 0, 0, 0, 0))
        self.assertTrue(type(obj.updated_at) is datetime.datetime)
        self.assertTrue(obj.updated_at == datetime.
                        datetime(2000, 1, 1, 0, 0, 0, 0))
        self.assertTrue(obj.name == "holberton")

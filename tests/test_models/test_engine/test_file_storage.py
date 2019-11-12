import unittest
""" Test cases for the FileStorage class
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """ Tests for the FileStorage class
    """
    def setUp(self):
        """ This method is always run for every test before execution
        """
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = 'test_storage_file.json'

    def tearDown(self):
        """ Always run after execution of tests
        """
        if os.path.isfile('test_storage_file.json'):
            os.remove('test_storage_file.json')

    def test_file_storage_instances(self):
        """ Test if a new instance of file storage exists
        """
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_file_storage_attributes(self):
        """ Checks if the instances of FileStorage have the attributes
        """
        storage = FileStorage()
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertIsInstance(storage._FileStorage__file_path, str)

        storage2 = FileStorage()
        self.assertIsInstance(storage2, FileStorage)
        self.assertIsNot(storage, storage2)
        self.assertIsInstance(storage2._FileStorage__objects, dict)
        self.assertIsInstance(storage2._FileStorage__file_path, str)

    def test_file_storage_methods(self):
        """ Tests if the FileStorage instances have the correct methods
        """
        storage = FileStorage()
        self.assertTrue(hasattr(storage, "all"))
        self.assertTrue(hasattr(storage, "new"))
        self.assertTrue(hasattr(storage, "save"))
        self.assertTrue(hasattr(storage, "reload"))

    def test_file_storage_all(self):
        """ Tests the all() method
        """
        storage = FileStorage()
        objs = storage.all()
        self.assertIsInstance(objs, dict)
        self.assertTrue(objs == {})

    def test_file_storage_new_save(self):
        """ Tests the methods new() and save() for serialization of objects
        """
        dic = {"id": 'ccb68527-5744-4e5c-ae6d-d21a09ecf50d',
               "created_at": '2000-01-01T00:00:00.000000',
               "updated_at": '2000-01-01T00:00:00.000000'}
        obj = BaseModel(**dic)
        storage = FileStorage()

        storage.new(obj)
        objects = storage.all()
        self.assertTrue(objects["BaseModel.ccb68527-5744-\
4e5c-ae6d-d21a09ecf50d"] is obj)

        storage.save()
        self.assertTrue(os.path.isfile('test_storage_file.json'))
        with open("test_storage_file.json", encoding="UTF-8") as f:
            read_json = f.read()
            self.assertTrue('\"BaseModel.ccb68527-5744-4e5c-ae6d-\
d21a09ecf50d\":' in read_json)
            self.assertTrue('\"id\": \"ccb68527-5744-4e5c-ae6d-d21a09ecf50d\"'
                            in read_json)
            self.assertTrue('\"__class__\": \"BaseModel\"' in read_json)
            self.assertTrue('\"created_at\": \"2000-01-01T00:00:00\"'
                            in read_json)
            self.assertTrue('\"updated_at\": \"2000-01-01T00:00:00\"'
                            in read_json)

    def test_file_storage_empty_path(self):
        """ Checks that reload() method does nothing when path is empty
        """
        if os.path.isfile('test_storage_file.json'):
            os.remove('test_storage_file.json')

        storage = FileStorage()
        storage.reload()
        obj = storage.all()
        self.assertTrue(obj == {})

    def test_file_storage_reload(self):
        """ Tests if the reload method is working correctly
        """
        with open("test_storage_file.json", encoding="UTF-8", mode="w") as f:
            f.write('{"BaseModel.ccb68527-5744-4e5c-ae6d-d21a09ecf50d": {"\
updated_at": "2000-01-01T00:00:00", "id": "ccb68527-5744-4e5c-\
ae6d-d21a09ecf50d", "__class__": "BaseModel", "created_at": "\
2000-01-01T00:00:00"}}')

        storage = FileStorage()
        storage.reload()
        objs = storage.all()
        self.assertTrue(type(objs["BaseModel.ccb68527-\
5744-4e5c-ae6d-d21a09ecf50d"]) is BaseModel)

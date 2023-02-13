#!/usr/bin/python3

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        self.file_path = "test.json"
        self.storage = FileStorage(self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test the all method"""
        # Test all method with empty storage
        self.assertEqual(self.storage.all(), {})

        # Test all method after adding an object
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(self.storage.all(), {f"BaseModel.{obj.id}": obj})

    def test_new(self):
        """Test the new method"""
        # Test new method with a new object
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(self.storage.all(), {f"BaseModel.{obj.id}": obj})

        # Test new method with an existing object
        obj2 = BaseModel()
        obj2.id = obj.id
        self.storage.new(obj2)
        self.assertEqual(self.storage.all(), {f"BaseModel.{obj.id}": obj2})

    def test_save(self):
        """Test the save method"""
        # Test save method with no objects
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, "r") as f:
            data = json.load(f)
        self.assertEqual(data, {})

        # Test save method with one object
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(self.file_path, "r") as f:
            data = json.load(f)
        self.assertEqual(data, {f"BaseModel.{obj.id}": obj.to_dict()})

    def test_reload(self):
        """Test the reload method"""
        # Test reload method with no file
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

        # Test reload method with one object in file
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage = FileStorage(self.file_path)
        self.storage.reload()
        self.assertEqual(self.storage.all(), {f"BaseModel.{obj.id}": obj})

    def test_class_from_dict(self):
        """Test the class_from_dict method"""
        storage = FileStorage()
        base = BaseModel()
        base_dict = base.to_dict()
        obj = storage.class_from_dict(base_dict)
        self.assertIsInstance(obj, BaseModel)
        self.assertEqual(obj.id, base.id)
        self.assertEqual(obj.created_at, base.created_at)
        self.assertEqual(obj.updated_at, base.updated_at)

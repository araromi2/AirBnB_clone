#!/usr/bin/python3
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.obj = BaseModel()
        self.storage.new(self.obj)
        self.storage.save()


    def test_all(self):
        """
        Test all() returns an empty dictionary if no objects are stored
        """
        self.storage._FileStorage__objects = {}  # Clear objects dictionary
        objects = self.storage.all()
        self.assertEqual(objects, {})

    def test_new(self):
        """
        Test new() adds the object to the objects dictionary"""
        objects = self.storage.all()
        key = "BaseModel." + self.obj.id
        self.assertIn(key, objects)
        self.assertEqual(objects[key], self.obj)

    def test_save(self):
        """
        Test save() serializes objects to the JSON file
        """
        with open(self.file_path, "r") as file:
            data = json.load(file)
        key = "BaseModel." + self.obj.id
        self.assertIn(key, data)
        self.assertEqual(data[key], self.obj.to_dict())

    def test_reload(self):
        """
        Test reload() deserializes the JSON file to objects
        """
        self.storage.reload()
        objects = self.storage.all()
        key = "BaseModel." + self.obj.id
        self.assertIn(key, objects)
        self.assertEqual(objects[key], self.obj)

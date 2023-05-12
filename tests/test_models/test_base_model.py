#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel class contains unit tests for the BaseModel class.
    """

    def setUp(self):
        """
        Set up the necessary objects and configurations before each test.
        """
        self.base_model = BaseModel()

    def test_attributes(self):
        """
        Test if the instance has the required attributes.
        """
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_generation(self):
        """
        Test the generation of the 'id' attribute.
        """
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)

    def test_initial_date(self):
        """
        Test the date attributes
        """
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsNotNone(self.base_model.updated_at)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_representation(self):
        """
        Test the string representation of the instance.
        """
        class_name = self.base_model.__class__.__name__
        expected_str = "[{}] ({}) {}".format(
            class_name,
            self.base_model.id,
            self.base_model.__dict__
        )
        self.assertEqual(expected_str, str(self.base_model))

    def test_save_method(self):
        """
        Test the 'save' method to ensure 'updated_at' is updated.
        """
        old_date = self.base_model.updated_at
        self.base_model.save()
        new_date = self.base_model.updated_at
        self.assertNotEqual(old_date, new_date)

    def test_to_dict_method(self):
        """
        Test the 'to_dict' method to ensure correct dictionary representation.
        """
        data = self.base_model.to_dict()
        self.assertIsInstance(data, dict)
        self.assertIn('__class__', data)
        self.assertIn('created_at', data)
        self.assertIn('updated_at', data)
        self.assertEqual(data['__class__'], self.base_model.__class__.__name__)

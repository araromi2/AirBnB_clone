#!/usr/bin/python3

import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def test_init(self):
        """Test instantiation"""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))
        self.assertEqual(base.id, str(uuid.uuid4()))
        self.assertEqual(base.created_at, base.updated_at)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)

    def test_str(self):
        """Test the __str__ method"""
        base = BaseModel()
        string = "[{}] ({}) {}".format(base.__class__.__name__, base.id, base.__dict__)
        self.assertEqual(string, str(base))

    def test_save(self):
        """Test the save method"""
        base = BaseModel()
        old_updated_at = base.updated_at
        base.save()
        self.assertNotEqual(old_updated_at, base.updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertIn('id', base_dict)
        self.assertIn('created_at', base_dict)
        self.assertIn('updated_at', base_dict)
        self.assertIn('__class__', base_dict)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertEqual(base_dict["created_at"], base.created_at.isoformat())
        self.assertEqual(base_dict["updated_at"], base.updated_at.isoformat())

if __name__ == "__main__":
    unittest.main()
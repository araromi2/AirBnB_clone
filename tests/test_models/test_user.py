import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up test objects"""
        self.user = User()

    def tearDown(self):
        """Clean up after each test"""
        del self.user

    def test_user_inherits_from_base_model(self):
        """Test if User class inherits from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_user_attributes(self):
        """Test if User instance has the expected attributes"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_user_attributes_initial_values(self):
        """Test if User instance attributes have initial values"""
        self.assertEqual(self.user.email, '')
        self.assertEqual(self.user.password, '')
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')

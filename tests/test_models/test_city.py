#!/usr/bin/python3
"""
Unit tests for the City class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class
    """
    def test_attributes(self):
        """
        Test the attributes of City class
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

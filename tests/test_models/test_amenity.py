#!/usr/bin/python3
"""
Unit tests for the Amenity class
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class
    """
    def test_attributes(self):
        """
        Test the attributes of Amenity class
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

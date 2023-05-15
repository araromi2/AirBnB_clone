#!/usr/bin/python3
"""
Unit tests for the State class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class
    """
    def test_attributes(self):
        """
        Test the attributes of State class
        """
        state = State()
        self.assertEqual(state.name, "")

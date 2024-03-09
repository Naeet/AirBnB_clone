#!/usr/bin/python3
"""
Module for Amenity class unittest
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity

class TestAmenity_instantiation(unittest.TestCase):
        """
            Unittests for testing instantiation of the Amenity class.
        """
    def setUp(self):
                try:
                    os.rename("file.json", "tmp.json")
                except FileNotFoundError:
                     pass


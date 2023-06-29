#!/usr/bin/python3
"""

"""
from contextlib import AbstractContextManager
import os
from typing import Any
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_with_str(self):
        b1 = Base("Hello")
        self.assertEqual("Hello", b1.id)

    def test_with_arg(self):
        b1 = Base(23)
        b2 = Base(55)
        self.assertEqual(b1.id, 23)
        self.assertEqual(b2.id, 55)

    def test_wit_none(self):
        b3 = Base(None)
        self.assertEqual(b3.id, 3)

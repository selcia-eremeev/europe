#!/usr/bin/env python
# coding: utf-8
""" Base class for Test """
import unittest

from europe.europe import Europe
from europe.utils.naming import Naming


class Base(unittest.TestCase):
    """ Base class for Test """

    def setUp(self) -> None:
        """ Setting up the test fixture before exercising it """
        self.europe = Europe()
        self.naming = Naming()

    def tearDown(self) -> None:
        """ Deconstructing the test fixture after testing it """
        self.europe.close()

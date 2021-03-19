#!/usr/bin/env python
# coding: utf-8
""" Test class for Sanity """
from loguru import logger
from tests.base.base import Base


class TestSanity(Base):
    """ Test class for Sanity """

    def test_sanity(self) -> None:
        """ Test Sanity
        Steps:
            #. Opens Europe
        """
        logger.info("[STEP] 1: Opens Europe")
        self.europe.open()

        logger.info("[EXPECTED] 1: Europe is displayed")
        assert self.europe.top.wait_for_page()

#!/usr/bin/env python
# coding: utf-8
""" Test class for Unit """
from loguru import logger
from tests.base.base import Base


class TestUnit(Base):
    """ Test class for Unit """

    def test_unit(self):
        logger.info("[STEP] 1: Opens Europe")
        self.europe.open()

        logger.info("[EXPECTED] 1: Europe is displayed")
        assert self.europe.top.wait_for_page()

        logger.info("[STEP] 2: Press Random button")
        self.europe.top.random_button.click()

        logger.info("[EXPECTED] 2: Random page is displayed")
        assert self.europe.top.random.wait_for_page()

        logger.info("[STEP] 3: Press Male button")
        self.europe.top.random.male_button.click()

        logger.info("[EXPECTED] 3: Male button is selected")
        assert self.europe.top.random.male_button.is_selected()

        logger.info("[STEP] 4: Press Female button")
        self.europe.top.random.female_button.click()

        logger.info("[EXPECTED] 4: Female button is selected")
        assert self.europe.top.random.female_button.is_selected()

        logger.info("[STEP] 5: Press English button")
        self.europe.top.random.english_button.click()

        logger.info("[EXPECTED] 5: English button is selected")
        assert self.europe.top.random.english_button.is_selected()

        logger.info("[STEP] 6: Press German button")
        self.europe.top.random.german_button.click()

        logger.info("[EXPECTED] 6: German button is selected")
        assert self.europe.top.random.german_button.is_selected()

        logger.info("[STEP] 7: Press French button")
        self.europe.top.random.french_button.click()

        logger.info("[EXPECTED] 7: French button is selected")
        assert self.europe.top.random.french_button.is_selected()

        logger.info("[STEP] 8: Press Italian button")
        self.europe.top.random.italian_button.click()

        logger.info("[EXPECTED] 8: Italian button is selected")
        assert self.europe.top.random.italian_button.is_selected()

        logger.info("[STEP] 9: Press Spanish button")
        self.europe.top.random.spanish_button.click()

        logger.info("[EXPECTED] 9: Spanish button is selected")
        assert self.europe.top.random.spanish_button.is_selected()

        logger.info("[STEP] 10: Press Swedish button")
        self.europe.top.random.swedish_button.click()

        logger.info("[EXPECTED] 10: Swedish button is selected")
        assert self.europe.top.random.swedish_button.is_selected()

        logger.info("[STEP] 11: Press Finnish button")
        self.europe.top.random.finnish_button.click()

        logger.info("[EXPECTED] 11: Finnish button is selected")
        assert self.europe.top.random.finnish_button.is_selected()

        logger.info("[STEP] 12: Press Russian button")
        self.europe.top.random.russian_button.click()

        logger.info("[EXPECTED] 12: Russian button is selected")
        assert self.europe.top.random.russian_button.is_selected()

        logger.info("[STEP] 13: Press Czech button")
        self.europe.top.random.czech_button.click()

        logger.info("[EXPECTED] 13: Czech button is selected")
        assert self.europe.top.random.czech_button.is_selected()

        logger.info("[STEP] 14: Press Dutch button")
        self.europe.top.random.dutch_button.click()

        logger.info("[EXPECTED] 14: Dutch button is selected")
        assert self.europe.top.random.dutch_button.is_selected()

        logger.info("[STEP] 15: Press Submit button")
        self.europe.top.random.submit_button.click()

        logger.info("[EXPECTED] 15: Random Name is displayed")
        assert self.europe.top.random.wait_for_page()
        assert self.europe.top.random.firstname is not None
        assert self.europe.top.random.lastname is not None

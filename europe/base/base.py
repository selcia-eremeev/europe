#!/usr/bin/env python
# coding: utf-8
""" Base class of POM """
import logging
from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger(__name__)


class Base:
    """ Base class of POM """

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def wait_for_page(self, max_wait: int = 10) -> bool:
        """ Wait for all elements to be displayed
        Returns:
            bool: True if all elements are displayed, False otherwise
        """
        try:
            sleep(max_wait)
            return WebDriverWait(self.driver, max_wait).until(expected_conditions.presence_of_all_elements_located)
        except TimeoutException as e:
            logger.error(f"{self.__class__.__name__} page is not displayed", exc_info=e)

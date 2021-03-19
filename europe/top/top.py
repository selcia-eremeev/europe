#!/usr/bin/env python
# coding: utf-8
""" POM class for Top """
from selenium.webdriver.remote.webelement import WebElement
from europe.top.random.random import Random

from europe.base.base import Base


class Top(Base):
    """ POM class for Top """

    @property
    def random(self) -> Random:
        """ Returns Random instance """
        return Random(self.driver)

    @property
    def random_button(self) -> WebElement:
        """ Random button
        Returns:
            WebElement: Random button WebElement
        """
        return self.driver.find_element_by_class_name("nv_random")

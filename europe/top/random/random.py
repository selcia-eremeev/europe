#!/usr/bin/env python
# coding: utf-8
""" POM class for Random """
from selenium.webdriver.remote.webelement import WebElement

from europe.base.base import Base


class Random(Base):
    """ POM class for Random """

    @property
    def firstname(self) -> str:
        """ First name
        Returns:
            str: First name
        """
        return self.driver.find_element_by_class_name("fa").text

    @property
    def lastname(self) -> str:
        """ Last name
        Returns:
            str: Last name
        """
        return self.driver.find_element_by_class_name("la").text

    @property
    def male_button(self) -> WebElement:
        """ Gender male button
        Returns:
            WebElement: Gender male button WebElement
        """
        return self.driver.find_element_by_id("rand_prm_t_m")

    @property
    def female_button(self) -> WebElement:
        """ Gender female button
        Returns:
            WebElement: Gender female button WebElement
        """
        return self.driver.find_element_by_id("rand_prm_t_f")

    @property
    def english_button(self) -> WebElement:
        """ English button
        Returns:
            WebElement: English button WebElement
        """
        return self.driver.find_element_by_id("rand_prm_l_en")

    @property
    def german_button(self) -> WebElement:
        """ German button
        Returns:
            WebElement: German button WebElement
        """
        return self.driver.find_element_by_id("rand_prm_l_de")

    @property
    def french_button(self) -> WebElement:
        """ French button
        Returns:
            WebElement: French button WebElement
        """
        return self.driver.find_element_by_id("rand_prm_l_fr")

    @property
    def italian_button(self) -> WebElement:
        """ Italian button
        Returns:
            WebElement: Italian button WebElement
        """
        return self.driver.find_element_by_id("rand_prm_l_it")

    @property
    def spanish_button(self) -> WebElement:
        """ Spanish button
        Returns:
            WebElement: Spanish button WebElement
        """
        return self.driver.find_element_by_id("rand_prm_l_es")

    @property
    def swedish_button(self) -> WebElement:
        """ Swedish button
        Returns:
            WebElement: Swedish button WebElement
        """
        return self.driver.find_element_by_id("rand_prm_l_sv")

    @property
    def finnish_button(self) -> WebElement:
        """ Finnish button
        Returns:
            WebElement: Finnish button WebElement
        """
        return self.driver.find_element_by_id("rand_prm_l_fi")

    @property
    def russian_button(self) -> WebElement:
        """ Russian button
        Returns:
            WebElement: Russian button WebElement
        """
        return self.driver.find_element_by_id("rand_prm_l_ru")

    @property
    def czech_button(self) -> WebElement:
        """ Czech button
        Returns:
            WebElement: Czech button WebElement
        """
        return self.driver.find_element_by_id("rand_prm_l_cs")

    @property
    def dutch_button(self) -> WebElement:
        """ Dutch button
        Returns:
            WebElement: Dutch button WebElement
        """
        return self.driver.find_element_by_id("rand_prm_l_nl")

    @property
    def submit_button(self) -> WebElement:
        """ Submit button
        Returns:
            WebElement: Submit button WebElement
        """
        return self.driver.find_element_by_id("random_submit_full")

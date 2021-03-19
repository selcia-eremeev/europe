#!/usr/bin/env python
# coding: utf-8
""" Application class for Europe """
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from europe.top.top import Top

URL = "https://www.worldsys.org/europe/"
MAX_WAIT = 15


class Europe:
    """ Application class for Europe """

    def __init__(self) -> None:
        options = Options()
        options.add_argument("--headless")
        self.driver: WebDriver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(MAX_WAIT)

    @property
    def top(self) -> Top:
        """ Returns Top instance """
        return Top(self.driver)

    def open(self) -> None:
        self.driver.get(URL)

    def close(self) -> None:
        self.driver.quit()

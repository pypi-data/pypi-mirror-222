# FIXME: THIS SCRIPT IS NOTE WORKING #
# ================================== #
import random
import sys
import time

import rich
from playsound import playsound
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

URL = "xxxx"
EMAIL = "xxxx"
PASSWORD = "xxxx"


TEXT = "xxx"
import datetime
import os


class SeleniumAutomator:
    def __init__(self, headless=None):
        if headless is None:
            headless = True
        self._default_sleep_time = 3

        self.log("open driver")
        options = Options()
        if headless:
            options.headless = True
        self.driver = webdriver.Firefox(options=options)
        self._init_driver()

    # ========== #
    # PUBLIC API #
    # ========== #

    def get(self, url: str):
        self.log(f"Requesting url {url!r}")
        self.driver.get(url)
        self.sleep(msg="URL requested")

    def input(self, text: str, *, id=None):
        if id is None:
            raise ValueError(f"id must be provided")

        input_element = self.driver.find_element(By.ID, id)
        self._enter_text_slowly(input_element, text)

    def click(self, *, css_selector=None):
        if css_selector is None:
            raise ValueError(f"css_selector must be provided")

        input_element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        self.log(f"Clicking element {css_selector!r}")
        input_element.click()
        self.sleep(msg=f"Clicked element {css_selector!r}")

    # PRIVATE METHODS #
    # =============== #
    def log(self, *args, **kwargs):
        rich.print("[SeleniumAutomator]", *args, **kwargs)

    def _init_driver(self):
        self.sleep(10, msg="Waiting driver to init")
        if len(self.driver.window_handles) > 1:
            self.log("Cleaning TABs")
            for i_tab, tab_id in enumerate(self.driver.window_handles[1:], 2):
                self.log(f"Cleaning tab n°{i_tab}")
                self.driver.switch_to.window(tab_id)
                self.driver.close()
                self.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[0])

    def _pre_log(self, *args, **kwargs):
        pass

    def _post_log(self, *args, sleep=None, **kwargs):
        if sleep is None:
            sleep = self._default_sleep_time
        rich.print("[DONE]", *args, f". Sleeping {sleep}", **kwargs)
        time.sleep(sleep)

    def sleep(self, sleep=None, msg=None):
        if sleep is None:
            sleep = self._default_sleep_time
        if msg:
            self.log(msg, f". Sleeping {sleep} seconds...")

        time.sleep(sleep)

    def _enter_text_slowly(self, input_element, text, sleep_time=0.3):
        for char in text:
            input_element.send_keys(char)
            # Add a slight random variation to the sleep time
            sleep_time_with_variation = sleep_time + random.uniform(-0.1, 0.1)
            time.sleep(sleep_time_with_variation)
            sys.stdout.flush()

    def press_enter(self):
        self.log("Pressing enter")
        element = self.driver.find_element(By.TAG_NAME, "body")
        element.send_keys(Keys.RETURN)
        self.sleep(msg="Waiting after pressing enter")

    def notificiation(self):
        here = os.path.dirname(__file__)
        sound_path = os.path.join(here, "notification.wav")
        playsound(sound_path)

    def search(self, *, negative: str):
        if negative not in self.driver.page_source:
            self.log("Found the searched text!")
            self.notificiation()
            return True
        else:
            self.log("Don't found! sorry")
            return False


if __name__ == "__main__":
    found = False
    while not found:
        sa = SeleniumAutomator()

        sa.get(URL)
        sa.press_enter()
        sa.input(EMAIL, id="XXXX")
        sa.input(PASSWORD, id="XXXX")
        sa.click(css_selector="XXXX")
        sa.press_enter()
        sa.sleep()
        found = sa.search(negative=TEXT)
        print("Iteration ended....")
        print()
        if not found:
            sa.driver.close()
            time.sleep(60 * 5)

    if found:
        for i in range(10):
            sa.notificiation()


# TODO test me! ...

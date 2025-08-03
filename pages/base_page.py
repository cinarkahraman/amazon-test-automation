import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        time.sleep()

    def navigate_to(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except (TimeoutException, NoSuchElementException):
            return None

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        element = self.find_element(locator)
        if element:
            element.click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        if element:
            return element.text
        return ""

    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def go_back(self):
        self.driver.back()

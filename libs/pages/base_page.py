from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from Constants import TIMEOUT

class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
 

    def go_url(self, url):
        self.driver.get(url)

    def find_element(self, selector):
        try:
            return self.driver.find_element(selector[0], selector[1])
        except NoSuchElementException as e:
            raise e

    def element_to_be_clickable(self, selector):
        try:
            return WebDriverWait(self.driver, TIMEOUT).until(
                EC.element_to_be_clickable(selector))
        except TimeoutException  as e:
            raise e


    def visibility_of_element_located(self, selector):
        try:
            return WebDriverWait(self.driver, TIMEOUT).until(
                EC.visibility_of_element_located(selector))
        except TimeoutException  as e:
            raise e
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from libs.pages.base_page import BasePage            
from libs.pages.selectors.home_selectors import HomeSelectors
import time

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def send_value_input(self, text):
        input_text = self.find_element(HomeSelectors.text_input)
        input_text.clear()
        input_text.send_keys(text)
        #time.sleep(1)
    
    def get_number_words(self):
        number_words = self.visibility_of_element_located(HomeSelectors.number_words_span)
        return number_words.text.strip()


    
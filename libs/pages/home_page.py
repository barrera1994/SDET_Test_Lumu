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
        time.sleep(1)
    
    def get_number_words(self):
        number_words = self.visibility_of_element_located(HomeSelectors.number_words_span)
        return number_words.text.strip()
    
    def get_number_characters(self):
        number_characters = self.visibility_of_element_located(HomeSelectors.number_characters_span)
        return number_characters.text.strip()
    
    def get_rows_table_keyword_density(self):
        rows_table_density = self.find_elements(HomeSelectors.keyword_density_table_rows)
        return rows_table_density
    
    def get_keyword_density_word(self, row):
        value_word = row.find_element(HomeSelectors.keyword_density_table_word_col[0], HomeSelectors.keyword_density_table_word_col[1]).text.strip()
        return value_word
        
    def get_keyword_density_number(self, row):
        value_number = row.find_element(HomeSelectors.keyword_density_table_number_col[0], HomeSelectors.keyword_density_table_number_col[1]).text.strip()
        return value_number

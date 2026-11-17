from selenium.webdriver.common.by import By

class HomeSelectors:
    text_input = (By.ID, 'box')
    number_words_span = (By.ID, 'word_count')
    number_characters_span = (By.ID, 'character_count')
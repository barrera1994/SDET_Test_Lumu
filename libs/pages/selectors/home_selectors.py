from selenium.webdriver.common.by import By

class HomeSelectors:
    text_input = (By.ID, 'box')
    number_words_span = (By.ID, 'word_count')
    number_characters_span = (By.ID, 'character_count')
    keyword_density_table_rows = (By.CSS_SELECTOR, '#kwd-accordion-data .list-group-item')
    keyword_density_table_rows_col = (By.CSS_SELECTOR, '#kwd-accordion-data .list-group-item .word')
    keyword_density_table_word_col = (By.CSS_SELECTOR, '.word')
    keyword_density_table_number_col = (By.CSS_SELECTOR, '.badge')
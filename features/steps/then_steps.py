from behave import then
from hamcrest import equal_to, assert_that

@then('the number of words should be "{number_words}"')
def step_number_words(context, number_words):
    get_number_words = context.homePage.get_number_words()
    assert_that(get_number_words, equal_to(number_words), f"se esperaba {number_words} palabras pero se obtuvo {get_number_words} palabras")

@then('the number of characters should be "{number_characters}"')
def step_number_characters(context, number_characters):
    get_number_characters = context.homePage.get_number_characters()
    assert_that(get_number_characters, equal_to(number_characters), f"se esperaba {number_characters} caracteres pero se obtuvo {get_number_characters} caracteres")

@then('the 3 most frequently repeated words are:')
def step_top3_words(context):
    rows_table_keyword_density = context.homePage.get_rows_table_keyword_density()

    for i in range(len(rows_table_keyword_density)):
        if i==3:
            break
        word=context.homePage.get_keyword_density_word(rows_table_keyword_density[i])
        word_expected=context.table[i]["word_top"]
        assert_that(word, equal_to(word_expected), f'palabra top{i+1} esperada: {word_expected} pero llego {word}')
        
        number_word_repeated=context.homePage.get_keyword_density_number(rows_table_keyword_density[i])
        repeated_word_expected=context.table[i]["number"]
        assert_that(number_word_repeated.split()[0], equal_to(repeated_word_expected), f'Numero de repeticiones top{i+1} esperado: {repeated_word_expected} pero llego {number_word_repeated}')
        

@then('I clear the text field')
def step_number_words(context):
    context.homePage.clear_text_field()
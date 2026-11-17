from behave import then, use_step_matcher
from hamcrest import equal_to, assert_that

use_step_matcher("re")

@then(u'the number of words should be "(?P<number_words>.*)"')
def step_impl(context, number_words):
    get_number_words = context.homePage.get_number_words()
    assert_that(get_number_words, equal_to(number_words), f"se esperaba {number_words} palabras pero se obtuvo {get_number_words} palabras")

@then(u'the number of characters should be "(?P<number_characters>.*)"')
def step_impl(context, number_characters):
    get_number_characters = context.homePage.get_number_characters()
    assert_that(get_number_characters, equal_to(number_characters), f"se esperaba {number_characters} caracteres pero se obtuvo {get_number_characters} caracteres")
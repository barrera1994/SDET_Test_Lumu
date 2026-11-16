from behave import then, use_step_matcher
from hamcrest import equal_to, assert_that

use_step_matcher("re")

@then(u'the number of words should be "(?P<number_words>.*)"')
def step_impl(context, number_words):
    get_number_words = context.homePage.get_number_words()
    assert_that(get_number_words, equal_to(number_words), "The number of words does not match")

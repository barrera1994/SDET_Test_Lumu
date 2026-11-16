from behave import when, use_step_matcher

use_step_matcher("re")

@when(u'I type the text "(?P<text>.*)"')
def visit_login(context, text):
    return context.homePage.send_value_input(text)
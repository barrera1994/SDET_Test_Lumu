from behave import when,use_step_matcher

use_step_matcher("re")

@when('I type the text "(.*)"')
def step_type_text(context, text):
    return context.homePage.send_value_input(text)
from behave import when

@when('I type the text "{text}"')
def step_type_text(context, text):
    return context.homePage.send_value_input(text)
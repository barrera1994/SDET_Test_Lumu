from behave import given

@given('I navigate to the "{url}" url')
def step_go_url(context, url):
    #if context.driver.current_url != url:
        return context.basePage.go_url(url)

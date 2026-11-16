from selenium import webdriver
from libs.pages.base_page import BasePage
from libs.pages.home_page import HomePage

def before_all(context):
    context.driver=webdriver.Chrome()
    context.driver.maximize_window()
    context.basePage = BasePage(context.driver)
    context.homePage = HomePage(context.driver)

def after_all(context):
    if context.driver is not None:
        context.driver.quit()
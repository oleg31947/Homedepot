from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep
SEARCH_FIELD = (By.CSS_SELECTOR, "input#headerSearch.SearchBox__input")

class SearchResults(Page):
    # def __init__(self, driver):
    #     self.driver = driver

    @when("Input {product} in search field")
    def insert_group_keyword(context, product):
        search = context.driver.find_element(*SEARCH_FIELD)
        search.clear()
        search.send_keys(product)
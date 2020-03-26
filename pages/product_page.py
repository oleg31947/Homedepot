from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class Product(Page):
    # RESULTS_FOUND = (By.CSS_SELECTOR, "div#breadcrumb")
    # RESULTS_FOUND = (By.CSS_SELECTOR, "h1.h1-style-tag")
    RESULTS_FOUND = (By.CSS_SELECTOR, "h1 span.original-keyword")

    def verify_result_search(self, text):
        #self.verify_text(text, *self.RESULTS_FOUND)
        self.verify_text(text, *self.RESULTS_FOUND)
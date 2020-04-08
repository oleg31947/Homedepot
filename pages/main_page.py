from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep

class MainPage(Page):
    CLICK_OBJECT = (By.CSS_SELECTOR, "div.Header3__groupItem.Header3__groupItem--center a#headerMyAccount")
    BTN = (By.CSS_SELECTOR, "button#headerSearchButton")

    def open_home_page(self):
        self.open_url()

    def click_wait(self):
        #context.driver.wait.until(EC.element_to_be_clickable(BTN)).click()
        self.click(*self.BTN)

    def click_account(self):
        self.click(*self.CLICK_OBJECT)








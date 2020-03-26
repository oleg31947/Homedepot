from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class SignIn(Page):
    REGISTER = (By.XPATH, ".//span[contains(text(),'Register')]")
    E_MAIL = (By.CSS_SELECTOR, "input#email")
    PASSWORD = (By.CSS_SELECTOR, "input#password-input-field")
    ZIP = (By.CSS_SELECTOR, "input#zipCode")
    PHONE = (By.CSS_SELECTOR, "input#phone")
    SUBMIT = (By.XPATH, ".//span[contains(text(),'Create an Account')]")
    YOU_REGISTERED = (By.XPATH, "//p[@class='u__bold u__text-align--center u__husky']")


    def click_register(self):
        self.click(*self.REGISTER)

    def fill_out_email(self, text):
        self.input_text(text, *self.E_MAIL)

    def fill_password(self, text):
        self.input_text(text, *self.PASSWORD)

    def fill_zip(self, text):
        self.input_text(text, *self.ZIP)

    def fill_phone(self, text):
        self.input_text(text, *self.PHONE)


    def click_submit(self):
        self.click(*self.SUBMIT)

    def verify_registration(self, text, ):
        self.verify_text(text, *self.YOU_REGISTERED)

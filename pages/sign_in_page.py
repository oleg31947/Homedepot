from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep
import requests


class SignIn(Page):
    REGISTER = (By.CSS_SELECTOR, "a.bttn-outline")
    CART = (By.CSS_SELECTOR, "a#headerCart span.MyCart__label")
    E_MAIL = (By.CSS_SELECTOR, "input#email")
    PASSWORD = (By.CSS_SELECTOR, "input#password-input-field")
    ZIP = (By.CSS_SELECTOR, "input#zipCode")
    PHONE = (By.CSS_SELECTOR, "input#phone")
    SUBMIT = (By.XPATH, ".//span[contains(text(),'Create an Account')]")
    YOU_REGISTERED = (By.XPATH, "//p[@class='u__bold u__text-align--center u__husky']")
    EMAIL_REGISTERED = (By.CSS_SELECTOR, "span.alert-inline__message")
    # SIGN_OUT = (By.CSS_SELECTOR, "a#signOut")
    SIGN_OUT = (By.XPATH, ".//a[@title='Sign Out']")
    VERIFY_BY_MOBILE = (By.CSS_SELECTOR, "label[for='verify-phone-checkbox'].checkbox-btn__label-test")

    def click_register(self):
        self.click(*self.REGISTER)

    def click_cart(self):
        self.click(*self.CART)

    def fill_out_email(self, text):
        self.input_text(text, *self.E_MAIL)

    def fill_password(self, fake_password):
        self.input_text(fake_password, *self.PASSWORD)

    def fill_zip(self, text):
        self.input_text(text, *self.ZIP)

    def fill_phone(self, text):
        self.input_text(text, *self.PHONE)

    def verify_by_mobile(self):
        self.click(*self.VERIFY_BY_MOBILE)

    def click_submit(self):
        self.click(*self.SUBMIT)

    def verify_registration(self, text):
        self.verify_exactly_text(text, *self.YOU_REGISTERED)

    # def verify_email_registred(self, text):
    #     self.verify_exactly_text(text, *self.EMAIL_REGISTERED)

    def verify_change_windows(self, url):
        self.verify_change_wind(url)

    # def sign_out_click(self):
    #     self.click(*self.SIGN_OUT)

    def check_sign_out(self, text2):
        self.retrieve_text(text2, *self.SIGN_OUT)

    def verify_log_in(self, url):
        self.verify_login(url)
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
import requests

@when("Click on search button and wait a couple of seconds")
def click_wait(context):
    context.app.main_page.click_wait()

@given("Open Homedepot page")
def auto_suggestion_works(context):
    context.driver.get("https://www.homedepot.com/")

@when("Click account button")
def click(context):
    context.app.main_page.click_account()

@when("Click 'register' button")
def click_register(context):
    context.app.sign_in_page.click_register()

@when("Fill email field with {fake_email}")
def fill_out_email(context, fake_email):
    context.app.sign_in_page.fill_out_email(fake_email)

@when("Fill password field with {fake_password}")
def fill_out_password(context, fake_password):
    context.app.sign_in_page.fill_password(fake_password)

@when("Fill zip code field with {fake_zip}")
def fill_out_zip(context, fake_zip):
    context.app.sign_in_page.fill_password(fake_zip)

@when("Fill Phone field with {fake_phone}")
def fill_out_phone(context, fake_phone):
    context.app.sign_in_page.fill_password(fake_phone)

@when("Verify my mobile number, click")
def verify_by_mobile(context):
    context.app.sign_in_page.verify_by_mobile()

@when("Click Submit")
def click_submit(context):
    context.app.sign_in_page.click_submit()

@when("Check button {text2}")
def check_sign_out(context, text2):
    context.app.sign_in_page.check_sign_out(text2)


# @then("Verify {text}")
# def verify_email_registred(context, text):
#     context.app.sign_in_page.verify_email_registred(text)

@then("Expected registration will be complete successfully {url}")
def verify_registration_url(context, url):
    context.app.sign_in_page.verify_change_windows(url)

@then ("Expected login will be complete successfully {url}")
def verify_log_in(context, url):
    context.app.sign_in_page.verify_log_in(url)

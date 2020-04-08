from behave import given, when, then
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
# from numpy.core import number
import requests


@when("Click on search button and wait a couple of seconds")
def click_wait(context):
    context.app.main_page.click_wait()

# @given("Open Homedepot page")
# def open_homedepot_page(context):

@given("Open Homedepot page")
def open_home_page(context):
    # context.driver.get("https://www.homedepot.com/")
    context.app.main_page.open_home_page()

@when("Click account button")
def click(context):
    context.app.main_page.click_account()

@when("Click 'register' button")
def click_register(context):
    context.app.sign_in_page.click_register()

@when("Click 'cart' button")
def click_cart(context):
    context.app.sign_in_page.click_cart()

@when("Fill email field with {fake_email}")
def fill_out_email(context, fake_email):
    context.app.sign_in_page.fill_out_email(fake_email)

@when("Fill password field with {fake_password}")
def fill_out_password(context, fake_password):
    context.app.sign_in_page.fill_password(fake_password)

@when("Fill zip code field with {fake_zip}")
def fill_out_zip(context, fake_zip):
    context.app.sign_in_page.fill_zip(fake_zip)

@when("Fill Phone field with {fake_phone}")
def fill_out_phone(context, fake_phone):
    context.app.sign_in_page.fill_phone(fake_phone)

@when("Verify my mobile number, click")
def verify_by_mobile(context):
    context.app.sign_in_page.verify_by_mobile()

@when("Click Submit")
def click_submit(context):
    context.app.sign_in_page.click_submit()

@when("Check button {text2}")
def check_sign_out(context, text2):
    context.app.sign_in_page.check_sign_out(text2)

@when("Insert {product} in search field")
def search_product(context, product):
    context.app.product_page.search_product(product)

@when("{expected_text} product added to shopping cart")
def add_product_cart(context, expected_text):
    expected_text = int(expected_text)
    context.app.product_page.add_product_cart(expected_text)

@when("Return to product search page")
def return_product_search_page(context):
    context.app.product_page.return_product_page()

# @when("On search results page choose another product and click it")
# def wait_until_new_windows_open(context):
#     context.app.product_page.wait_until_iframe_not_visible()
#

@then("Count them. {step}")
def count_assert(context, step):
    context.app.product_page.count_assert(step)
    # context.after_step_page()

@then("Expect {expected_text}")
def verify_product_in_cart(context, expected_text):
    # expected_text = int(expected_text)
    context.app.product_page.verify_product_in_cart(expected_text)

# @then("Close all pop-ups")
# def close_all_pop_ups(context):
#     context.app.product_page.close_all_pop_ups()


# @then("Verify {text}")
# def verify_email_registred(context, text):
#     context.app.sign_in_page.verify_email_registred(text)

@then("Expected registration will be complete successfully {url}")
def verify_registration_url(context, url):
    context.app.sign_in_page.verify_change_windows(url)

@then ("Expected login will be complete successfully {url}")
def verify_log_in(context, url):
    context.app.sign_in_page.verify_log_in(url)

@then("Expected cart page will have empty in the title{expected_text}")
def verify_empty_cart(context, expected_text):
    context.app.product_page.verify_empty_cart(expected_text)


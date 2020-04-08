from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# RESULTS_FOUND = (By.CSS_SELECTOR, "div#breadcrumb")
# RESULTS_FOUND = (By.CSS_SELECTOR, "h1.h1-style-tag")
# RESULTS_FOUND = (By.CSS_SELECTOR, "h1 span.original-keyword")
RESULTS_FOUND = (By.CSS_SELECTOR, "div.page-header.u__truncate")


@then("Verify {search_words} is shown.")
def verify_result_search(context, search_words):
    #name_result = context.driver.find_elements(*RESULTS_FOUND)[0].text
    # name_result = context.driver.wait.until(EC.presence_of_all_elements_located(RESULTS_FOUND))[0].text
    name_result = context.driver.wait.until(EC.visibility_of_any_elements_located(RESULTS_FOUND))[0].text

    print(f" Actual result are:  {name_result}")
    print(f" Expected result is: {search_words}")

    assert search_words in name_result, f'Expected word {search_words} in message, but got {name_result}.'

    # e = 0
    # if step.status == 'true':
    #     e += 1
    # return (print(f'We actualy have {e} items'))
    # # if assert is True:

    # return sum(assert True)

# @then("Count serched items")
# def count_serched_items(contect, )

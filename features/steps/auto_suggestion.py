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
    #context.app.product_page.verify_result_search(search_words)
    #name_result = context.driver.find_elements(*RESULTS_FOUND)[0].text

    name_result = context.driver.wait.until(EC.presence_of_all_elements_located(RESULTS_FOUND))[0].text
    print(f" '/n {name_result}")


    # print(f" '/n actual {name_result}")
    # print(f" '/n expected {search_words}")
    #
    assert search_words in name_result, f'Expected word {search_words} in message, but got {name_result}.'
    # # if assert is True:

    # return sum(assert True)

# @then("Count serched items")
# def count_serched_items(contect, )

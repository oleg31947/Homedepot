from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
import requests

class Page:
    def __init__(self, driver):
       self.driver = driver
       self.base_url = 'https://www.homedepot.com/'
       self.waite = WebDriverWait(self.driver, 15)
       self.driver.implicitly_wait(10)
       self.action = ActionChains(self.driver)

    def simple_click(self, *locator):
        self.driver.find_element(*locator).click()

    def click(self, *locator):
        e = self.driver.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    # def wait_for_element_click(self, *locator):
    #     e = self.driver.wait.until(EC.element_to_be_clickable(locator))
    #     e.click()

    def multy_click(self, *locator):
        # self.driver.find_elements(*locator)[2].click()
        self.driver.wait.until(EC.visibility_of_all_elements_located(locator))[0].click()
    #
    # def find_element(self, *locator):
    #     return self.driver.find_element(*locator)
    #

    #
    # def wait_for_element_disappear(self, *locator):
    #     self.driver.wait.until(EC.invisibility_of_element(locator))
    #
    # def wait_for_element_appear(self, *locator):
    #     self.driver.wait.until(EC.presence_of_element_located(locator))
    #
    # def input_number(self, number, *locator):
        # e = self.driver.wait.until(EC.element_to_be_clickable(locator))
        #e = self.driver.find_elements(*locator)[0]
        # e = self.driver.wait.until(EC.visibility_of_all_elements_located(locator))[0]
        # e = self.driver.find_elements(*locator)[-3]
        # e.click()
        # e.clear()
        # e.send_keys(number)

    def input_text(self, product, *locator):
        e = self.driver.wait.until(EC.visibility_of_element_located(locator))
        e.clear()
        e.send_keys(product)

    def open_url(self):
        self.driver.get(self.base_url)

    def open_page(self, url=' '):
        self.driver.get(self.base_url + url)

    def retrieve_text(self, text2, *locator):
        text_text = self.driver.find_element(*locator).text
        # return text_text
        if text2 in text_text:
            self.driver.find_element(*locator).click()
        else:
            pass


    # def verify_one_text(self, expected_text, *locator):
    #     actual_text = self.driver.wait.until(EC.visibility_of_element_located(locator)).text
    #     # actual_text = self.driver.wait.until(EC.presence_of_element_located(locator).text
    #     print(f'Actual {actual_text}')
    #     print(type(actual_text))
    #     print(f'expected {expected_text}')
    #     print(type(expected_text))
    #     assert expected_text in actual_text, f'Expected text {expected_text}, but got {actual_text}'

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_elements(*locator)[0].text
        print(f'actual {actual_text}')
        print(type(actual_text))
        print(f'expected {expected_text}')
        print(type(expected_text))
        assert expected_text in actual_text, f'Expected text {expected_text}, but got {actual_text}'

    def verify_exactly_text(self, expected_text, *locator):
        actual_text = self.driver.wait.until(EC.visibility_of_any_elements_located(locator))[0].text
        # actual_text = self.driver.wait.until(EC.presence_of_element_located(locator)).text
        print(f'Actual result is: {actual_text}')
        print(type(actual_text))
        print(f'Expected result is: {expected_text}')
        print(type(expected_text))
        assert expected_text == actual_text, f'Expected text: {expected_text}, but got: {actual_text}'

    def verify_change_wind(self, url):
        self.driver.wait.until(EC.new_window_is_opened)
        current_url = self.driver.current_url
        assert current_url != url, f'Expected result was {current_url} not equal {url}'

    def verify_login(self, url):
        x = requests.get(url)
        print(x.status_code)
        assert (400 <= x.status_code <= 499), f'Expected result is 400 but got (x.status_code)'

    # def product_in_cart(self, *locator):
    #     self.driver.wait.until(EC.new_window_is_opened)
    #     self.find_elements(*locator)


    def after_step_page(self, step):
        e = 0
        if step.status == 'trued':
            e += 1
        return print(f'We actualy have {e} items')
        #print('\nStep failed: ', step)

    # def count_positive_passed_assert(self, step):
    #
    #     if step.status == 'true':
    #         e += 1
    #     return (print(f'We actualy have {e} items'))
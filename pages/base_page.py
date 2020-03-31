from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
import requests

class Page:
    def __init__(self, driver):
       self.driver = driver
       self.base_url = "https://www.homedepot.com/"
       self.waite = WebDriverWait(self.driver, 15)
       self.action = ActionChains(self.driver)

    def click(self, *locator):
        e = self.driver.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def simple_click(self, *locator):
        self.driver.find_element(*locator).click()
    #
    # def find_element(self, *locator):
    #     return self.driver.find_element(*locator)
    #
    # def wait_for_element_click(self, *locator):
    #     e = self.driver.wait.until(EC.element_to_be_clickable(locator))
    #     e.click()
    #
    # def wait_for_element_disappear(self, *locator):
    #     self.driver.wait.until(EC.invisibility_of_element(locator))
    #
    # def wait_for_element_appear(self, *locator):
    #     self.driver.wait.until(EC.presence_of_element_located(locator))
    #
    def input_text(self, text, *locator):
        e = self.driver.wait.until(EC.element_to_be_clickable(locator))
        e.clear()
        e.send_keys(text)


    def retrieve_text(self, text2, *locator):
        text_text = self.driver.find_element(*locator).text
        # return text_text
        if text2 in text_text:
            self.driver.find_element(*locator).click()
        else:
            pass


    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator)[0].text
        print(f'actual {actual_text}')
        print(f'expected {expected_text}')
        assert expected_text == actual_text, f'Expected text {expected_text}, but got (actual_text)'

    def verify_exactly_text(self, expected_text, *locator):
        actual_text = self.driver.wait.until(EC.presence_of_element_located(locator)).text
        print(f'actual result is: {actual_text}')
        print(f'expected result is: {expected_text}')
        assert expected_text in actual_text, f'Expected text {expected_text}, but got (actual_text)'

    def verify_change_wind(self, url):
        self.driver.wait.until(EC.new_window_is_opened)
        current_url = self.driver.current_url
        assert current_url != url, f'Expected result was {current_url} not equal {url}'

    def verify_login(self, url):
        x = requests.get(url)
        print(x.status_code)
        assert (400 <= x.status_code <= 499), f'Expected result is 200 but got (x.status_code)'



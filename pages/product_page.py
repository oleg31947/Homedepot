from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from pages.base_page import Page
from time import sleep


class Product(Page):

    RESULTS_FOUND = (By.CSS_SELECTOR, "h1 span.original-keyword")
    EMTY_CART = (By.XPATH, ".//div[@id='root']//p[text()='Your shopping cart is empty.']")
    SEARCH_FILD_SECOND = (By.ID, "#headerSearch")
    SEARCH_FILD = (By.CSS_SELECTOR, "input.SearchBox__input#headerSearch")
    SEARCH_CLICK = (By.CSS_SELECTOR, "button#headerSearchButton")
    SEARCH_CLICK_SECOND = (By.CSS_SELECTOR,"button#headerSearchButton")
    ADD_CART = (By.XPATH, ".//div[@class=' pod-plp__atc-bttn']//span[text()='Add to Cart']")
    QUANTITY_WINDOW = (By.CSS_SELECTOR, "div.quantity__input")
    SECOND_ADD_CART = (By.XPATH, ".//span[@class='bttn__content'][text()='Add To Cart']")
    ADDED_TO_CART = (By.XPATH, ".//header//span[text()='1 Item Added to Cart']")
    FRAME = (By.CSS_SELECTOR, "iframe.thd-overlay-frame")
    IFRAME_CLOSE = (By.CSS_SELECTOR, "div.col__2-12.u__text-align--right")


    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FILD)
        self.click(*self.SEARCH_CLICK)

    def search_product_second(self, product):
        self.input_text(product, *self.SEARCH_FILD_SECOND)
        self.click(*self.SEARCH_CLICK)

    def add_product_cart(self, expected_text):
        self.multy_click(*self.ADD_CART)



    def verify_product_in_cart(self, expected_text):
        frame = self.driver.find_elements(*self.FRAME)[1]
        self.driver.switch_to.frame(frame)

        self.verify_exactly_text(expected_text, *self.ADDED_TO_CART)
        # self.verify_one_text(expected_text, *self.ADDED_TO_CART)
        sleep(7)


        self.driver.find_element(*self.IFRAME_CLOSE).click()

        # self.driver.switch_to_default_content()


    # def wait_until_iframe_not_visible(self):


    # def close_all_pop_ups(self):
    #     alert = self.driver.switch_to.alert
    #     if alert.is_displayed():
    #         alert.accept()




        # self.driver.wait.until(EC.new_window_is_opened)
        # self.input_number(number, *self.QUANTITY_WINDOW)
        # sleep(4)
        # self.click(*self.SECOND_ADD_CART)


    def verify_result_search(self, text):
        self.verify_text(text, *self.RESULTS_FOUND)

    def verify_empty_cart(self, expected_text):
        self.verify_exactly_text(expected_text, *self.EMTY_CART)

    # def verify_product_in_cart(self):

    def count_assert(self, step):
        self.after_step_page(step)
        # self.count_positive_passed_assert()


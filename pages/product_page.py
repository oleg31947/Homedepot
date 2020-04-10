from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from pages.base_page import Page
from time import sleep


class Product(Page):

    RESULTS_FOUND = (By.CSS_SELECTOR, "h1 span.original-keyword")
    SEARCH_FILD_SECOND = (By.CSS_SELECTOR, "input#headerSearch")
    # SEARCH_FILD = (By.CSS_SELECTOR, "input.SearchBox__input#headerSearch")
    SEARCH_CLICK = (By.CSS_SELECTOR, "button#headerSearchButton")
    SEARCH_CLICK_SECOND = (By.CSS_SELECTOR,"button#headerSearchButton")
    ADD_CART = (By.XPATH, ".//div[@class=' pod-plp__atc-bttn']//span[text()='Add to Cart']")
    QUANTITY_WINDOW = (By.CSS_SELECTOR, "div.quantity__input")
    SECOND_ADD_CART = (By.XPATH, ".//span[@class='bttn__content'][text()='Add To Cart']")
    ADDED_TO_CART = (By.XPATH, ".//header//span[text()='1 Item Added to Cart']")
    FRAME = (By.CSS_SELECTOR, "iframe.thd-overlay-frame")
    IFRAME_CLOSE = (By.CSS_SELECTOR, "div.col__2-12.u__text-align--right")
    # IFRAME_CLOSE = (By.CSS_SELECTOR, "svg[viewBox='0 0 32 32']")
    CART_BUTTON = (By.CSS_SELECTOR, "a#headerCart")
    QUANTITY_WINDOWS = (By.CSS_SELECTOR, "input.cartItem__qtyInput.form-input__field.u__left.padding_left-10.padding_right-10")
    CHECK_OUT = (By.XPATH, ".//div[@data-automation-id='appCheckoutOptionsContainer']//span[text()='Checkout ']")
    # VIEW_CART = (By.CSS_SELECTOR, "section span#editCartLinkItemCount")
    VIEW_CART = (By.CSS_SELECTOR, "a#headerCart span.MyCart__itemCount")
    PRODUCT_STARS = (By.CSS_SELECTOR, "div a span.stars")
    WRITE_BUTTON = (By.XPATH, ".//button//span[text()='Write a Review']")
    WRITE_TEXT = (By.XPATH, ".//h2[text()='Write A Review']")


    def search_product(self, product):
        # self.driver.wait.until(EC.new_window_is_opened)
        sleep(2)
        self.input_text(product, *self.SEARCH_FILD_SECOND)
        self.click(*self.SEARCH_CLICK)

    # def search_product_second(self, product):
    #     self.input_text(product, *self.SEARCH_FILD_SECOND)
    #     self.click(*self.SEARCH_CLICK)

    def add_product_cart(self, expected_text):
        self.multy_click(*self.ADD_CART)



    def verify_product_in_cart(self, expected_text):
        frame = self.driver.find_elements(*self.FRAME)[1]
        self.driver.switch_to.frame(frame)
        self.verify_exactly_text(expected_text, *self.ADDED_TO_CART)
        # self.verify_one_text(expected_text, *self.ADDED_TO_CART)
        # sleep(7)
        # self.driver.find_element(*self.IFRAME_CLOSE).click()
        self.driver.wait.until(EC.visibility_of_element_located(self.IFRAME_CLOSE)).click()
        # self.driver.switch_to_default_content()

    def return_product_page(self):
        frame = self.driver.find_elements(*self.FRAME)[1]
        self.driver.wait.until(EC.frame_to_be_available_and_switch_to_it(frame))
        # self.driver.switch_to.frame(frame)
        sleep(3)
        # self.driver.find_element(*self.IFRAME_CLOSE).click()
        self.driver.wait.until(EC.visibility_of_element_located(self.IFRAME_CLOSE)).click()

    def click_cart_button(self):
        # self.driver.switch_to_default_content()
        sleep(3)
        self.simple_click(*self.CART_BUTTON)
        # self.click(*self.CART_BUTTON)


    def click_review_button(self):
        sleep(2)
        self.multy_click(*self.WRITE_BUTTON)


    def change_quantity(self, number_1, number_2):
        if number_1 == 1:
            number_1 = 'True'
        else:
            self.input_text(number_1, *self.QUANTITY_WINDOWS)
        self.input_text(number_2, *self.QUANTITY_WINDOWS)


    def expect_items_in_cart(self, items):
        self.multy_click(*self.CHECK_OUT)

        # alert = self.driver.switch_to.alert
        # if alert.is_displayed():
        #     alert.dismiss()

        # self.driver.wait.until(EC.alert_is_present)
        # self.driver.switch_to.alert().dismiss()
        self.driver.back()
        self.verify_exactly_text(items, *self.VIEW_CART)

    # def close_all_pop_ups(self):
    #     alert = self.driver.switch_to.alert
    #     if alert.is_displayed():
    #         alert.accept()

    def click_stars(self):
        self.multy_click(*self.PRODUCT_STARS)
        self.driver.wait.until(EC.new_window_is_opened)


        # self.driver.wait.until(EC.new_window_is_opened)
        # self.input_number(number, *self.QUANTITY_WINDOW)
        # sleep(4)
        # self.click(*self.SECOND_ADD_CART)


    def verify_result_search(self, text):
        self.verify_text(text, *self.RESULTS_FOUND)

    def verify_empty_cart(self, expected_text):
        self.verify_exactly_text(expected_text, *self.CART_BUTTON)

    def product_button(self, name):
        self.verify_exactly_text(name, *self.WRITE_TEXT)

    # def verify_product_in_cart(self):

    # def count_assert(self, step):
    #     self.after_step_page(step)
    #     # self.count_positive_passed_assert()


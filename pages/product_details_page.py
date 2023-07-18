from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class ProductDetailsPage(Page):

    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".button--full-width[name='add']")
    VIEW_CART_BTN = (By.XPATH, "//a[contains(text(), 'View cart')]")
    CHECKOUT_BTN = (By.CSS_SELECTOR, ".button[name='checkout']")

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def verify_confirmation(self):
        sleep(1)
        e = self.wait_for_element_appear(*self.CHECKOUT_BTN)
        assert e.is_displayed(), f"element {e} is not displayed"
        # self.wait_for_element_clickable(*self.VIEW_CART_BTN)

    def click_view_my_cart(self):
        self.wait_for_element_click(*self.VIEW_CART_BTN)

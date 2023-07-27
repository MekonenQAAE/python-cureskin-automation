from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class ProductDetailsPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".button--full-width[name='add']")
    VIEW_CART_BTN = (By.XPATH, "//a[contains(text(), 'View cart')]")
    CHECKOUT_BTN = (By.CSS_SELECTOR, ".button[name='checkout']")
    CART_ICON = (By.ID, "cart-icon-bubble")
    CART_VAL = (By.CSS_SELECTOR, ".quantity__input")

    def click_add_to_cart(self):
        self.wait_for_element_click(*self.ADD_TO_CART_BTN)
        sleep(2)
        self.wait_for_element_click(*self.CART_ICON)
    def verify_confirmation(self):

        cart_val = self.find_element(*self.CART_VAL).get_attribute('value')
        assert int(cart_val) == 1, f"shopping cart has more than one items"

        e = self.wait_for_element_appear(*self.CHECKOUT_BTN)
        assert e.is_displayed(), f"element {e} is not displayed"


    def click_view_my_cart(self):
        self.wait_for_element_click(*self.VIEW_CART_BTN)

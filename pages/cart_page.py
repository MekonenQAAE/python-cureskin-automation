from pages.base_page import Page
from selenium.webdriver.common.by import By

class CartPage(Page):
    CART_PAGE_HEADER = (By.XPATH, "//h1[contains(text(), 'Your cart')]")

    def verify_cart_page(self, ):
        self.verify_element_text('Your cart', *self.CART_PAGE_HEADER)

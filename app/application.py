from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage
class Application:

    def __init__(self, driver):
        self.driver = driver

        self.home_page = HomePage(self.driver)
        self.product_details_page = ProductDetailsPage(self.driver)
        self.cart_page = CartPage(self.driver)

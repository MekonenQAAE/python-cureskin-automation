from pages.base_page import Page


class HomePage(Page):

    def open_product_details(self, url):
        self.open_url(url)

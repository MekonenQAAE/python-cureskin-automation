from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.base_url = 'https://shop.cureskin.com/'

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def open_url(self, url=''):
        self.driver.get(url)

    def verify_element_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, \
            f'Checking by locator {locator}. Expected {expected_text}, but got {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, \
            f'Checking by locator {locator}. Expected text {expected_text} is not in {actual_text}'

    def verify_element_int(self, expected_int, *locator):
        # cart_count = int(context.driver.find_element(*CART_QUANTITY).text)
        actual_text = int(self.driver.find_element(*locator).text[0])
        assert expected_int == actual_text, \
            f'Checking by locator {locator}. Expected {expected_int}, but got {actual_text}'

    def verify_element_displayed(self, *locator):
        assert self.find_element(*locator).is_displayed(), "element is not displayed"

    def wait_for_url_contains(self, url):
        self.wait.until(EC.url_contains(url))

    def wait_for_element_clickable(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator), message=f'Element not clickable by {locator}')

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator), message=f'Element not clickable by {locator}')
        e.click()

    def verify_url_contains_query(self, query):
        self.wait.until(EC.url_contains(query))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator), message='Element not present')

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_TITLE = (By.TAG_NAME, "//h1[contains(text(), 'Sepet')]")
    CART_ITEMS = (By.CSS_SELECTOR, ".sc-list-item")
    CART_ITEM_TITLES = (By.CSS_SELECTOR, ".sc-product-title")
    DELETE_BUTTON = (By.CSS_SELECTOR, "input[value='Sil']")
    EMPTY_CART_MESSAGE = (By.ID, "nav-cart-count")

    def verify_cart_page(self):
        element = self.find_element(self.CART_TITLE)
        return element is not None

    def get_cart_items(self):
        return self.find_elements(self.CART_ITEMS)

    def get_cart_item_titles(self):
        titles = self.find_elements(self.CART_ITEM_TITLES)
        return [title.text.strip() for title in titles]

    def verify_product_in_cart(self, product_title):
        item_titles = self.get_cart_item_titles()
        shortened_title = product_title[:15].lower()
        return any(shortened_title in title.lower() for title in item_titles)

    def delete_item_from_cart(self):
        if self.is_element_visible(self.DELETE_BUTTON):
            self.click_element(self.DELETE_BUTTON)
            time.sleep(2)
            return True
        return False

    def verify_cart_is_empty(self):
        element = self.find_element(self.EMPTY_CART_MESSAGE)
        return element and element.text.strip() == "0"
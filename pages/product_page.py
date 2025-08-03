from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_TITLE = (By.ID, "productTitle")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    ADDED_TO_CART_MSG = (By.CSS_SELECTOR, "#NATC_SMART_WAGON_CONF_MSG_SUCCESS")
    GO_TO_CART_BUTTON = (By.ID, "sw-gtc")

    def verify_on_product_page(self):
        if self.is_element_visible(self.PRODUCT_TITLE):
            return True

        current_url = self.get_current_url()
        return any(pattern in current_url for pattern in ["/dp/", "/gp/product/"])

    def get_product_title(self):
        return self.get_text(self.PRODUCT_TITLE)

    def add_to_cart(self):
        self.click_element(self.ADD_TO_CART_BUTTON)

    def verify_added_to_cart(self):
        return self.is_element_visible(self.ADDED_TO_CART_MSG)

    def go_to_cart(self):
        if self.is_element_visible(self.GO_TO_CART_BUTTON):
            self.click_element(self.GO_TO_CART_BUTTON)
        else:
            self.navigate_to("https://www.amazon.com.tr/gp/cart/view.html")
        return True

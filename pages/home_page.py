from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class HomePage(BasePage):
    COOKIE_ACCEPT = (By.ID, "sp-cc-accept")
    AMAZON_LOGO = (By.ID, "nav-logo-sprites")
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.amazon.com.tr/"

    def go_to_home_page(self):
        self.navigate_to(self.url)
        self.driver.E
        self.accept_cookies_if_present()

    def accept_cookies_if_present(self):
        try:
            cookie_btn = self.find_element(self.COOKIE_ACCEPT)
            if cookie_btn:
                cookie_btn.click()
            else:
                print("Çerez kabul butonu bulunamadı.")
        except:
            print("Çerez kontrolü sırasında hata oluştu.")

    def verify_on_home_page(self):
        result = self.is_element_visible(self.AMAZON_LOGO) and "amazon.com.tr" in self.get_current_url()
        return result

    def search_product(self, product_name):
        search_box = self.find_element(self.SEARCH_BOX)
        if search_box:
            search_box.clear()
            search_box.send_keys(product_name)
            search_box.send_keys(Keys.RETURN)
        else:
            print("Arama kutusu bulunamadı.")

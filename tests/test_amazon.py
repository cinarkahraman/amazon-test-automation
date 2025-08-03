import unittest
import time
import logging
from selenium import webdriver
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

# Logging yapılandırması
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TestAmazonShopping(unittest.TestCase):

    def setUp(self):
        """ Tarayıcıyı başlat ve Amazon ana sayfasına git """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.home_page.go_to_home_page()

    def test_amazon_shopping_flow(self):
        """ Amazon alışveriş sürecini test et... """
        logging.info("Ana sayfa doğrulanıyor...")
        self.assertTrue(self.home_page.verify_on_home_page(), "Ana sayfa doğrulanamadı.")
        time.sleep(3)

        logging.info("'samsung' araması yapılıyor...")
        self.home_page.search_product("samsung")
        logging.info("Arama sonuçları kontrol ediliyor...")
        self.assertTrue(self.search_results_page.verify_search_results("samsung"), "Arama sonuçları doğrulanamadı.")

        logging.info("2. sayfaya geçiliyor...")
        self.search_results_page.go_to_page(2)
        self.assertTrue(self.search_results_page.verify_current_page(2), "2. sayfada olmadığı doğrulandı.")
        time.sleep(3)

        logging.info("Üçüncü ürüne tıklanıyor...")
        self.search_results_page.click_product_by_index(2)
        logging.info("Ürün sayfası doğrulanıyor...")
        self.assertTrue(self.product_page.verify_on_product_page(), "Ürün sayfasında olunduğu doğrulanamadı.")
        time.sleep(3)
        product_title = self.product_page.get_product_title()
        logging.info(f"Seçilen ürün: {product_title}")

        logging.info("Ürün sepete ekleniyor...")
        self.product_page.add_to_cart()
        logging.info("Sepete ürün eklendiğini doğrula...")
        self.assertTrue(self.product_page.verify_added_to_cart(), "Ürün sepete eklenmedi.")
        time.sleep(3)
        logging.info("Sepete gidiliyor...")
        self.product_page.go_to_cart()
        logging.info("Sepette doğru ürün olduğunu doğrula...")
        self.assertTrue(self.cart_page.verify_product_in_cart(product_title), "Sepette doğru ürün bulunamadı.")
        time.sleep(3)
        logging.info("Ürün sepetten siliniyor...")
        self.cart_page.delete_item_from_cart()
        time.sleep(3)
        logging.info("Sepette ürün kalmadığını doğrula...")
        self.assertTrue(self.cart_page.verify_cart_is_empty(), "Ürün sepetten silinemedi.")

        logging.info("Ana sayfaya geri dönülüyor...")
        self.home_page.go_to_home_page()
        self.assertTrue(self.home_page.verify_on_home_page(), "Ana sayfa doğrulanamadı.")

    def tearDown(self):
        """ Tarayıcıyı kapat """
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

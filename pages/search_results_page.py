import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
    PAGINATION_NEXT = (By.CSS_SELECTOR, "a.s-pagination-item[href*='page=']")
    PAGINATION_CURRENT = (By.CSS_SELECTOR, ".s-pagination-selected")
    PRODUCT_LINKS = (By.CSS_SELECTOR, ".s-result-item .a-link-normal.s-no-outline")

    def verify_search_results(self, search_term):
        results = self.find_elements(self.SEARCH_RESULTS)
        if not results:
            return False
        page_title = self.driver.title.lower()
        return search_term.lower() in page_title and len(results) > 0

    def verify_current_page(self, page_number):
        current_page_element = self.find_element(self.PAGINATION_CURRENT)
        if current_page_element and current_page_element.text.strip() == str(page_number):
            return True
        current_url = self.get_current_url()
        return f"page={page_number}" in current_url or f"&p={page_number}" in current_url

    def click_product_by_index(self, index):
        products = self.find_elements(self.PRODUCT_LINKS)
        if products and 0 <= index < len(products):
            products[index].click()
            return True
        return False

    def go_to_page(self, page_number):

        page_link = (By.CSS_SELECTOR, f"a.s-pagination-item[href*='page={page_number}']")
        if self.is_element_visible(page_link):
            self.click_element(page_link)
            return True

        current_page = 1
        max_attempts = min(page_number - current_page, 5)

        for _ in range(max_attempts):
            if self.is_element_visible(self.PAGINATION_NEXT):
                self.click_element(self.PAGINATION_NEXT)
                time.sleep(2)
                current_page += 1
                if current_page == page_number:
                    return True
        return False

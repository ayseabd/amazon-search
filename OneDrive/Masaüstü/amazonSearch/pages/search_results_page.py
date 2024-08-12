from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    PAGE_2 = (By.LINK_TEXT, "2")

    def verify_results(self):
        assert "samsung" in self.driver.page_source

    def go_to_page_2(self):
        self.click_element(*self.PAGE_2)
        self.wait_for_url_contains("page=2", timeout=10)

    def verify_page_2(self):
        assert "page=2" in self.driver.current_url, "2. Sayfa doğru yüklenmedi."

    def click_product_on_5th_row_1st_column(self):
        # İkinci sayfaya geçtiğinden emin ol
        self.verify_page_2()

        # 5. satır ve 1. sütun ürününü seç
        products = self.driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
        if len(products) >= 5:
            product = products[4]  # 5. satır
            product_link = product.find_element(By.XPATH, ".//h2/a")
            product_link.click()
        else:
            raise Exception("Yeterli ürün bulunamadı.")

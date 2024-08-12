from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_LINK = (By.XPATH, "(//div[@data-component-type='s-search-result'])[5]//h2/a")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")

    def select_product(self):
        self.click_element(*self.PRODUCT_LINK)

    def verify_product_page(self):
        assert "dp" in self.driver.current_url, "Ürün sayfasında değiliz"

    def add_to_cart(self):
        self.click_element(*self.ADD_TO_CART_BUTTON)

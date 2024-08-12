from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_HEADER = (By.CLASS_NAME, 'sc-your-amazon-cart-is-empty')
    MAIN_LOGO = (By.ID, "nav-logo-sprites")

    def verify_cart_page(self):
        assert "cart" in self.driver.current_url, "Sepet sayfasında değiliz"

    def click_main_header_logo(self):
        self.click_element(*self.MAIN_LOGO)

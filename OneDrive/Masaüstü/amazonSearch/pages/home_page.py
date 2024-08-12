from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    LOGO = (By.ID, "nav-logo-sprites")

    def search(self, keyword):
        search_field = self.find(*self.SEARCH_BOX)
        search_field.send_keys(keyword)
        search_field.send_keys(Keys.RETURN)

    def click_logo(self):
        self.click_element(*self.LOGO)

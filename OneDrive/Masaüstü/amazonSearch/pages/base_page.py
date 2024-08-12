from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def accept_cookies(self):
        try:
            accept_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "sp-cc-accept"))  # ID'yi uygun şekilde değiştirin
            )
            accept_button.click()
        except Exception as e:
            print(f"Çerez kabul edilirken bir hata oluştu: {e}")
            pass

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def hover_element(self, *locator):
        element = self.find(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_current_url(self):
        return self.driver.current_url

    def wait_element(self, method, message=''):
        return self.wait.until(EC.element_to_be_clickable(method), message)

    def get_text(self, locator):
        return self.wait_element(locator).text

    def get_nth_element(self, index, *locator):
        return self.driver.find_elements(*locator)[index]

    def wait_for_url_contains(self, text, timeout=10):
        self.wait.until(EC.url_contains(text))

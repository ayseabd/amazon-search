from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.search_results_page import SearchResultsPage
from tests.base_test import BaseTest


class TestAmazonSearching(BaseTest):

    def test_amazon_shopping(self):
        home_page = HomePage(self.driver)
        # Çerezleri kabul et
        home_page.accept_cookies()

        # 1. Ana sayfanın açıldığını doğrula
        self.assertIn("amazon.com.tr", home_page.get_current_url(), "Amazon Anasayfa Açılmadı")

        # 2. 'samsung' araması yap
        home_page.search("samsung")

        # 3. Arama sonucunun samsung içerdiğini doğrula
        search_results_page = SearchResultsPage(self.driver)
        search_results_page.verify_results()

        # 4. 2. sayfaya git ve doğrula
        search_results_page.go_to_page_2()

        # 5. 2. sayfanın 5. satır 1. sütun ürününe tıkla
        search_results_page.click_product_on_5th_row_1st_column()

        # 6. Ürün sayfasında olduğumuzu doğrula
        product_page = ProductPage(self.driver)
        product_page.verify_product_page()

        # 7. Ürünü sepete ekle
        product_page.add_to_cart()

        # 8. Sepet sayfasında olduğumuzu doğrula
        cart_page = CartPage(self.driver)
        cart_page.verify_cart_page()

        # 9. Ana sayfaya geri dön ve doğru URL'yi kontrol et
        cart_page.click_main_header_logo()
        self.assertEqual("https://www.amazon.com.tr/ref=nav_logo", home_page.get_current_url(),
                         "Amazon Anasayfa Açılmadı")

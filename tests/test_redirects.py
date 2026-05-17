import allure
from pages.main_page import MainPage
from constants import Urls

@allure.feature("Редиректы по логотипам")
class TestRedirects:
    
    @allure.title("При нажатии на логотип Самоката открывается главная страница")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.FULL_MAIN_URL)
        
        main_page.click_order_top_button()
        main_page.click_scooter_logo_and_wait()
        main_page.wait_for_main_page_url()
        
        assert main_page.get_current_url() == Urls.FULL_MAIN_URL, \
            "Логотип Самоката не привёл на главную страницу"
    
    @allure.title("При нажатии на логотип Яндекса открывается ya.ru в новой вкладке")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.FULL_MAIN_URL)
        
        main_page.click_yandex_logo_and_wait_new_window()
        main_page.wait_for_url_contains("ya.ru")
        
        current_url = main_page.get_current_url()
        assert "ya.ru" in current_url or "yandex" in current_url.lower(), \
            f"Логотип Яндекса не привёл на ya.ru. Текущий URL: {current_url}"
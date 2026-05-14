import allure
from pages.main_page import MainPage
from constants import Urls

@allure.feature("Редиректы по логотипам")
class TestRedirects:
    
    @allure.title("Клик по логотипу Самоката возвращает на главную страницу")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        driver.get(Urls.BASE_URL)
        
        # Переходим на страницу заказа
        main_page.click_order_top_button()
        
        # Кликаем на логотип Самоката и проверяем редирект (все внутри метода)
        main_page.click_scooter_logo_and_wait_for_main_page()
    
    @allure.title("Клик по логотипу Яндекса открывает ya.ru в новой вкладке")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        driver.get(Urls.BASE_URL)
        
        # Кликаем на логотип Яндекса и проверяем открытие ya.ru (все внутри метода)
        main_page.click_yandex_logo_and_check_url()
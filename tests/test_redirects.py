import allure
from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Редиректы по логотипам")
class TestRedirects:
    
    @allure.title("Клик по логотипу Самоката возвращает на главную страницу")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.education-services.ru/")
        
        # Переходим на страницу заказа, чтобы потом проверить возврат на главную
        main_page.click_order_top_button()
        assert "order" in driver.current_url.lower(), "Не перешли на страницу заказа"
        
        # Кликаем на логотип Самоката
        main_page.click_scooter_logo()
        
        # Ожидаем, что вернулись на главную страницу
        WebDriverWait(driver, 5).until(
            EC.url_to_be("https://qa-scooter.education-services.ru/")
        )
        
        assert driver.current_url == "https://qa-scooter.education-services.ru/", \
            "Логотип Самоката не привёл на главную страницу"
    
    @allure.title("Клик по логотипу Яндекса открывает ya.ru в новой вкладке")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.education-services.ru/")
        
        # Получаем текущую вкладку
        original_window = driver.current_window_handle
        
        # Кликаем на логотип Яндекса
        main_page.click_yandex_logo()
        
        # Ожидаем открытия новой вкладки (максимум 5 секунд)
        WebDriverWait(driver, 5).until(
            lambda d: len(d.window_handles) > 1
        )
        
        # Переключаемся на новую вкладку
        new_window = [w for w in driver.window_handles if w != original_window][0]
        driver.switch_to.window(new_window)
        
        # Ожидаем загрузки страницы ya.ru
        WebDriverWait(driver, 10).until(
            lambda d: d.current_url != "about:blank"
        )
        
        # Проверяем URL новой вкладки
        assert "ya.ru" in driver.current_url or "yandex" in driver.current_url.lower(), \
            f"Логотип Яндекса не привёл на ya.ru. Текущий URL: {driver.current_url}"
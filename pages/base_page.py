from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_locators import BaseLocators
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def click_element(self, locator):
        with allure.step(f"Клик на элемент: {locator}"):
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
    
    def send_keys(self, locator, text):
        with allure.step(f"Ввод текста '{text}' в поле: {locator}"):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
    
    def get_text(self, locator):
        with allure.step(f"Получение текста из элемента: {locator}"):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text
    
    def is_element_displayed(self, locator):
        with allure.step(f"Проверка отображения элемента: {locator}"):
            try:
                return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
            except:
                return False
    
    def scroll_to_element(self, locator):
        with allure.step(f"Скролл до элемента: {locator}"):
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    def click_scooter_logo(self):
        with allure.step("Клик на логотип Самоката"):
            self.click_element(BaseLocators.SCOOTER_LOGO)
    
    def click_yandex_logo(self):
        with allure.step("Клик на логотип Яндекса"):
            self.click_element(BaseLocators.YANDEX_LOGO)
            self.driver.switch_to.window(self.driver.window_handles[1])
    
    # ========== НОВЫЕ МЕТОДЫ ДЛЯ ТЕСТОВ ==========
    
    def wait_for_url_to_be(self, expected_url, timeout=5):
        with allure.step(f"Ожидание URL: {expected_url}"):
            WebDriverWait(self.driver, timeout).until(
                EC.url_to_be(expected_url)
            )
    
    def get_current_url(self):
        with allure.step("Получение текущего URL"):
            return self.driver.current_url
    
    def get_window_handles(self):
        return self.driver.window_handles
    
    def switch_to_window(self, window_handle):
        with allure.step(f"Переключение на окно: {window_handle}"):
            self.driver.switch_to.window(window_handle)
    
    def wait_for_new_window_and_switch(self, original_handles, timeout=5):
        with allure.step("Ожидание открытия новой вкладки"):
            WebDriverWait(self.driver, timeout).until(
                lambda d: len(d.window_handles) > len(original_handles)
            )
            new_handles = self.driver.window_handles
            for handle in new_handles:
                if handle not in original_handles:
                    self.driver.switch_to.window(handle)
                    return handle
            return None
    
    def wait_for_url_contains(self, text, timeout=10):
        with allure.step(f"Ожидание URL содержит: {text}"):
            WebDriverWait(self.driver, timeout).until(
                lambda d: text in d.current_url and d.current_url != "about:blank"
            )
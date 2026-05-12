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
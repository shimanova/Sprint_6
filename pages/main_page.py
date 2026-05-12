from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_order_top_button(self):
        with allure.step("Клик на кнопку Заказать (верхняя)"):
            self.click_element(MainPageLocators.ORDER_TOP_BUTTON)
    
    def click_order_bottom_button(self):
        with allure.step("Клик на кнопку Заказать (нижняя)"):
            self.scroll_to_element(MainPageLocators.ORDER_BOTTOM_BUTTON)
            self.click_element(MainPageLocators.ORDER_BOTTOM_BUTTON)
    
    def click_question(self, index):
        with allure.step(f"Клик на вопрос c индексом {index}"):
            self.scroll_to_element(MainPageLocators.QUESTION_BUTTONS[index])
            self.click_element(MainPageLocators.QUESTION_BUTTONS[index])
    
    def get_answer_text(self, index):
        with allure.step(f"Получение текста ответа c индексом {index}"):
            self.scroll_to_element(MainPageLocators.ANSWER_PANELS[index])
            return self.get_text(MainPageLocators.ANSWER_PANELS[index])
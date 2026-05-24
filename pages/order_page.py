from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_first_form(self, name, surname, address, metro, phone):
        with allure.step("Заполнение первой формы заказа"):
            self.send_keys(OrderPageLocators.NAME_FIELD, name)
            self.send_keys(OrderPageLocators.SURNAME_FIELD, surname)
            self.send_keys(OrderPageLocators.ADDRESS_FIELD, address)
            self.send_keys(OrderPageLocators.METRO_STATION, metro)
            metro_option = (By.XPATH, f"//div[contains(text(), '{metro}')]")
            self.click_element(metro_option)
            self.send_keys(OrderPageLocators.PHONE_FIELD, phone)
    
    def click_next(self):
        with allure.step("Клик на кнопку Далее"):
            self.click_element(OrderPageLocators.NEXT_BUTTON)
    
    def fill_second_form_black(self, date, rental_days, comment):
        with allure.step("Заполнение второй формы заказа (чёрный жемчуг)"):
            self.send_keys(OrderPageLocators.DATE_FIELD, date)
            self.click_element(OrderPageLocators.RENTAL_PERIOD)
            rental_locator = (OrderPageLocators.RENTAL_OPTION[0], 
                              OrderPageLocators.RENTAL_OPTION[1].format(days=rental_days))
            self.click_element(rental_locator)
            self.click_element(OrderPageLocators.COLOR_BLACK)
            if comment:
                self.send_keys(OrderPageLocators.COMMENT_FIELD, comment)
    
    def fill_second_form_grey(self, date, rental_days, comment):
        with allure.step("Заполнение второй формы заказа (серая безысходность)"):
            self.send_keys(OrderPageLocators.DATE_FIELD, date)
            self.click_element(OrderPageLocators.RENTAL_PERIOD)
            rental_locator = (OrderPageLocators.RENTAL_OPTION[0], 
                              OrderPageLocators.RENTAL_OPTION[1].format(days=rental_days))
            self.click_element(rental_locator)
            self.click_element(OrderPageLocators.COLOR_GREY)
            if comment:
                self.send_keys(OrderPageLocators.COMMENT_FIELD, comment)
    
    def click_order(self):
        with allure.step("Клик на кнопку Заказать в форме"):
            self.click_element(OrderPageLocators.ORDER_BUTTON)
    
    def confirm_order(self):
        with allure.step("Подтверждение заказа в модальном окне"):
            self.click_element(OrderPageLocators.YES_BUTTON)
    
    def is_order_successful(self):
        with allure.step("Проверка успешного создания заказа"):
            return self.is_element_displayed(OrderPageLocators.SUCCESS_MESSAGE)
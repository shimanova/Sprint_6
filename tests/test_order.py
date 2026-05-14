import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from constants import Urls, OrderData

@allure.feature("Заказ самоката")
class TestOrder:
    
    @allure.title("Заказ самоката через верхнюю кнопку (чёрный жемчуг)")
    def test_order_top_button_black(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        driver.get(Urls.BASE_URL)
        main_page.click_order_top_button()
        
        data = OrderData.ORDER_TOP_BUTTON_DATA
        order_page.fill_first_form(
            data["name"], data["surname"], data["address"], 
            data["metro"], data["phone"]
        )
        order_page.click_next()
        order_page.fill_second_form_black(
            data["date"], data["rental_days"], data["comment"]
        )
        order_page.click_order()
        order_page.confirm_order()
        
        assert order_page.is_order_successful(), "Заказ не был оформлен"
    
    @allure.title("Заказ самоката через нижнюю кнопку (серая безысходность)")
    def test_order_bottom_button_grey(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        driver.get(Urls.BASE_URL)
        main_page.click_order_bottom_button()
        
        data = OrderData.ORDER_BOTTOM_BUTTON_DATA
        order_page.fill_first_form(
            data["name"], data["surname"], data["address"], 
            data["metro"], data["phone"]
        )
        order_page.click_next()
        order_page.fill_second_form_grey(
            data["date"], data["rental_days"], data["comment"]
        )
        order_page.click_order()
        order_page.confirm_order()
        
        assert order_page.is_order_successful(), "Заказ не был оформлен"
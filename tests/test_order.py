import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.feature("Заказ самоката")
class TestOrder:
    
    ORDER_DATA = [
        ("Тест", "Тестик", "Москва, Кутузовский проезд 4", "Кутузовская", "89991234567", 
         "13.05.2025", "сутки", "чёрный жемчуг", "Позвонить за час", "top"),
        ("Тестов", "Тестовидзе", "Санкт-Петербург, Воздухоплавательная 5", "Парк Победы", "89997654321", 
         "15.05.2026", "трое суток", "серая безысходность", "", "bottom"),
    ]
    
    @allure.title("Позитивный сценарий заказа самоката")
    @pytest.mark.parametrize("name,surname,address,metro,phone,date,rental_days,color,comment,button_position", ORDER_DATA)
    def test_order_scooter(self, driver, name, surname, address, metro, phone, date, rental_days, color, comment, button_position):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        driver.get("https://qa-scooter.education-services.ru/")
        
        if button_position == "top":
            main_page.click_order_top_button()
        else:
            main_page.click_order_bottom_button()
        
        order_page.fill_first_form(name, surname, address, metro, phone)
        order_page.click_next()
        
        order_page.fill_second_form(date, rental_days, color, comment)
        order_page.click_order()
        
        order_page.confirm_order()
        
        assert order_page.is_order_successful(), "Заказ не был оформлен"
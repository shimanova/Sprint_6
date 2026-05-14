import allure
import pytest
from pages.main_page import MainPage
from constants import Urls, OrderData

@allure.feature("Вопросы о важном")
class TestFAQ:
    
    @allure.title("Проверка текста ответа на вопрос {index}")
    @pytest.mark.parametrize("index, expected_text", enumerate(OrderData.FAQ_EXPECTED_ANSWERS))
    def test_question_answer(self, driver, index, expected_text):
        main_page = MainPage(driver)
        driver.get(Urls.BASE_URL)
        
        main_page.click_question(index)
        actual_answer = main_page.get_answer_text(index)
        
        assert actual_answer == expected_text, \
            f"Текст ответа на вопрос {index} не совпадает.\nОжидалось: {expected_text}\nПолучено: {actual_answer}"
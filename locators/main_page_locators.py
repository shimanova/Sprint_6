from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_TOP_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
    
    QUESTION_BUTTONS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7"),
    ]
    
    ANSWER_PANELS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7"),
    ]
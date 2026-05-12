from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='{days}']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    
    CONFIRM_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    NO_BUTTON = (By.XPATH, "//button[text()='Нет']")
    
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")
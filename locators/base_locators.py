from selenium.webdriver.common.by import By

class BaseLocators:
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")  # Обратите внимание: alt='Scooter' (без blueprint)
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
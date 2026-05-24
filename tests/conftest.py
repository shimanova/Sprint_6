import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import os

@pytest.fixture
def driver():
    driver_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "geckodriver.exe")
    service = Service(driver_path)
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()
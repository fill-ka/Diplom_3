import pytest
from selenium import webdriver
from locators.variables import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(params=['firefox', 'chrome'])
def init_driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(BASE_URL.MAIN_PAGE_URL)
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(BASE_URL.MAIN_PAGE_URL)
    yield driver
    driver.quit()

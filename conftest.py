import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(service=ChromeService())
    elif request.param == "firefox":
        driver = webdriver.Firefox(service=FirefoxService())

    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

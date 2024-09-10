from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Open URL: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Click element located by {by} with value {value}")
    def click(self, by, value):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    @allure.step("Get text of element located by {by} with value {value}")
    def get_text(self, by, value):
        element = self.wait.until(EC.presence_of_element_located((by, value)))
        return element.text

    @allure.step("Input text '{text}' into element located by {by} with value {value}")
    def input_text(self, by, value, text):
        element = self.wait.until(EC.presence_of_element_located((by, value)))
        element.clear()
        element.send_keys(text)

from locators.locators import AccountPageLocators
from locators.variables import *
from selenium.webdriver.common.by import By

class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(f"{BASE_URL}/account")

    def login(self, email, password):
        self.driver.get(f"{BASE_URL}/login")
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    def go_to_order_history(self):
        history_button = self.driver.find_element(*AccountPageLocators.ORDER_HISTORY_BUTTON)
        history_button.click()

    def logout(self):
        logout_button = self.driver.find_element(*AccountPageLocators.LOGOUT_BUTTON)
        logout_button.click()
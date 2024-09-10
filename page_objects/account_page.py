import allure

from locators.locators import *
from locators.variables import *
from selenium.webdriver.common.by import By

class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Open Account Page")
    def open(self):
        self.driver.get(f"{BASE_URL}/account")

    @allure.step("Login with email {email} and password {password}")
    def login(self, email, password):
        self.driver.get(f"{BASE_URL}/login")
        self.driver.find_element(*PasswordResetLocators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*PasswordResetLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*PasswordResetLocators.LOGIN_BUTTON).click()

    @allure.step("Go to Order History")
    def go_to_order_history(self):
        history_button = self.driver.find_element(*AccountPageLocators.ORDER_HISTORY_BUTTON)
        history_button.click()

    @allure.step("Logout")
    def logout(self):
        logout_button = self.driver.find_element(*AccountPageLocators.LOGOUT_BUTTON)
        logout_button.click()

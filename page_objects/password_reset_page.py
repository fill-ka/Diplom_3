from locators.locators import PasswordResetLocators
from locators.variables import *

class PasswordResetPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(f"{BASE_URL}//forgot-password")

    def enter_email(self, email):
        email_input = self.driver.find_element(*PasswordResetLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

    def click_reset_button(self):
        reset_button = self.driver.find_element(*PasswordResetLocators.RESET_BUTTON)
        reset_button.click()

    def toggle_password_visibility(self):
        toggle_button = self.driver.find_element(*PasswordResetLocators.TOGGLE_PASSWORD)
        toggle_button.click()

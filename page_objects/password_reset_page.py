from locators.locators import *
from locators.variables import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PasswordResetPage:
    def __init__(self, driver):
        self.wait = None
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

    @property
    def is_password_visible(self):
        password_field = self.wait.until(EC.visibility_of_element_located(*PasswordResetLocators.PASSWORD_INPUT))
        return password_field.get_attribute('type') == 'text'
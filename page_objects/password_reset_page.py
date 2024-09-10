from locators.locators import *
from locators.variables import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base_page import *


class PasswordResetPage(BasePage):

    @allure.step("Open the password reset page")
    def open(self):
        self.driver.get(f"{BASE_URL}//forgot-password")

    @allure.step("Enter email address: {email}")
    def enter_email(self):
        email_input = self.driver.find_element(*PasswordResetLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

    @allure.step("Click the reset button")
    def click_reset_button(self):
        reset_button = self.driver.find_element(*PasswordResetLocators.RESET_BUTTON)
        reset_button.click()

    @allure.step("Toggle password visibility")
    def toggle_password_visibility(self):
        toggle_button = self.driver.find_element(*PasswordResetLocators.TOGGLE_PASSWORD)
        toggle_button.click()

    @property
    @allure.step("Check if password is visible")
    def is_password_visible(self):
        password_field = self.wait.until(EC.visibility_of_element_located(*PasswordResetLocators.PASSWORD_INPUT))
        return password_field.get_attribute('type') == 'text'

    @allure.step("Check if on the password recovery page")
    def is_on_recovery_password_page(self):
        try:
            element = self.wait.until(EC.presence_of_element_located(*PasswordResetLocators.PASSWORD_RECOVERY))
            return element.text == "Восстановление пароля"
        except:
            return False

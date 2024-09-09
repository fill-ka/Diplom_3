from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.variables import *
from locators.locators import *


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        # Открываем страницу логина
        self.driver.get(f"{BASE_URL}/login")

    def login(self, email, password):
        # Вводим email
        self.driver.find_element(*PasswordResetLocators.EMAIL_INPUT).send_keys(email)
        # Вводим пароль
        self.driver.find_element(*PasswordResetLocators.PASSWORD_INPUT).send_keys(password)
        # Кликаем по кнопке "Войти"
        self.driver.find_element(*PasswordResetLocators.LOGIN_BUTTON).click()

        # Ждём, пока не откроется страница личного кабинета
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/account")
        )

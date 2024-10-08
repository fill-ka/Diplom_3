import allure
import pytest
from page_objects.password_reset_page import PasswordResetPage
from locators.variables import *


@pytest.mark.usefixtures("init_driver")
class TestPasswordReset:

    def __init__(self):
        self.driver = None

    @allure.title("Navigationt to password recovery page")
    def test_password_reset_navigation(self):
        page = PasswordResetPage(self.driver)
        page.open(BASE_URL)
        assert "reset-password" in self.driver.current_url

    @allure.title("Password reset functionality")
    def test_password_reset_functionality(self):
        page = PasswordResetPage(self.driver)
        page.open(BASE_URL)
        page.enter_email(email)
        page.click_reset_button()
        assert page.is_on_recovery_password_page()

    @allure.title("Visible password toggle")

    def test_toggle_password_visibility(self):
        page = PasswordResetPage(self.driver)
        page.open(BASE_URL)
        page.toggle_password_visibility()
        assert page.is_password_visible(), "Password should be visible after toggling"

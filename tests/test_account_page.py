import allure
import pytest
from page_objects.account_page import AccountPage
from locators.variables import *
from page_objects.login_page import LoginPage


@pytest.mark.usefixtures("init_driver")
class TestAccountPage:

    def __init__(self):
        self.driver = None

    @allure.title("Navigate to Account Page")
    def test_account_navigation(self, init_driver):
        page = AccountPage(init_driver)
        login_page = LoginPage(init_driver)

        login_page.open(BASE_URL)
        login_page.login(email, password)

        page.open(BASE_URL)
        assert "account" in init_driver.current_url

    @allure.title("Go to Order History")
    def test_go_to_order_history(self):
        page = AccountPage(self.driver)
        page.open(BASE_URL)
        page.go_to_order_history()
        assert "account/orders" in self.driver.current_url

    @allure.title("Logout")
    def test_logout(self):
        page = AccountPage(self.driver)
        page.open(BASE_URL)
        page.logout()
        assert "login" in self.driver.current_url

import pytest
from page_objects.order_history_page import OrderHistoryPage
from page_objects.account_page import AccountPage
from page_objects.login_page import LoginPage
from locators.variables import *

@pytest.mark.usefixtures("init_driver")
class TestOrderHistory():

    def __init__(self):
        self.driver = None

    def test_go_to_order_history(self, browser):
        page = AccountPage(browser)
        login_page = LoginPage(browser)

        # Авторизуемся
        login_page.open()
        login_page.login(email, password)

        # Переходим в историю заказов
        page.go_to_order_history()
        assert "account/orders" in browser.current_url

    def test_order_details_popup(self):
        page = OrderHistoryPage(self.driver)
        page.open()
        page.click_on_order(1)
        assert page.is_order_popup_visible()

    def test_order_count_increases(self):
        page = OrderHistoryPage(self.driver)
        initial_count = page.get_order_count()
        page.create_new_order()
        assert page.get_order_count() > initial_count

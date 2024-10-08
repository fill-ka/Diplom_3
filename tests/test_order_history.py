import allure
import pytest
from page_objects.order_history_page import OrderHistoryPage
from page_objects.account_page import AccountPage
from page_objects.login_page import LoginPage
from locators.variables import *


@pytest.mark.usefixtures("init_driver")
class TestOrderHistory:

    def __init__(self):
        self.driver = None

    @allure.title("Go to order history page")
    def test_go_to_order_history(self, init_driver):
        page = AccountPage(init_driver)
        login_page = LoginPage(init_driver)

        login_page.open(BASE_URL)
        login_page.login(email, password)

        page.go_to_order_history()
        assert "account/orders" in init_driver.current_url

    @allure.title("Visible order details popup")
    def test_order_details_popup(self):
        page = OrderHistoryPage(self.driver)
        page.open(BASE_URL)
        page.click_on_order(1)
        assert page.is_order_popup_visible()

    @allure.title("Order count increases")
    def test_order_count_increases(self):
        page = OrderHistoryPage(self.driver)
        initial_count = page.get_order_count()
        page.create_new_order()
        assert page.get_order_count() > initial_count

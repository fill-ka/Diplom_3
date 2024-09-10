import allure
import pytest
from page_objects.oreder_feed_page import OrdersFeedPage


@pytest.mark.usefixtures("init_driver")
class TestOrdersFeed:

    def __init__(self):
        self.driver = None

    @allure.title("View order details")
    def test_view_order_details(self):
        page = OrdersFeedPage(self.driver)
        page.open()
        page.view_order_details("#0116823")
        order_number_displayed = page.get_order_number()
        assert order_number_displayed == "#0116823"

    @allure.title("Order counts")
    def test_order_counts(self):
        page = OrdersFeedPage(self.driver)
        page.open()
        total_count, today_count = page.check_order_counts()
        assert int(total_count) > 0
        assert int(today_count) > 0

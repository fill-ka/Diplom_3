from locators.locators import OrderHistoryPageLocators
from locators.variables import *
from page_objects.base_page import BasePage
import allure


class OrderHistoryPage(BasePage):

    @allure.step("Open the order history page")
    def open(self):
        self.driver.get(f"{BASE_URL}/account/order-history")

    @allure.step("Click on order at index {order_index}")
    def click_on_order(self, order_index):
        orders = self.driver.find_elements(*OrderHistoryPageLocators.ORDER_ITEM)
        orders[order_index].click()

    @allure.step("Check if the order details popup is visible")
    def is_order_popup_visible(self):
        return self.driver.find_element(*OrderHistoryPageLocators.ORDER_DETAILS_POPUP).is_displayed()

    @allure.step("Get the order count from the order history")
    def get_order_count(self):
        count_element = self.driver.find_element(*OrderHistoryPageLocators.ORDER_COUNT)
        return int(count_element.text)

    @allure.step("Create a new order")
    def create_new_order(self):
        create_button = self.driver.find_element(*OrderHistoryPageLocators.CREATE_ORDER_BUTTON)
        create_button.click()

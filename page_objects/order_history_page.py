from locators.locators import OrderHistoryPageLocators
from locators.variables import *

class OrderHistoryPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(f"{BASE_URL}/account/order-history")

    def click_on_order(self, order_index):
        orders = self.driver.find_elements(*OrderHistoryPageLocators.ORDER_ITEM)
        orders[order_index].click()

    def is_order_popup_visible(self):
        return self.driver.find_element(*OrderHistoryPageLocators.ORDER_DETAILS_POPUP).is_displayed()

    def get_order_count(self):
        count_element = self.driver.find_element(*OrderHistoryPageLocators.ORDER_COUNT)
        return int(count_element.text)

    def create_new_order(self):
        create_button = self.driver.find_element(*OrderHistoryPageLocators.CREATE_ORDER_BUTTON)
        create_button.click()

from locators.locators import *
from locators.variables import *
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ConstructorPage(BasePage):

    def open(self, url):
        self.driver.get(BASE_URL)

    def click_constructor(self):
        constructor_button = self.driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

    def go_to_orders_feed(self):
        orders_feed_button = self.wait.until(EC.element_to_be_clickable(*ConstructorPageLocators.LENTA_ZAKAZOV))
        orders_feed_button.click()

    def add_ingredient_to_order(self, ingredient_name):
        self.click(By.XPATH, f".//p[text()='{ingredient_name}']")

    def get_ingredient_counter(self, ingredient_name):
        counter = self.driver.find_element(By.XPATH,
                                           f"//span[text()='{ingredient_name}']/../..//span[@class='order-counter']")
        return int(counter.text)

    def place_order(self):
        place_order_button = self.wait.until(
            EC.element_to_be_clickable(*ConstructorPageLocators.CREATE_ORDER))
        place_order_button.click()
        confirmation_message = self.wait.until(
            EC.visibility_of_element_located(*ConstructorPageLocators.ORDER_CONFIRMATION_MASSAGE))
        return confirmation_message.text

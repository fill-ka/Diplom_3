from locators.locators import ConstructorPageLocators
from locators.variables import *
from selenium.webdriver.common.by import By

class ConstructorPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(BASE_URL)

    def click_constructor(self):
        constructor_button = self.driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

    def add_ingredient_to_order(self, ingredient_name):
        ingredient = self.driver.find_element(By.XPATH, f".//p[text()='{ingredient_name}']")
        ingredient.click()
        add_button = self.driver.find_element(*ConstructorPageLocators.ADD_TO_ORDER_BUTTON)
        add_button.click()

    def get_ingredient_counter(self, ingredient_name):
        counter = self.driver.find_element(By.XPATH, f"//span[text()='{ingredient_name}']/../..//span[@class='order-counter']")
        return int(counter.text)

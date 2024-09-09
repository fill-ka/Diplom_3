from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.variables import *
from locators.locators import *


class OrdersFeedPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(f"{BASE_URL}/orders-feed")

    def view_order_details(self, order_id):
        order_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@data-id='{order_id}']")))
        order_element.click()

    def check_order_counts(self):
        total_count = self.wait.until(EC.visibility_of_element_located(*OrderFeedPageLocators.TOTAL_COUNTER)).text
        today_count = self.wait.until(EC.visibility_of_element_located(*OrderFeedPageLocators.TODAY_COUNT)).text
        return total_count, today_count

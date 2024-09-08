from selenium.webdriver.common.by import By

class PasswordResetLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    RESET_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    TOGGLE_PASSWORD = (By.CSS_SELECTOR, ".toggle-password-btn")

class AccountPageLocators:
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a[href='/account']")
    ORDER_HISTORY_BUTTON = (By.CSS_SELECTOR, "a[href='/account/orders']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "button.logout-btn")

class ConstructorPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    INGREDIENT_ITEM = (By.CSS_SELECTOR, ".ingredient-item")
    ADD_TO_ORDER_BUTTON = (By.XPATH, "//button[text()='Добавить']")
    ORDER_COUNTER = (By.CSS_SELECTOR, ".order-counter")

class OrderHistoryPageLocators:
    ORDER_ITEM = (By.CSS_SELECTOR, ".order-item")
    ORDER_DETAILS_POPUP = (By.CSS_SELECTOR, ".order-details-popup")
    ORDER_COUNT = (By.CSS_SELECTOR, ".order-count")
    CREATE_ORDER_BUTTON = (By.CSS_SELECTOR, "button.create-order-btn")

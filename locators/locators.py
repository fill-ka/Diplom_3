from selenium.webdriver.common.by import By


class PasswordResetLocators:
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")
    RESET_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    TOGGLE_PASSWORD = (By.CSS_SELECTOR, ".toggle-password-btn")
    PASSWORD_INPUT = (By.CSS_SELECTOR, ".//input[@type='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "//button[text()='Войти']")
    PASSWORD_RECOVERY = (By.XPATH, ".//h2[text()='Восстановление пароля']")


class AccountPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, ".//a[text() = 'Профиль']")
    ORDER_HISTORY_BUTTON = (By.XPATH, ".//a[text() = 'История заказов']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")


class ConstructorPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    INGREDIENT_ITEM = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")
    ADD_TO_ORDER_BUTTON = (By.XPATH, "//button[text()='Добавить']")
    ORDER_COUNTER = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow')]")
    LENTA_ZAKAZOV = (By.XPATH, ".//p[contains(text(), 'Лента Заказов')]")
    CREATE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_CONFIRMATION_MASSAGE = (By.XPATH, ".//div[contains(@class, 'Modal_modal__container')]")


class OrderHistoryPageLocators:
    ORDER_ITEM = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]")
    ORDER_DETAILS_POPUP = (By.CSS_SELECTOR, ".order-details-popup")
    ORDER_COUNT = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")


class OrderFeedPageLocators:
    TOTAL_COUNTER = (
        By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    TODAY_COUNT = (
        By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")

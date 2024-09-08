import pytest
from page_objects.password_reset_page import PasswordResetPage


@pytest.mark.usefixtures("init_driver")
class TestPasswordReset:

    def __init__(self):
        self.driver = None

    def test_password_reset_navigation(self):
        page = PasswordResetPage(self.driver)
        page.open()
        assert "reset-password" in self.driver.current_url

    def test_password_reset_functionality(self):
        page = PasswordResetPage(self.driver)
        page.open()
        page.enter_email("test@example.com")
        page.click_reset_button()
        # Проверка появления уведомления об успешном запросе (заглушка)

    def test_toggle_password_visibility(self):
        page = PasswordResetPage(self.driver)
        page.open()
        page.toggle_password_visibility()
        # Проверить, что поле подсвечивается или что пароль виден (заглушка)
